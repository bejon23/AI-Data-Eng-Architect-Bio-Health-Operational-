# =======================
# PROJECT 5: Clinical Trial Outcome Prediction
# =======================
!pip install lifelines scikit-learn plotly pandas numpy -q

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

# ============================================
# Cell 1: Clinical Trial Data
# ============================================
print("=== Cell 1: Clinical Trial Data ===")

np.random.seed(42)
n_trials = 500

trials_data = {
    'trial_id': [f'NCT{i:08d}' for i in range(n_trials)],
    'phase': np.random.choice(['Phase I', 'Phase II', 'Phase III'], n_trials, p=[0.3, 0.4, 0.3]),
    'enrollment': np.random.randint(20, 2000, n_trials),
    'duration_months': np.random.randint(6, 60, n_trials),
    'therapeutic_area': np.random.choice(['Oncology', 'Cardiology', 'Neurology', 'Immunology'], n_trials),
    'success': np.random.choice([0, 1], n_trials, p=[0.4, 0.6])
}
trials_df = pd.DataFrame(trials_data)
print(f"Loaded {len(trials_df)} clinical trials")
print(trials_df.head())

# ============================================
# Cell 2: LLM Summarization (Mock)
# ============================================
print("\n=== Cell 2: LLM Summarization ===")

def summarize_trial(trial_data):
    """Summarize trial with LLM (mock)"""
    return f"{trial_data['phase']} trial in {trial_data['therapeutic_area']} with {trial_data['enrollment']} patients"

# Sample summary
sample = trials_df.iloc[0].to_dict()
summary = summarize_trial(sample)
print(f"Sample trial summary: {summary}")

# ============================================
# Cell 3: Meta-Analysis
# ============================================
print("\n=== Cell 3: Meta-Analysis ===")

# Success rates by phase
phase_stats = trials_df.groupby('phase')['success'].agg(['mean', 'count']).reset_index()
phase_stats.columns = ['Phase', 'Success_Rate', 'N_Trials']
print(phase_stats)

# Success rates by therapeutic area
area_stats = trials_df.groupby('therapeutic_area')['success'].agg(['mean', 'count']).reset_index()
area_stats.columns = ['Area', 'Success_Rate', 'N_Trials']
print(area_stats)

# ============================================
# Cell 4: Survival Analysis
# ============================================
print("\n=== Cell 4: Survival Analysis ===")

from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

kmf = KaplanMeierFitter()
kmf.fit(durations=trials_df['duration_months'], event_observed=trials_df['success'])

plt.figure(figsize=(10, 6))
kmf.plot_survival_function()
plt.title('Kaplan-Meier Survival Curve (Trial Success)')
plt.xlabel('Duration (months)')
plt.ylabel('Success Probability')
plt.grid(True, alpha=0.3)
plt.show()

print(f"Median success time: {kmf.median_survival_time_:.1f} months")

# ============================================
# Cell 5: Success Prediction Model
# ============================================
print("\n=== Cell 5: Success Prediction ===")

# Features
trials_df['phase_num'] = trials_df['phase'].map({'Phase I': 1, 'Phase II': 2, 'Phase III': 3})
area_dummies = pd.get_dummies(trials_df['therapeutic_area'], prefix='area')

X = pd.concat([trials_df[['enrollment', 'duration_months', 'phase_num']], area_dummies], axis=1)
y = trials_df['success']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.3f}")

# Feature importance
importances = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nTop 5 Important Features:")
print(importances.head())

# ============================================
# Cell 6: Dashboard Visualization
# ============================================
print("\n=== Cell 6: Dashboard ===")

fig = go.Figure()
for phase in ['Phase I', 'Phase II', 'Phase III']:
    phase_data = trials_df[trials_df['phase'] == phase]
    fig.add_trace(go.Box(y=phase_data['success'], name=phase))

fig.update_layout(
    title="Clinical Trial Success by Phase",
    yaxis_title="Success Rate",
    height=500
)
fig.show()

# Summary
print("\n" + "="*50)
print("FINAL SUMMARY")
print("="*50)
print(f"Total trials analyzed: {len(trials_df)}")
print(f"Overall success rate: {trials_df['success'].mean():.1%}")
print(f"Model accuracy: {accuracy_score(y_test, y_pred):.3f}")
print("="*50)
