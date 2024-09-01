import pandas as pd

df = pd.read_csv('/AMZN.csv')
df.drop(columns=['Adj Close'], axis=1, inplace=True)

df_2023 = df[df['Date'].str.startswith('2023')]
new_file_path = '/AMZN_2023.csv'
df_2023.to_csv(new_file_path, index=False, float_format='%.6f')


df_excluding_2023 = df[~df['Date'].str.startswith('2023')]
updated_file_path = '/AMZN_Until_23.csv'
df_excluding_2023.to_csv(updated_file_path, index=False, float_format='%.6f')

df_2015_to_2022 = df[(df['Date'] >= '2015-01-01') & (df['Date'] < '2023-01-01')]
updated_file_path = '/AMZN_2015_to_2022.csv'
df_2015_to_2022.to_csv(updated_file_path, index=False, float_format='%.6f')

df_2018_to_2022 = df[(df['Date'] >= '2018-01-01') & (df['Date'] < '2023-01-01')]
updated_file_path = '/AMZN_2018_to_2022.csv'
df_2018_to_2022.to_csv(updated_file_path, index=False, float_format='%.6f')

df_2012_to_2022 = df[(df['Date'] >= '2012-01-01') & (df['Date'] < '2023-01-01')]
updated_file_path = '/AMZN_2012_to_2022.csv'
df_2012_to_2022.to_csv(updated_file_path, index=False, float_format='%.6f')

df_2016_to_2022 = df[(df['Date'] >= '2016-01-01') & (df['Date'] < '2023-01-01')]
updated_file_path = '/AMZN_2016_to_2022.csv'
df_2016_to_2022.to_csv(updated_file_path, index=False, float_format='%.6f')

df_2020_to_2022 = df[(df['Date'] >= '2020-01-01') & (df['Date'] < '2023-01-01')]
updated_file_path = '/AMZN_2020_to_2022.csv'
df_2020_to_2022.to_csv(updated_file_path, index=False, float_format='%.6f')