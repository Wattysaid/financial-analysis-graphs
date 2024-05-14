import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {'Date': pd.date_range(start='1/1/2023', periods=100),
        'Stock Price': np.random.normal(loc=100, scale=10, size=100)}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Stock Price'], label='Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Over Time')
plt.legend()
plt.grid(True)
plt.show()
