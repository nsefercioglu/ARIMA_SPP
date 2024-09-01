import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/AMZN.csv')

df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(15, 7))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')

plt.title('Amazon Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()

plt.grid(True)
plt.show()

plt.figure(figsize=(15, 7))
plt.plot(df['Date'], df['Volume'], label='Volume', color='green')
plt.title('Amazon Stock Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.show()