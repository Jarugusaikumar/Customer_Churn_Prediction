from setuptools import setup, find_packages

setup(
    name="customer-churn-prediction",
    version="0.1.0",
    description="Customer churn prediction project",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "xgboost",
        "joblib",
        "jupyter",
    ],
)
