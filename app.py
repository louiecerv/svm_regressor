import streamlit as st
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# --- Function to perform SVM Regression and display results ---
def perform_svm_regression(df, problem_description, interpretation_text):
    st.write(problem_description)
    st.write("**Dataset:**")
    st.write(df)

    # Hyperparameters with unique keys
    kernel = st.selectbox("Kernel:", ("linear", "rbf", "poly"), key=f"kernel_{problem_description}")
    C = st.slider("C (Regularization parameter):", 0.1, 10.0, 1.0, 0.1, key=f"C_{problem_description}")
    epsilon = st.slider("Epsilon (Tolerance for errors):", 0.01, 1.0, 0.1, 0.01, key=f"epsilon_{problem_description}")

    # Train-test split
    X = df.iloc[:,:-1]
    y = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model training
    model = SVR(kernel=kernel, C=C, epsilon=epsilon)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f"Mean Squared Error: {mse:.2f}")
    st.write(f"R-squared: {r2:.2f}")

    # Visualization
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred)
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "k--", lw=2)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    st.pyplot(fig)

    # Interpretation
    st.write("**Interpretation:**")
    st.write(interpretation_text)


def main():
    # --- App ---
    st.title("SVM Regressor Demo")

    about = """This app demonstrates the use of Support Vector Machine (SVM) regression 
    for different problems: Business, Engineering, and Education.  Select a problem to 
    view the dataset, train an SVM model, and interpret the results.  Explore the 
    impact of hyperparameter tuning and visualize the predictions.

    Created by Louie F. Cervantes, M.Eng. (Information Engineering)"""
    with st.expander("About"):
        st.markdown(about) 

    # Tabs for each problem
    tab1, tab2, tab3 = st.tabs(
        ["Business Problem", "Engineering Problem", "Education Problem"]
    )

    # --- Business Problem ---
    with tab1:
        df = pd.read_csv("business_data.csv")
        perform_svm_regression(
            df,
            "**Business Problem:** Predicting customer churn based on usage patterns and demographics.",
            "The model predicts customer churn rate based on usage patterns and demographics. "
            "This information can be used to identify customers at risk of churning and take proactive steps to retain them.",
        )

    # --- Engineering Problem ---
    with tab2:
        df = pd.read_csv("engineering_data.csv")
        perform_svm_regression(
            df,
            "**Engineering Problem:** Predicting the remaining useful life of an industrial machine based on sensor data.",
            "The model predicts the remaining useful life of an industrial machine based on sensor data. "
            "This information can be used to schedule maintenance and prevent costly downtime.",
        )

    # --- Education Problem ---
    with tab3:
        df = pd.read_csv("education_data.csv")
        perform_svm_regression(
            df,
            "**Education Problem:** Predicting student performance on a standardized test based on study habits and previous grades.",
            "The model predicts student performance on a standardized test based on study habits and previous grades. "
            "This information can be used to identify students who may need extra help and provide them with appropriate support.",
        )

if __name__ == "__main__":
    main()