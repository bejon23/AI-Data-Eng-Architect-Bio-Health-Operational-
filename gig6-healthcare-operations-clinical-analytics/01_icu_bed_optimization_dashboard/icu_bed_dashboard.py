# PROJECT 1: ICU Bed Optimization
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.ensemble import RandomForestRegressor

np.random.seed(42)
days = 365

data = {
    'Date': pd.date_range('2025-01-01', periods=days),
    'ICU_Beds_Occupied': np.random.poisson(45, days).clip(30, 60),
    'ICU_Capacity': 80,
    'Emergency_Admissions': np.random.poisson(25, days).clip(15, 40),
    'Staff_Available': np.random.normal(45, 5, days).clip(35, 55).astype(int),
    'Readmission_Rate': np.random.uniform(0.08, 0.18, days)
}

df_ops = pd.DataFrame(data)
df_ops['ICU_Utilization'] = (df_ops['ICU_Beds_Occupied'] / df_ops['ICU_Capacity']) * 100
df_ops['Day_of_Week'] = df_ops['Date'].dt.day_name()

X = np.array(range(len(df_ops))).reshape(-1, 1)
y = df_ops['ICU_Beds_Occupied'].values

model = RandomForestRegressor(n_estimators=50, random_state=42)
model.fit(X, y)

future_days = np.array(range(len(df_ops), len(df_ops) + 7)).reshape(-1, 1)
predicted_beds = model.predict(future_days).astype(int)

print("Next 7 Days Forecast:", predicted_beds)
print(f"Model R2: {model.score(X, y):.3f}")
