import plotly.graph_objects as go

# Sample data
data = {'Date': pd.date_range(start='1/1/2023', periods=100),
        'Open': np.random.normal(loc=100, scale=10, size=100),
        'High': np.random.normal(loc=110, scale=10, size=100),
        'Low': np.random.normal(loc=90, scale=10, size=100),
        'Close': np.random.normal(loc=100, scale=10, size=100)}
df = pd.DataFrame(data)

# Plot
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])
fig.update_layout(title='Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price')
fig.show()
