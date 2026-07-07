import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.predict import predict_churn
from src.train import train_model
from src.utils import MODEL_PATH

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.title("Customer Churn Prediction")
st.caption("Enter customer details to estimate whether they are likely to churn.")

if not MODEL_PATH.exists():
    with st.spinner("Training the churn model for the first time..."):
        metrics = train_model()
    st.success(f"Model trained successfully with accuracy {metrics['accuracy']} and ROC-AUC {metrics['roc_auc']}")
else:
    st.success("Loaded existing trained model.")

with st.sidebar:
    st.header("Model info")
    if MODEL_PATH.exists():
        st.write(f"Model file: {MODEL_PATH.name}")
    st.write("This app uses a trained Random Forest model on the Telco customer churn dataset.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.selectbox("Partner", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
        MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
        InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
        DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

    with col2:
        TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
        PaymentMethod = st.selectbox(
            "Payment Method",
            ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
        )
        MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=65.0, step=0.1)
        TotalCharges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1000.0, step=0.1)

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
    }

    result = predict_churn(payload)
    st.subheader("Prediction Result")
    st.metric("Churn Prediction", result["prediction"])
    st.metric("Churn Probability", f"{result['probability'] * 100:.2f}%")
    st.progress(result["probability"])
