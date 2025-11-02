import numpy as np
from hypercubeq import HypercubeQ
from visualization import plot_dispatch_heatmap, plot_travel_times, plot_state_probabilities
import config

def run_hypercube_model(params, label):
    """
    Run the hypercube model with given parameters and generate labeled visualizations
    """
    # Initialize model
    model = HypercubeQ(
        n_atoms=params['n_atoms'],
        Lam=params['arrival_rates'],
        T=params['travel_times'],
        P=params['dispatch_preferences'],
        cap=params['capacity'],
        max_iter=params['max_iterations']
    )
    
    # Generate visualizations with scenario-specific labels
    plot_dispatch_heatmap(model.Rho_1, f"Dispatch Fractions - {label}")
    plot_travel_times(model.Tu, f"Average Travel Times per Unit - {label}")
    plot_state_probabilities(model.Pi, f"State Probabilities - {label}")
    
    return model

def main():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Load parameters from config
    model_params = {
        'n_atoms': config.N_ATOMS,
        'arrival_rates': config.ARRIVAL_RATES if hasattr(config, 'ARRIVAL_RATES') else None,
        'travel_times': config.TRAVEL_TIMES if hasattr(config, 'TRAVEL_TIMES') else None,
        'dispatch_preferences': config.DISPATCH_PREFERENCES if hasattr(config, 'DISPATCH_PREFERENCES') else None,
        'max_iterations': config.MAX_ITERATIONS
    }
    
    # Run model for zero-line capacity
    print("Running Zero-Line Capacity Model...")
    model_zero = run_hypercube_model({**model_params, 'capacity': 'zero'}, label="Zero-Line Capacity")
    
    # Run model for infinite-line capacity
    print("Running Infinite-Line Capacity Model...")
    model_inf = run_hypercube_model({**model_params, 'capacity': 'inf'}, label="Infinite-Line Capacity")
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("Zero-Line Capacity Model:")
    print(f"Average Travel Time: {model_zero.Tu.mean():.2f}")
    print(f"State Probability Sum: {model_zero.Pi.sum():.4f}")
    
    print("\nInfinite-Line Capacity Model:")
    print(f"Average Travel Time: {model_inf.Tu.mean():.2f}")
    print(f"State Probability Sum: {model_inf.Pi.sum() + model_inf.Pi_Q.sum():.4f}")

if __name__ == "__main__":
    main()
