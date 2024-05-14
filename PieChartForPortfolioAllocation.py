# Sample data
data = {'Asset': ['Stocks', 'Bonds', 'Real Estate', 'Cash'],
        'Allocation': [50, 20, 20, 10]}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(8, 8))
plt.pie(df['Allocation'], labels=df['Asset'], autopct='%1.1f%%', startangle=140)
plt.title('Portfolio Allocation')
plt.show()
