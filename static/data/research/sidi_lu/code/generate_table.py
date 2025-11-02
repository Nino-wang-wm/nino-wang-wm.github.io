import pandas as pd

original_avg_result = pd.read_csv('100_rounds_original_result.csv')
enhanced_avg_result = pd.read_csv('100_rounds_enhanced_result.csv')

original_best_distance = original_avg_result['best'].min()
enhanced_best_distance = enhanced_avg_result['best'].min()
original_avg_distance = original_avg_result['avg'].mean()
enhanced_avg_distance = enhanced_avg_result['avg'].mean()

comparison_table = pd.DataFrame({
    'Algorithm': ['Original', 'Enhanced Dynamic Pheromone'],
    'Best Distance': [original_best_distance, enhanced_best_distance],
    'Average Distance': [original_avg_distance, enhanced_avg_distance]
})

print("Comparison Table:")
print(comparison_table)

original_stats = pd.DataFrame({
    'Metric': ['Best Distance', 'Average Distance'],
    'Value': [original_best_distance, original_avg_distance]
})

print("\nOriginal Algorithm Statistics:")
print(original_stats)

enhanced_stats = pd.DataFrame({
    'Metric': ['Best Distance', 'Average Distance'],
    'Value': [enhanced_best_distance, enhanced_avg_distance]
})

print("\nEnhanced Dynamic Pheromone Algorithm Statistics:")
print(enhanced_stats)