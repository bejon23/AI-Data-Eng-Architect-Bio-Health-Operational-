# PROJECT 4: Equipment Predictive Maintenance
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

np.random.seed(42)
n = 500

sensor_data = pd.DataFrame({
    'timestamp': pd.date_range('2026-01-01', periods=n, freq='H'),
    'temp': np.random.normal(37, 2, n),
    'vibration': np.random.normal(5, 1, n),
    'pressure': np.random.normal(100, 5, n)
})

# Inject anomalies
anomaly_idx = np.random.choice(n, 20, replace=False)
sensor_data.loc[anomaly_idx, 'temp'] += np.random.normal(10, 3, 20)
sensor_data.loc[anomaly_idx, 'vibration'] += np.random.normal(8, 2, 20)

model = IsolationForest(contamination=0.04, random_state=42)
sensor_data['anomaly'] = model.fit_predict(sensor_data[['temp', 'vibration', 'pressure']])

print(f"Anomalies detected: {(sensor_data['anomaly']==-1).sum()}")
print(sensor_data.head())
