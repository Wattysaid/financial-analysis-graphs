import seaborn as sns

# Sample data
returns = np.random.normal(0, 0.1, 1000)

# Plot
plt.figure(figsize=(10, 6))
sns.histplot(returns, bins=30, kde=True)
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.title('Return Distribution')
plt.show()
