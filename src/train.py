import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

from src.preprocess import preprocess_data
from src.utils import MODEL_PATH


def train_model():
    data = preprocess_data()
    X_train = data["X_train"]
    X_test = data["X_test"]
    y_train = data["y_train"]
    y_test = data["y_test"]

    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({
        "model": model,
        "preprocessor": data["preprocessor"],
        "feature_names": data["feature_names"],
    }, MODEL_PATH)

    return {
        "accuracy": round(float(accuracy), 4),
        "roc_auc": round(float(roc_auc), 4),
        "report": classification_report(y_test, predictions, output_dict=True),
    }


if __name__ == "__main__":
    print(train_model())
