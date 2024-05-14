from statsmodels.tsa.seasonal import seasonal_decompose

# Sample data
data = {'Date': pd.date_range(start='1/1/2020', periods=100, freq='D'),
        'Value': np.random.normal(loc=0, scale=1, size=100).cumsum()}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Decomposition
decomposition = seasonal_decompose(df['Value'], model='additive')
decomposition.plot()
plt.show()
