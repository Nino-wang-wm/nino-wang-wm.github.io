
# Basic Parameters
N_ATOMS = 5          # Number of geographical atoms
CAPACITY = "inf"    # "zero" or "inf"
MAX_ITERATIONS = 10  # Maximum iterations for steady state calculation

# Optional Parameters - set to None to use random initialization
ARRIVAL_RATES = [0.2, 0.2, 0.2, 0.2, 0.2]  # Must sum to 1
TRAVEL_TIMES = None  # Will be randomly initialized if None
DISPATCH_PREFERENCES = None  # Will be randomly initialized if None

# Visualization Parameters
PLOT_FIGSIZE = (10, 6)
HEATMAP_CMAP = 'viridis'
SAVE_PLOTS = True
PLOT_DIR = 'plots/'