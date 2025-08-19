# --------- Churn Prediction + Forecasting ---------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from prophet import Prophet
import joblib

# =============================
# PART 1 - CUSTOMER CHURN MODEL
# =============================

print("----- Churn Prediction -----")

# Step 1: Simulate example customer dataset
np.random.seed(42)
n = 1000
customers = pd.DataFrame({
    "CustomerID": range(1, n+1),
    "Age": np.random.randint(18, 70, n),
    "Balance": np.random.uniform(100, 10000, n),
    "TransactionsLastMonth": np.random.randint(1, 200, n),
    "CreditScore": np.random.randint(300, 850, n),
    "TenureYears": np.random.randint(0, 20, n),
    "IsActive": np.random.choice([0,1], size=n),
    "Churned": np.random.choice([0,1], size=n, p=[0.8,0.2])  # ~20% churn
})

# Step 2: Features & labels
X = customers.drop(columns=["CustomerID", "Churned"])
y = customers["Churned"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 3: Train model
churn_model = RandomForestClassifier(n_estimators=200, random_state=42)
churn_model.fit(X_train, y_train)

# Step 4: Evaluate
y_pred = churn_model.predict(X_test)
y_prob = churn_model.predict_proba(X_test)[:,1]
print("Classification Report:\n", classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

# Step 5: Save predictions
customers["Churn_Probability"] = churn_model.predict_proba(X_scaled)[:,1]
customers.to_excel("Churn_Predictions.xlsx", index=False)
print("✅ Churn predictions saved to Churn_Predictions.xlsx")

# Step 6: Save model
joblib.dump((churn_model, scaler), "churn_model.pkl")
print("✅ Churn model saved as churn_model.pkl")

# --------- Step 7: Export Feature Importances ---------
feature_importances = pd.DataFrame({
    "Feature": X.columns,   # original feature names
    "Importance": churn_model.feature_importances_
}).sort_values(by="Importance", ascending=False)

feature_importances.to_excel("Feature_Importance.xlsx", index=False)
print("✅ Feature importances saved to Feature_Importance.xlsx")
# =============================
# PART 2 - TRANSACTION FORECAST
# =============================

print("\n----- Transaction Forecasting -----")
# Step 1: Simulate historical monthly transactions
df_txn = pd.DataFrame({
    "ds": pd.date_range("2020-01-01", periods=36, freq="M"),
    "y": np.random.randint(1000, 5000, 36)
})

# Step 2: Train Prophet model
forecast_model = Prophet()
forecast_model.fit(df_txn)

# Step 3: Forecast next 12 months
future = forecast_model.make_future_dataframe(periods=12, freq="M")
forecast = forecast_model.predict(future)

# Step 4: Merge actuals (y) with forecasted values
forecast_full = forecast[["ds","yhat","yhat_lower","yhat_upper"]].merge(
    df_txn, on="ds", how="left"
)

# Step 5: Save forecast with actuals
forecast_full.to_excel("Transaction_Forecast.xlsx", index=False)
print("✅ Transaction forecast with actuals saved to Transaction_Forecast.xlsx")

# Step 6: Save trained model
joblib.dump(forecast_model, "forecast_model.pkl")
print("✅ Forecast model saved as forecast_model.pkl")