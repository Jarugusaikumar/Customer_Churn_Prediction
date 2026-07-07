import joblib
import pandas as pd

from src.utils import MODEL_PATH


def load_model():
    return joblib.load(MODEL_PATH)


def predict_churn(input_data: dict):
    bundle = load_model()
    model = bundle["model"]
    preprocessor = bundle["preprocessor"]

    row = pd.DataFrame([input_data])
    row["TotalCharges"] = pd.to_numeric(row["TotalCharges"], errors="coerce")
    features = preprocessor.transform(row)
    probability = model.predict_proba(features)[0, 1]
    label = "Yes" if probability >= 0.5 else "No"
    return {
        "prediction": label,
        "probability": round(float(probability), 4),
    }
