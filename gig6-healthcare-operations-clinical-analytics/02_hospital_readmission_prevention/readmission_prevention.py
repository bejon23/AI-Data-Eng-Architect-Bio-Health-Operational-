# PROJECT 2: Readmission Prevention
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

np.random.seed(42)
n = 1000

df = pd.DataFrame({
    'age': np.random.randint(18, 90, n),
    'prior_admissions': np.random.randint(0, 10, n),
    'hba1c_level': np.random.uniform(4.0, 12.0, n),
    'medication_adherence': np.random.uniform(0.1, 1.0, n)
})

readmission_prob = (0.3*(df['age']/100) + 0.4*(df['prior_admissions']/10) +
                    0.2*((df['hba1c_level']-4)/8) + 0.1*(1-df['medication_adherence']))
df['readmitted'] = (readmission_prob > 0.5).astype(int)

X = df[['age', 'prior_admissions', 'hba1c_level', 'medication_adherence']]
y = df['readmitted']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBClassifier(n_estimators=100, learning_rate=0.05, max_depth=6, random_state=42)
model.fit(X_train, y_train)

y_pred_proba = model.predict_proba(X_test)[:, 1]
print(f"AUC: {roc_auc_score(y_test, y_pred_proba):.3f}")

def get_action(score):
    if score >= 0.8: return "URGENT: Immediate follow-up"
    elif score >= 0.6: return "CAUTION: Follow-up within 7 days"
    elif score >= 0.4: return "MONITOR: Check-up within 14 days"
    else: return "LOW RISK: Standard protocol"

for i, s in enumerate(y_pred_proba[:10]):
    print(f"Patient {i+1}: {s:.2f} -> {get_action(s)}")
