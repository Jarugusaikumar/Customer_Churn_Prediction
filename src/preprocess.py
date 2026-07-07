import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

from src.utils import load_data, PROCESSED_PATH


class ColumnDropper(BaseEstimator, TransformerMixin):
    def __init__(self, columns=None):
        self.columns = columns or []

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(columns=self.columns, errors="ignore")


def preprocess_data():
    df = load_data()
    df = df.copy()
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.drop(columns=["customerID"], errors="ignore")
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()
    numeric_features = X.select_dtypes(exclude=["object"]).columns.tolist()

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    processed = {
        "X_train": X_train_processed,
        "X_test": X_test_processed,
        "y_train": y_train,
        "y_test": y_test,
        "preprocessor": preprocessor,
        "feature_names": X.columns.tolist(),
    }

    return processed
