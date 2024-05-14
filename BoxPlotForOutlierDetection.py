# Sample data
data = {'Stock': np.random.choice(['A', 'B', 'C', 'D'], size=100),
        'Return': np.random.normal(loc=0, scale=1, size=100)}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Stock', y='Return', data=df)
plt.xlabel('Stock')
plt.ylabel('Return')
plt.title('Return Distribution by Stock')
plt.show()
