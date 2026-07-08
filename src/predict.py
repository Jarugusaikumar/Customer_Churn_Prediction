import joblib
import pandas as pd

from src.utils import MODEL_PATH


def load_model():
    artifact = joblib.load(MODEL_PATH)

    if isinstance(artifact, dict) and "model" in artifact and "preprocessor" in artifact:
        return artifact

    if hasattr(artifact, "predict_proba"):
        from src.train import train_model

        train_model()
        artifact = joblib.load(MODEL_PATH)

        if isinstance(artifact, dict) and "model" in artifact and "preprocessor" in artifact:
            return artifact

        raise RuntimeError(
            "The model artifact was rebuilt, but the new artifact still has an unsupported format. "
            "Check your training pipeline and ensure the saved model is a dict bundle."
        )

    raise RuntimeError(
        f"Loaded model artifact has unsupported format: {type(artifact).__name__}. "
        "Delete models/churn_model.pkl and retrain the model."
    )


def predict_churn(input_data: dict):
    bundle = load_model()
    model = bundle["model"]
    preprocessor = bundle["preprocessor"]

    if preprocessor is None:
        raise RuntimeError(
            "The model bundle does not include a preprocessor. "
            "Retrain the model by deleting models/churn_model.pkl and restarting the app."
        )

    row = pd.DataFrame([input_data])
    row["TotalCharges"] = pd.to_numeric(row["TotalCharges"], errors="coerce")
    features = preprocessor.transform(row)
    probability = model.predict_proba(features)[0, 1]
    label = "Yes" if probability >= 0.5 else "No"
    return {
        "prediction": label,
        "probability": round(float(probability), 4),
    }
