# Column Generation for "LP with Complicating Constraints"
from gurobipy import Model, GRB, quicksum

# ----------------------------
# Problem data (4 blocks, each 2 vars) & 3 complicating constraints
# ----------------------------
# x = (x1..x8)
c = [3.0, 5.0, 4.0, 2.0, 1.0, 6.0, 2.5, 3.5]   # cost
n = len(c)

# blocks: (x1,x2), (x3,x4), (x5,x6), (x7,x8)
blocks = [(0,2), (2,4), (4,6), (6,8)]
f = [5.0, 6.0, 4.0, 7.0]                              # per-block equality sum
ub = [5.0, 5.0, 6.0, 6.0, 4.0, 4.0, 7.0, 7.0]   # upper bounds

# Ax = b  (m = 3)
A = [
    [2,1,   1,3,   2,1,   1,2],   # row1
    [1,2,   3,1,   1,2,   2,1],   # row2
    [0,1,   2,0,   1,1,   3,2],   # row3
]

b = [40.0, 32.0, 27.0]
m = len(A)

# ----------------------------
# Helpers
# ----------------------------
def solve_block_modified_cost(block_id, cbar):
    """ min sum cbar_j x_j  s.t. sum x_j = f[k], 0<=x_j<=ub_j
    """
    i0, i1 = blocks[block_id]
    M = Model()
    M.Params.OutputFlag = 0
    x = M.addVars(range(i0, i1), lb=0.0, ub=[ub[j] for j in range(i0, i1)],
                  name=f"x_blk{block_id}")
    M.addConstr(quicksum(x[j] for j in range(i0, i1)) == f[block_id])
    M.setObjective(quicksum(cbar[j]*x[j] for j in range(i0, i1)), GRB.MINIMIZE)
    M.optimize()
    x_blk = [0.0]*n
    for j in range(i0, i1):
        x_blk[j] = x[j].X
    return x_blk

def eval_obj(x):
    return sum(c[j]*x[j] for j in range(n))

def eval_r(x):
    return [sum(A[i][j]*x[j] for j in range(n)) for i in range(m)]

# ----------------------------
# Initialization: build p(ν) initial columns by "arbitrary costs" ĉ^(ℓ)
# ----------------------------
init_costs = [
    [-1, -1,   1,  2,   3,  4,   3,  4],  
    [ 2,  1,  -1, -1,   3,  4,   3,  4],  
    [ 3,  3,   2,  3,  -1, -1,   2,  3], 
]

X_pool, Z_pool, R_pool = [], [], []
for hat_c in init_costs:
    x_total = [0.0]*n
    for k in range(len(blocks)):
        x_blk = solve_block_modified_cost(k, hat_c)
        for j in range(n):
            x_total[j] += x_blk[j]
    X_pool.append(x_total)
    Z_pool.append(eval_obj(x_total))
    R_pool.append(eval_r(x_total))

print(f"Initialized with {len(X_pool)} columns.")
print(f"X_pool = {X_pool}")
print(f"Z_pool = {Z_pool}")
print(f"R_pool = {R_pool}")

# ----------------------------
# Always-feasible Master
#   min  Σ_s z^(s) u_s + M * Σ_i (δ_i^+ + δ_i^-)
#   s.t. Σ_s r_i^(s) u_s + δ_i^+ - δ_i^- = b_i
#        Σ_s u_s = 1,  u_s>=0, δ>=0
# return: u*, λ, σ, obj, (δ+, δ-)
# ----------------------------
def solve_master(Z_pool, R_pool, b, BIGM=1e6):
    P = len(Z_pool)
    M = Model()
    M.Params.OutputFlag = 0
    u = M.addVars(P, lb=0.0, name="u")
    dpos = M.addVars(m, lb=0.0, name="dpos")
    dneg = M.addVars(m, lb=0.0, name="dneg")

    M.setObjective(quicksum(Z_pool[s]*u[s] for s in range(P))
                   + BIGM*quicksum(dpos[i]+dneg[i] for i in range(m)), GRB.MINIMIZE)

    cc = []
    for i in range(m):
        cons = M.addConstr(quicksum(R_pool[s][i]*u[s] for s in range(P))
                           + dpos[i] - dneg[i] == b[i], name=f"Aeq[{i}]")
        cc.append(cons)

    conv = M.addConstr(quicksum(u[s] for s in range(P)) == 1.0, name="convexity")
    M.optimize()

    if M.Status != GRB.OPTIMAL:
        raise RuntimeError(f"Master not optimal, status={M.Status}")

    u_star = [u[s].X for s in range(P)]
    lam = [cc[i].Pi for i in range(m)]
    sig = conv.Pi
    obj = M.ObjVal
    deltas = ([dpos[i].X for i in range(m)], [dneg[i].X for i in range(m)])
    return u_star, lam, sig, obj, deltas

# ----------------------------
# Relaxed:  c̄ = c - A^T λ;  solve each block; compute v,z,r
# ----------------------------
def solve_relaxed(lam):
    cbar = [c[j] - sum(lam[i]*A[i][j] for i in range(m)) for j in range(n)]
    x_total = [0.0]*n
    for k in range(len(blocks)):
        x_blk = solve_block_modified_cost(k, cbar)
        for j in range(n):
            x_total[j] += x_blk[j]
    v = sum(cbar[j]*x_total[j] for j in range(n))
    z = eval_obj(x_total)
    r = eval_r(x_total)
    return x_total, v, z, r, cbar

def solve_full_lp():
    """
    Solve the original LP in one shot:
      min  c^T x
      s.t.  for each block k: sum_{j in block k} x_j = f[k]
            0 <= x_j <= ub_j
            A x = b
    Returns: (x_full, z_full)
    """
    # Uses global data: c, A, b, blocks, f, ub, n, m
    M = Model("full_lp")
    M.Params.OutputFlag = 0

    x = M.addVars(range(n), lb=0.0, ub=ub, name="x")

    for k, (i0, i1) in enumerate(blocks):
        M.addConstr(quicksum(x[j] for j in range(i0, i1)) == f[k], name=f"blk[{k}]")

    for i in range(m):
        M.addConstr(quicksum(A[i][j] * x[j] for j in range(n)) == b[i], name=f"Aeq[{i}]")

    M.setObjective(quicksum(c[j] * x[j] for j in range(n)), GRB.MINIMIZE)

    M.optimize()
    if M.Status != GRB.OPTIMAL:
        raise RuntimeError(f"Full LP not optimal, status={M.Status}")

    x_full = [x[j].X for j in range(n)]
    z_full = sum(c[j] * x_full[j] for j in range(n))
    return x_full, z_full


def main():
    it = 0
    while True:
        it += 1
        u_star, lam, sig, obj, deltas = solve_master(Z_pool, R_pool, b)
        x_new, v, z_new, r_new, cbar = solve_relaxed(lam)
        dpos, dneg = deltas
        max_dev = max([0.0] + dpos + dneg)

        print(f"\n=== Iteration {it} ===")
        print(f"Master obj: {obj:.6f}")
        print(f"Duals λ: {', '.join(f'{x:.6f}' for x in lam)}   σ: {sig:.6f}")
        print(f"Relaxed v: {v:.6f}   σ: {sig:.6f}   max|δ|: {max_dev:.2e}")

        if (v >= sig - 1e-9) and (max_dev <= 1e-7):
            x_star = [0.0]*n
            for s, us in enumerate(u_star):
                for j in range(n):
                    x_star[j] += us * X_pool[s][j]
            z_star = eval_obj(x_star)
            r_star = eval_r(x_star)
            print("\nConverged: v >= σ and δ≈0.")
            print("x* =", [round(val,6) for val in x_star])
            print("z* =", round(z_star,6))
            print("A x* =", [round(val,6) for val in r_star], " (== b)")
            break

        X_pool.append(x_new)
        Z_pool.append(z_new)
        R_pool.append(r_new)
        print(">> Added new column and continue...")



    # Compare with full LP (direct solve)
    x_full, z_full = solve_full_lp()
    print("\n--- Direct (one-shot) LP solve ---")
    print("x_full =", [round(v, 6) for v in x_full])
    print("z_full =", round(z_full, 6))

    # Optional: check difference
    diff_x = [abs(x_full[j] - x_star[j]) for j in range(n)]
    print("max |x_full - x*| =", round(max(diff_x), 8))
    print("diff in obj (z_full - z*) =", round(z_full - z_star, 8))

if __name__ == "__main__":
    main()

