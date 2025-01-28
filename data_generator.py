import pandas as pd
import numpy as np

def generate_business_data():
    np.random.seed(0)
    n_samples = 100
    usage_patterns = np.random.rand(n_samples) * 100
    demographics = np.random.randint(0, 2, n_samples)
    churn = (
        10 + 5 * usage_patterns - 2 * demographics + np.random.randn(n_samples) * 5
    )
    df = pd.DataFrame({"Usage": usage_patterns, "Demographics": demographics, "Churn": churn})
    df.to_csv("business_data.csv", index=False)

def generate_engineering_data():
    np.random.seed(1)
    n_samples = 100
    sensor_data = np.random.rand(n_samples) * 50
    rul = 100 - 2 * sensor_data + np.random.randn(n_samples) * 10
    df = pd.DataFrame({"Sensor_Data": sensor_data, "RUL": rul})
    df.to_csv("engineering_data.csv", index=False)

def generate_education_data():
    np.random.seed(2)
    n_samples = 100
    study_hours = np.random.rand(n_samples) * 50
    prev_grades = np.random.rand(n_samples) * 4
    test_scores = 20 + 5 * study_hours + 10 * prev_grades + np.random.randn(n_samples) * 5
    df = pd.DataFrame({"Study_Hours": study_hours, "Prev_Grades": prev_grades, "Test_Scores": test_scores})
    df.to_csv("education_data.csv", index=False)

if __name__ == "__main__":
    generate_business_data()
    generate_engineering_data()
    generate_education_data()