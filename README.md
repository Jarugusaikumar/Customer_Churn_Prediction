# Customer Churn Prediction

This project trains a churn prediction model on the Telco customer churn dataset and exposes it through a Streamlit dashboard.

## Setup

```bash
pip install -r requirements.txt
```

## Run the app

```bash
streamlit run app/app.py
```

## Project structure

- app/app.py: Streamlit dashboard
- src/preprocess.py: data preprocessing pipeline
- src/train.py: model training script
- src/predict.py: inference helper
- src/utils.py: shared paths and data loading helpers
