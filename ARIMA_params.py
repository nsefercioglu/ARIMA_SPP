import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pmdarima.arima import auto_arima

df = pd.read_csv('/AMZN_2020_to_2022.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
ts_data = df['Close']

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

plot_acf(ts_data, ax=axes[0], lags=40, title='Autocorrelation Function (ACF)')
plot_pacf(ts_data, ax=axes[1], lags=40, title='Partial Autocorrelation Function (PACF)')

plt.tight_layout()
plt.show()

model = auto_arima(ts_data, seasonal=False, trace=True,
                      error_action='ignore', suppress_warnings=True)

print(model.summary())