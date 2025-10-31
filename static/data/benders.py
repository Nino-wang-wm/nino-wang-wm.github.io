import gurobipy as gp
from gurobipy import GRB
import numpy as np
import time

# ----------------------- Direct Solve (baseline) -----------------------

def solve_direct(obj_coeffs, constraints, bounds, verbose=True):
    """
    Solve min c_x * x + c_y * y
    s.t.  coeff_y * y + coeff_x * x (<= or >=) rhs
          x_min <= x <= x_max, y >= y_min
    """
    model = gp.Model("Direct")
    model.setParam('OutputFlag', 0)

    x = model.addVar(lb=bounds['x_min'], ub=bounds['x_max'], name="x")
    y = model.addVar(lb=bounds['y_min'], name="y")

    model.setObjective(obj_coeffs['x'] * x + obj_coeffs['y'] * y, GRB.MINIMIZE)

    for i, c in enumerate(constraints):
        expr = c['coeff_y'] * y + c['coeff_x'] * x
        if c['type'] == '<=':
            model.addConstr(expr <= c['rhs'], name=f"c{i+1}")
        elif c['type'] == '>=':
            model.addConstr(expr >= c['rhs'], name=f"c{i+1}")
        else:
            raise ValueError("Constraint type must be '<=' or '>='")

    t0 = time.time()
    model.optimize()
    t1 = time.time()

    if model.Status != GRB.OPTIMAL:
        raise RuntimeError(f"Direct solve failed, status={model.Status}")

    xv, yv, zv = x.X, y.X, model.ObjVal
    if verbose:
        print("1) DIRECT SOLUTION")
        print("-" * 60)
        print(f"Optimal: x = {xv:.6g}, y = {yv:.6g}")
        print(f"Objective: {zv:.6g}")
        print(f"Solve time: {t1 - t0:.4f}s")
    return xv, yv, zv

# ----------------------- Subproblem at fixed x -----------------------

def solve_subproblem(x_fixed, obj_coeffs, constraints, bounds):
    """
    Subproblem: fix x = x_fixed; solve min c_y * y
    s.t. coeff_y * y <= rhs - coeff_x * x_fixed (or >=)
    Return: y*, theta (sub obj), slope = d theta(x) / dx via dual Pis.
    """
    model = gp.Model("Subproblem")
    model.setParam('OutputFlag', 0)

    y = model.addVar(lb=bounds['y_min'], name="y")
    model.setObjective(obj_coeffs['y'] * y, GRB.MINIMIZE)

    # Keep each constraint and its coeff_x to compute slope from Pis
    rows = []
    for i, c in enumerate(constraints):
        rhs_adj = c['rhs'] - c['coeff_x'] * x_fixed
        if c['type'] == '<=':
            con = model.addConstr(c['coeff_y'] * y <= rhs_adj, name=f"c{i+1}")
        elif c['type'] == '>=':
            con = model.addConstr(c['coeff_y'] * y >= rhs_adj, name=f"c{i+1}")
        else:
            raise ValueError("Constraint type must be '<=' or '>='")
        rows.append((con, c['coeff_x']))

    model.optimize()
    if model.Status != GRB.OPTIMAL:
        return None, float('inf'), None  # infeasible/unbounded -> caller handles

    # Gurobi: d obj* / d RHS_r = con.Pi   (true for both <= and >=)
    # RHS_r(x) = rhs_r - coeff_x_r * x  => dRHS/dx = -coeff_x_r
    pis = [con.Pi for (con, cx) in rows]
    cxs = [cx for (con, cx) in rows]
    slope = - sum(pi * cx for pi, cx in zip(pis, cxs))

    return y.X, model.ObjVal, float(slope)

# ----------------------- Master with accumulated cuts -----------------------

def solve_master_problem(cuts, obj_coeffs, bounds):
    """
    Master: min c_x * x + alpha
    s.t. x bounds, and for each cut: alpha >= intercept + slope * x
    """
    model = gp.Model("Master")
    model.setParam('OutputFlag', 0)

    x = model.addVar(lb=bounds['x_min'], ub=bounds['x_max'], name="x")
    alpha = model.addVar(lb=-GRB.INFINITY, name="alpha")  # alpha free below

    model.setObjective(obj_coeffs['x'] * x + alpha, GRB.MINIMIZE)

    for i, cut in enumerate(cuts):
        model.addConstr(alpha >= cut['intercept'] + cut['slope'] * x, name=f"cut_{i+1}")

    model.optimize()
    if model.Status != GRB.OPTIMAL:
        return None, None, None
    return x.X, alpha.X, model.ObjVal

# ----------------------- Benders driver -----------------------

def solve_benders(obj_coeffs, constraints, bounds, x_init, max_iter=100, tol=1e-6, verbose=True):
    """
    Classic Benders (LP, single subproblem). No alpha lower bound; use bootstrap cut.
    """
    if verbose:
        print("\n2) BENDERS DECOMPOSITION")
        print("-" * 60)

    t0 = time.time()
    cuts = []

    # ---- Bootstrap: use x_init to create the first cut, then solve the master once ----
    y0, theta0, slope0 = solve_subproblem(x_init, obj_coeffs, constraints, bounds)
    if y0 is None:
        raise RuntimeError("Subproblem infeasible at x_init; choose a different x_init.")
    cuts.append({'intercept': theta0 - slope0 * x_init, 'slope': slope0})

    x_val, alpha_val, z_down = solve_master_problem(cuts, obj_coeffs, bounds)
    if x_val is None:
        raise RuntimeError("Master failed at bootstrap.")

    if verbose:
        print("Iter     x         alpha      y         slope      z_up        z_down      gap")
        print("-" * 90)

    # ---- Main loop ----
    for it in range(1, max_iter + 1):
        y_val, theta, slope = solve_subproblem(x_val, obj_coeffs, constraints, bounds)
        if y_val is None:
            raise RuntimeError("Subproblem infeasible during iterations.")

        z_up = obj_coeffs['x'] * x_val + theta
        gap = z_up - z_down
        if verbose:
            print(f"{it:4d}  {x_val:10.6g}  {alpha_val:10.6g}  {y_val:10.6g}  {slope:10.6g}  "
                  f"{z_up:12.6g}  {z_down:12.6g}  {gap:10.6g}")

        if abs(gap) <= tol:
            t1 = time.time()
            if verbose:
                print("Converged.")
                print(f"Optimal: x = {x_val:.6g}, y = {y_val:.6g}")
                print(f"Objective: {z_up:.6g}")
                print(f"Solve time: {t1 - t0:.4f}s")
            return x_val, y_val, z_up, it

        # add new cut and re-solve master
        cuts.append({'intercept': theta - slope * x_val, 'slope': slope})
        x_val, alpha_val, z_down = solve_master_problem(cuts, obj_coeffs, bounds)
        if x_val is None:
            raise RuntimeError("Master failed after adding cuts.")

    t1 = time.time()
    if verbose:
        print("Did not converge within max_iter.")
        print(f"Solve time: {t1 - t0:.4f}s")
    return x_val, y_val, z_up, max_iter

# ----------------------- Instances -----------------------

def run_instance():

    obj = {'x': -1.5, 'y': -10.0}
    bounds = {'x_min': 0.0, 'x_max': 16.0, 'y_min': 0.0}
    cons = [
        {'coeff_y': 1.0,  'coeff_x': -1.5,  'rhs': 5.0,   'type': '<='},
        {'coeff_y': 1.0,  'coeff_x': -0.5,  'rhs': 7.5,   'type': '<='},
        {'coeff_y': 1.0,  'coeff_x':  0.5,  'rhs': 17.5,  'type': '<='},
        {'coeff_y': -1.0, 'coeff_x':  1.0,  'rhs': 10.0,  'type': '<='},
        # y >= 0 is via y_min in bounds
    ]
    expected = {'x': 10.0, 'y': 12.5, 'obj': -15.0}
    x_init = 2.5
    """

    # Mathematical formulation: minimize 2x + 3y
    # Constraints: x + y ≤ 12 (resource limit)
    #             2x - y ≤ 8 (processing constraint)
    #             -x + 2y ≤ 10 (balance constraint)
    #             x ≥ 3 (minimum production)
    #             0 ≤ x ≤ 15, y ≥ 0
    obj = {'x': -0.1, 'y': 0.125}  # min -0.2 x + 0.8 y
    bounds = {'x_min': 1, 'x_max': 15.0, 'y_min': 0.0}
    cons = [
        {'coeff_y': 5.0,  'coeff_x':  3, 'rhs': 150.0, 'type': '<='},  # y + 0.3x ≤ 11
        {'coeff_y': 3.0,  'coeff_x': -7, 'rhs':  116.0, 'type': '<='},  # y - 0.7x ≤ 6
        {'coeff_y': -12.0, 'coeff_x':  5, 'rhs':  117.0, 'type': '<='},  # -y + 0.5x ≤ 7  -> y ≥ 0.5x - 7
        {'coeff_y': 6.0,  'coeff_x': -1, 'rhs':  11.5, 'type': '>='},  # y - 0.1x ≥ 0.5
        
    ]   
    expected = None
    x_init = 0.5
    """

    print("Problem:")
    print(f"  Objective: min {obj['x']}*x + {obj['y']}*y")
    print(f"  Bounds: {bounds['x_min']} <= x <= {bounds['x_max']},  y >= {bounds['y_min']}")
    for i, c in enumerate(cons, 1):
        sign = '≤' if c['type'] == '<=' else '≥'
        print(f"  c{i}: {c['coeff_y']}*y + {c['coeff_x']}*x {sign} {c['rhs']}")
    if expected:
        print(f"  Expected: x*={expected['x']}, y*={expected['y']}, z*={expected['obj']}")

    # Direct
    x_d, y_d, z_d = solve_direct(obj, cons, bounds, verbose=True)

    # Benders
    x_b, y_b, z_b, it = solve_benders(obj, cons, bounds, x_init=x_init, max_iter=100, tol=1e-8, verbose=True)

    # Compare
    print("\n3) COMPARISON")
    print("-" * 60)
    print(f"Direct  : x={x_d:.6g}, y={y_d:.6g}, z={z_d:.6g}")
    print(f"Benders : x={x_b:.6g}, y={y_b:.6g}, z={z_b:.6g}, iters={it}")
    if expected:
        ok = (abs(x_d - expected['x']) < 1e-6
              and abs(y_d - expected['y']) < 1e-6
              and abs(z_d - expected['obj']) < 1e-6)
        print(f"Matches expected? {'YES' if ok else 'NO'}")

if __name__ == "__main__":
    run_instance()
