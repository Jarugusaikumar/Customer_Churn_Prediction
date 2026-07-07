-- Create Database
CREATE DATABASE CustomerChurnDB;
GO

-- Use Database
USE CustomerChurnDB;
GO

-- Create Table
CREATE TABLE customer_predictions
(
    id INT IDENTITY(1,1) PRIMARY KEY,
    customerID VARCHAR(20),
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(5),
    Dependents VARCHAR(5),
    tenure INT,
    PhoneService VARCHAR(5),
    InternetService VARCHAR(30),
    Contract VARCHAR(30),
    PaymentMethod VARCHAR(50),
    MonthlyCharges DECIMAL(10,2),
    TotalCharges DECIMAL(10,2),
    Prediction VARCHAR(10),
    PredictionProbability DECIMAL(5,2),
    PredictionDate DATETIME DEFAULT GETDATE()
);
GO
USE CustomerChurnDB;
GO

SELECT * FROM customer_predictions;
--Insert a Test Record
INSERT INTO customer_predictions
(
customerID,
gender,
SeniorCitizen,
Partner,
Dependents,
tenure,
PhoneService,
InternetService,
Contract,
PaymentMethod,
MonthlyCharges,
TotalCharges,
Prediction,
PredictionProbability
)
VALUES
(
'7590-VHVEG',
'Female',
0,
'Yes',
'No',
12,
'Yes',
'Fiber optic',
'Month-to-month',
'Electronic check',
70.35,
845.50,
'Yes',
0.91
);
SELECT * FROM customer_predictions;
SELECT * FROM customer_predictions;