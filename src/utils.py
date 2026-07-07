from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
PROCESSED_PATH = ROOT / "data" / "processed"
MODEL_PATH = ROOT / "models" / "churn_model.pkl"


def load_data(path: Path | None = None) -> pd.DataFrame:
    data_path = path or DATA_PATH
    return pd.read_csv(data_path)


def ensure_directories() -> None:
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
