“AI-Powered Banking Analytics: Automated Power BI Documentation, Churn Prediction, and Transaction Forecasting”
________________________________________
** Project Workflow **
________________________________________
**1.	 Data Acquisition (Kaggle)**
•	Dataset sourced from Kaggle (credit card / banking dataset).
•	Contains customer demographics, credit card transactions, and account details.
•	Cleaned and transformed data in Power BI for dashboard building.
________________________________________
**2.	Interactive Power BI Dashboard**
•	Built two key analytics pages:
1.	Customer Churn Insights → shows churn risk, drivers, segmentation.
2.	Transaction Forecasting → predicts future monthly transactions with confidence bands.
•	Added KPI cards, slicers, and professional formatting.
•	Ensured design follows business needs: customer risk, forecasting, and governance.
________________________________________
**3.	 Automated Documentation (Python + VPAX)**
•	Exported the Power BI data model (VPAX) using DAX Studio.
•	Created a Python script to automatically generate:
o	Word doc with model documentation.
o	Excel file with tables, relationships, and fields.
o	ER diagram image.
•	This automation saves analysts hours of manual work and enforces governance.
________________________________________
**4.	 Churn Prediction Model (Python + Power BI)**
•	Built a Random Forest model for churn prediction.
•	Output:
o	Customer-level churn probability.
o	Risk categories (Low, Medium, High).
o	Feature importance (drivers of churn).
•	Exported predictions to Excel → Imported into Power BI.
•	Added Churn Risk Dashboard:
o	Distribution of churn risk.
o	Top churn drivers (feature importance bar chart).
________________________________________
**5.	Transaction Forecasting Model (Python + Prophet)**
•	Used Prophet (Facebook’s forecasting library) to model monthly transaction volumes.
•	Forecasted next 12 months with confidence intervals (yhat_lower, yhat_upper).
•	Exported results to Excel → Integrated into Power BI.
•	Added Transaction Forecasting Dashboard:
o	Actual vs Forecast line chart (with confidence band).
o	KPI cards (Next Month Forecast, YoY Growth).
o	Clustered column chart for recent 12 months.
________________________________________
**6.	End-to-End Data & AI Pipeline
•	Data Source (Kaggle) → Power BI Dashboard → Automated Documentation → AI/ML Models → Power BI Insights.**

**File Details:**

**.idea/**	PyCharm IDE configuration folder (auto-generated).
**Churn Prediction + Forecasting.py**	Main Python script for churn prediction (Random Forest) and transaction forecasting (Prophet).
**churn_model.pkl**	Saved machine learning model (Random Forest) for churn prediction.
**Churn_Predictions.xlsx** Excel output of churn probabilities and risk categories per customer.
**Credit Card Financial Dashboard.pbix**	Power BI dashboard file (interactive BI report).
**Credit Card Financial Dashboard.pdf**	Exported PDF version of the Power BI dashboard.
**credit_card.xlsx**	Kaggle dataset (credit card transactions / account features).
**customer.xlsx**	Kaggle dataset (customer demographic and account info).
**DocumentationGenerator.py**	Python script that parses VPAX model and generates automated Power BI documentation.
**Feature_Importance.xlsx**	Feature importance scores from churn model (top churn drivers).
**forecast_model.pkl**	Saved Prophet model for forecasting monthly transactions.
LICENSE	License file for open-source/public sharing.
**model.vpax**	Exported Power BI data model (via DAX Studio) for documentation.
**PowerBI_Documentation.docx**	Word output of auto-generated Power BI documentation.
**PowerBI_Documentation.xlsx**	Excel output of auto-generated Power BI documentation.
**PowerBI_ER_Diagram.png**	Entity-Relationship diagram image generated from Power BI model.
**README.md**	Markdown summary file for GitHub/Kaggle.
**Transaction_Forecast.xlsx**	Excel output containing actuals + forecast (Prophet) with confidence bounds.

