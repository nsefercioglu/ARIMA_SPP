import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('/AMZN.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
ts_data = df['Close']


decomposition = seasonal_decompose(ts_data, model='additive', period=365)

fig, axes = plt.subplots(4, 1, figsize=(10, 8), dpi=300)

axes[0].plot(ts_data, label='Original', color='green', linewidth=1)
axes[0].set_title('Original Time Series')
axes[0].legend()

axes[1].plot(decomposition.trend, label='Trend', color='green', linewidth=1)
axes[1].set_title('Trend Component')
axes[1].legend()

axes[2].plot(decomposition.seasonal, label='Seasonal', color='green', linewidth=1)
axes[2].set_title('Seasonal')
axes[2].legend()

axes[3].plot(decomposition.resid, label='Residuals', color='green', linewidth=1)
axes[3].set_title('Residuals')
axes[3].legend()

plt.tight_layout()
plt.show()