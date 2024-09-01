import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

df = pd.read_csv('/AMZN_2020_to_2022.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df.asfreq('B')
ts_data = df['Close']


p, d, q = 2, 0, 2

model = ARIMA(ts_data, order=(p, d, q))
model_fit = model.fit()

print(model_fit.summary())


df23 = pd.read_csv('/AMZN_2023.csv')
df23_dates = pd.to_datetime(df23['Date'])

start_date = df23_dates.min()
end_date = df23_dates.max()

predictions = model_fit.get_prediction(start=start_date, end=end_date)
predictions_df = predictions.summary_frame()

actual_values = df23['Close']


plt.figure(figsize=(12, 6))
plt.plot(ts_data, color='green', label='Original Data')
plt.plot(predictions_df.index, predictions_df['mean'], color='orange', label='Predictions')
plt.fill_between(predictions_df.index, predictions_df['mean_ci_lower'], predictions_df['mean_ci_upper'], color='lightgray', label='95% CI', alpha=0.7)
plt.plot(df23_dates, actual_values, color='darkblue', label='Actual Values')

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Time Series Prediction for AMZN with Confidence Intervals (95%)')
plt.legend()
plt.show()


def calculate_confidence_interval(mean_forecast, se_forecast, confidence_level):
    critical_value = stats.norm.ppf(1 - (1 - confidence_level) / 2)
    ci_lower = mean_forecast - critical_value * se_forecast
    ci_upper = mean_forecast + critical_value * se_forecast
    return ci_lower, ci_upper

mean_forecast = predictions_df['mean']
se_forecast = predictions_df['mean_se']

ci_75_lower, ci_70_upper = calculate_confidence_interval(mean_forecast, se_forecast, 0.75)
ci_50_lower, ci_50_upper = calculate_confidence_interval(mean_forecast, se_forecast, 0.50)


plt.figure(figsize=(12, 6))


plt.fill_between(predictions_df.index, ci_75_lower, ci_70_upper, color='skyblue', alpha=0.7, label='75% CI')
plt.fill_between(predictions_df.index, ci_50_lower, ci_50_upper, color='blue', alpha=0.5, label='50% CI')
plt.plot(ts_data['2022-01-01':], color='green', label='Original Data')
plt.plot(predictions_df.index, predictions_df['mean'], color='darkred', linewidth=2, label='Predictions')
plt.fill_between(predictions_df.index, predictions_df['mean_ci_lower'], predictions_df['mean_ci_upper'], color='lightgray', label='95% CI', alpha=0.7)
plt.plot(df23_dates, actual_values, color='darkblue', label='Actual Values')

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Time Series Prediction for AMZN with Confidence Intervals - Starting from 2022')
plt.legend()
plt.show()


df23_dates = pd.to_datetime(df23_dates)
predictions_df.index = pd.to_datetime(predictions_df.index)
actual_values.index = pd.to_datetime(df23_dates)

dates_with_no_actual = predictions_df.index.difference(actual_values.index)
predictions_df_cleaned = predictions_df.drop(dates_with_no_actual)
actual_values_aligned = actual_values.loc[predictions_df_cleaned.index]

rmse = mean_squared_error(actual_values_aligned, predictions_df_cleaned['mean'], squared=False)
print("RMSE:", rmse)
