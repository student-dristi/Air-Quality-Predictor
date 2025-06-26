import numpy as np
import pandas as pd

np.random.seed(42)

n=500

data = {
    'PM2.5': np.random.uniform(10, 250, n),
    'NO2': np.random.uniform(5, 100, n),
    'CO': np.random.uniform(0.2, 5, n),
    'SO2': np.random.uniform(2, 60, n),
    'AQI': np.random.uniform(30, 300, n)
}

df=pd.DataFrame(data)
'''make dataframe'''


df['CO2'] = (
    df['PM2.5'] * 1.2 +
    df['NO2'] * 0.9 +
    df['CO'] * 10 +
    df['SO2'] * 0.5 +
    np.random.normal(0, 20, n)
).clip(lower=300, upper=1000)

df['AQI_Status'] = df['AQI'].apply(lambda x: 1 if x > 100 else 0)

print(df.head())
df.to_csv("simulated_air_quality.csv", index=False)
