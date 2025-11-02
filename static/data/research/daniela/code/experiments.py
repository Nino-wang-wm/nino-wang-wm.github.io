import numpy as np
from hypercubeq import HypercubeQ
import config

def run_experiment(n_atoms, arrival_rates, travel_times, dispatch_preferences, label):
    print(f"\n--- Experiment: {label} ---")
    
    # Zero-line capacity model
    model_zero = HypercubeQ(n_atoms, Lam=arrival_rates, T=travel_times, P=dispatch_preferences, cap="zero")
    
    # Infinite-line capacity model
    model_inf = HypercubeQ(n_atoms, Lam=arrival_rates, T=travel_times, P=dispatch_preferences, cap="inf")
    
    # Print results
    print("Zero-line capacity results:")
    print(f"Average Travel Time: {model_zero.Tu.mean():.4f}")
    print(f"State Probability Sum: {model_zero.Pi.sum():.4f}")
    print(f"Dispatch Fraction Range: {model_zero.Rho_1.min():.4f} - {model_zero.Rho_1.max():.4f}")
    
    print("\nInfinite-line capacity results:")
    print(f"Average Travel Time: {model_inf.Tu.mean():.4f}")
    print(f"State Probability Sum: {model_inf.Pi.sum() + model_inf.Pi_Q.sum():.4f}")
    print(f"Dispatch Fraction Range: {model_inf.Rho_1.min():.4f} - {model_inf.Rho_1.max():.4f}")

def main():
    np.random.seed(42)
    
    # Experiment 1: Varying number of atoms
    for n_atoms in [3, 5, 7]:
        arrival_rates = np.ones(n_atoms) / n_atoms
        travel_times = np.random.rand(n_atoms, n_atoms)
        dispatch_preferences = np.random.rand(n_atoms, n_atoms).argsort()
        run_experiment(n_atoms, arrival_rates, travel_times, dispatch_preferences, f"N_ATOMS = {n_atoms}")
    
    # Experiment 2: Different arrival rate distributions
    n_atoms = 5
    arrival_distributions = [
        np.ones(n_atoms) / n_atoms,  # Uniform
        np.array([0.4, 0.3, 0.1, 0.1, 0.1]),  # Skewed
        np.array([0.5, 0.2, 0.2, 0.05, 0.05])  # Highly skewed
    ]
    for i, arr_dist in enumerate(arrival_distributions):
        travel_times = np.random.rand(n_atoms, n_atoms)
        dispatch_preferences = np.random.rand(n_atoms, n_atoms).argsort()
        run_experiment(n_atoms, arr_dist, travel_times, dispatch_preferences, f"Arrival Distribution {i+1}")
    
    # Experiment 3: Changing travel time matrices
    travel_time_scenarios = [
        np.random.rand(n_atoms, n_atoms),  # Random
        np.random.rand(n_atoms, n_atoms) * 2,  # Increased travel times
        np.triu(np.random.rand(n_atoms, n_atoms))  # Upper triangular
    ]
    for i, travel_times in enumerate(travel_time_scenarios):
        arrival_rates = np.ones(n_atoms) / n_atoms
        dispatch_preferences = np.random.rand(n_atoms, n_atoms).argsort()
        run_experiment(n_atoms, arrival_rates, travel_times, dispatch_preferences, f"Travel Time Scenario {i+1}")
    
    # Experiment 4: Modifying dispatch preferences
    dispatch_preference_scenarios = [
        np.random.rand(n_atoms, n_atoms).argsort(),  # Random
        np.tile(np.arange(n_atoms), (n_atoms, 1)),  # Fixed preference
        np.array([np.roll(np.arange(n_atoms), i) for i in range(n_atoms)])  # Cyclic preference
    ]
    for i, dispatch_preferences in enumerate(dispatch_preference_scenarios):
        arrival_rates = np.ones(n_atoms) / n_atoms
        travel_times = np.random.rand(n_atoms, n_atoms)
        run_experiment(n_atoms, arrival_rates, travel_times, dispatch_preferences, f"Dispatch Preference Scenario {i+1}")

if __name__ == "__main__":
    main()