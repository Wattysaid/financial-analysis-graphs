import numpy as np

# Sample data
data = np.random.rand(10, 10)
correlation_matrix = np.corrcoef(data)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
