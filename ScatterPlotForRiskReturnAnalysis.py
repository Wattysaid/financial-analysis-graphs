# Sample data
data = {'Risk': np.random.normal(loc=0.1, scale=0.05, size=50),
        'Return': np.random.normal(loc=0.15, scale=0.05, size=50)}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Risk', y='Return', data=df)
plt.xlabel('Risk')
plt.ylabel('Return')
plt.title('Risk-Return Analysis')
plt.show()
