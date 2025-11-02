import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import config

def ensure_plot_dir():
    """Create plot directory if it doesn't exist"""
    if config.SAVE_PLOTS and not os.path.exists(config.PLOT_DIR):
        os.makedirs(config.PLOT_DIR)

def plot_dispatch_heatmap(data, title):
    """Plot heatmap of dispatch fractions"""
    plt.figure(figsize=config.PLOT_FIGSIZE)
    sns.heatmap(data, 
                cmap=config.HEATMAP_CMAP,
                annot=True, 
                fmt='.2f')
    plt.title(title)
    plt.xlabel('Geographical Atoms')
    plt.ylabel('Response Units')
    
    if config.SAVE_PLOTS:
        ensure_plot_dir()
        filename = title.lower().replace(" ", "_").replace("-", "_") + ".png"
        plt.savefig(os.path.join(config.PLOT_DIR, filename))
    plt.close()

def plot_travel_times(data, title):
    """Plot bar chart of average travel times"""
    plt.figure(figsize=config.PLOT_FIGSIZE)
    plt.bar(range(len(data)), data)
    plt.title(title)
    plt.xlabel('Response Unit')
    plt.ylabel('Average Travel Time')
    plt.xticks(range(len(data)))
    
    if config.SAVE_PLOTS:
        ensure_plot_dir()
        filename = title.lower().replace(" ", "_").replace("-", "_") + ".png"
        plt.savefig(os.path.join(config.PLOT_DIR, filename))
    plt.close()

def plot_state_probabilities(data, title):
    """Plot state probabilities"""
    plt.figure(figsize=config.PLOT_FIGSIZE)
    plt.plot(range(len(data)), data, 'bo-')
    plt.title(title)
    plt.xlabel('State Index')
    plt.ylabel('Probability')
    plt.grid(True)
    
    if config.SAVE_PLOTS:
        ensure_plot_dir()
        filename = title.lower().replace(" ", "_").replace("-", "_") + ".png"
        plt.savefig(os.path.join(config.PLOT_DIR, filename))
    plt.close()
