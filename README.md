# S I M J A N G

This is a **Streamlit** application designed for exploring heart disease datasets and predicting the likelihood of heart disease based on user inputs. The app provides an interactive interface for both exploring the dataset and making predictions using a machine learning model.

## Features

- **Data Exploration**: Explore the heart disease dataset with various statistics and visualizations.
- **Prediction Page**: Enter patient details to predict whether they have heart disease based on the trained Random Forest model.
- **Interactive Visuals**: The app includes bar charts to visualize key statistics and distributions in the dataset.

## Setup and Installation

To run the app locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/santanamnaa/simjang.git
   cd simjang
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the following files are present in the root directory:
   - `heart.csv`: The dataset used for data exploration and prediction.
   - `saved_steps.pkl`: The serialized Random Forest model and encoders used for prediction.

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501` to use the app.

## Usage

### Explore Page
- This section allows you to visualize the dataset with statistics and charts. It includes:
  - Dataset overview (first few rows).
  - Basic statistical summary.
  - Class distribution of heart disease occurrences.
  - Chest pain type distribution.

### Predict Page
- This section allows you to enter patient data to predict if the patient has heart disease or not. You will need to input:
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Cholesterol
  - Fasting Blood Sugar
  - Resting ECG Results
  - Max Heart Rate Achieved
  - Exercise-induced Angina
  - Oldpeak (ST depression induced by exercise)
  - ST Slope (slope of the peak exercise ST segment)

After entering the required information, the app will return a prediction based on the model (1 = Heart Disease, 0 = No Heart Disease).

## Dependencies

- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`

## Model Information

The machine learning model used for prediction is a **Random Forest** classifier. The model was trained on a heart disease dataset and saved using `pickle`. The `saved_steps.pkl` file contains the trained model and necessary encoders for categorical variables.
