-- SQL script to populate a basic churn dashboard table
CREATE TABLE IF NOT EXISTS churn_dashboard (
    customerID VARCHAR(50),
    gender VARCHAR(20),
    SeniorCitizen INT,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    Contract VARCHAR(30),
    MonthlyCharges DECIMAL(10,2),
    TotalCharges DECIMAL(10,2),
    Churn VARCHAR(10)
);

INSERT INTO churn_dashboard (customerID, gender, SeniorCitizen, Partner, Dependents, tenure, Contract, MonthlyCharges, TotalCharges, Churn) VALUES
('7590-VHVEG', 'Female', 0, 'Yes', 'No', 1, 'Month-to-month', 29.85, 29.85, 'No'),
('5575-GNVDE', 'Male', 0, 'No', 'No', 34, 'One year', 56.95, 1889.50, 'No'),
('3668-QPYBK', 'Male', 0, 'No', 'No', 2, 'Month-to-month', 53.85, 108.15, 'Yes');
