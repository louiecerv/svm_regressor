---
title: SVM Regressor
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: streamlit
sdk_version: 1.41.1
app_file: app.py
pinned: false
license: mit
short_description: App demonstrating the SVM Regressor
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# SVM Regressor Demo 🤖

This app demonstrates the use of Support Vector Machines (SVM) for regression problems in various domains. It provides a user-friendly interface to select a problem, visualize the dataset, train an SVM Regressor, and interpret the results.

## Features

* **Problem Selection:** Choose from three example problems: Business 💼, Engineering ⚙️, or Education 🎓.
* **Dataset Display:** View the corresponding dataset for the selected problem, along with a description of its features.
* **Model Training and Performance:** Train an SVM Regressor on the selected dataset. Display the model's performance using metrics like R-squared and Mean Squared Error. Adjust hyperparameters to fine-tune the model. Visualize the regression results using a scatter plot with a regression line.
* **Output Interpretation:** Get a clear explanation of the model's output in the context of the selected problem. Understand the significance of the results and how they can be used for predictions or decisions.

## Learning Objectives

* Understand the concept of SVM Regression and its applications.
* Learn how to train and evaluate SVM Regressors using Python.
* Explore the impact of different hyperparameters on the model's performance.
* Interpret and explain the results of SVM Regression in various domains.

## Datasets

The app uses three synthetic datasets for demonstration purposes:

* **Business 💼:**
    * **Features:** `Usage` (in hours), `Demographics` (binary)
    * **Target:** `Churn` (continuous)
    * **Description:** Predicts customer churn based on usage patterns and demographics.
* **Engineering ⚙️:**
    * **Features:** `Sensor_Data` (continuous)
    * **Target:** `RUL` (Remaining Useful Life) (continuous)
    * **Description:** Predicts the remaining useful life of an industrial machine based on sensor data.
* **Education 🎓:**
    * **Features:** `Study_Hours` (continuous), `Prev_Grades` (continuous)
    * **Target:** `Test_Scores` (continuous)
    * **Description:** Predicts student performance on a standardized test based on study habits and previous grades.

## How to Use

1. **Select a Problem:** Choose one of the three problems from the dropdown menu.
2. **View Dataset:** The corresponding dataset will be displayed, along with a description of its features.
3. **Train and Evaluate Model:** Adjust the hyperparameters (kernel, C, epsilon) using the sliders. The model will be trained on the dataset and its performance metrics will be displayed.
4. **Visualize Results:** The regression results will be visualized using a scatter plot with a regression line.
5. **Interpret Output:** Read the interpretation of the model's output in the context of the selected problem.

## Additional Features

* **Interactive Visualizations:** Explore the impact of different hyperparameters on the model's performance by adjusting the sliders and observing the changes in the regression results.
* **Upload Your Own Data:** Train an SVM Regressor on your own dataset by uploading a CSV file. (This feature is not yet implemented.)

## Requirements

* Python 3.7+
* Streamlit
* Pandas
* Scikit-learn
* Matplotlib

## Installation

1. Install Python 3.7+
2. Create a virtual environment (optional but recommended)
3. Activate the virtual environment
4. Install the required packages using pip: `pip install streamlit pandas scikit-learn matplotlib`

## Usage

1. Download the repository and unzip it.
2. Navigate to the repository directory.
3. Run the app using `streamlit run app.py`.

## Contributing

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

This app is inspired by [https://medium.com/coinmonks/support-vector-regression-or-svr-8eb3acf6d0ff](https://medium.com/coinmonks/support-vector-regression-or-svr-8eb3acf6d0ff).