# DiabetesPredictionSystem


This is a web-based application developed using Streamlit and Python that predicts whether a person is likely to have diabetes based on input health parameters. The application uses a Logistic Regression model trained on the Pima Indians Diabetes Dataset.

## Project Overview

The goal of this project is to create a simple and effective diabetes prediction tool that takes commonly available health metrics as input and returns a binary prediction: Diabetic or Non-Diabetic. The app is easy to use and runs entirely in the browser.

## Features

- User-friendly web interface built with Streamlit
- Accepts health metrics as input
- Predicts diabetes using a trained machine learning model
- Built with Python and Scikit-learn
- Can be hosted online (e.g., Streamlit Cloud)

## Technologies Used

- Python
- Streamlit
- Pandas and NumPy
- Scikit-learn (Logistic Regression)
- Joblib (for saving and loading the model and scaler)

## Project Structure

DiabetesPredictionSystem/
├── app.py                         
├── predictor.py                    
├── model/
│   ├── logistic_regression_model.joblib  
│   ├── scaler.joblib                      
│   └── column_names.joblib              
├── diabetes.csv                     
├── requirements.txt             
└── README.md      


## How to Run Locally

1. Clone the repository:
git clone https://github.com/varshithrevally/diabetes-prediction-app.git
cd DiabetesPredictionSystem


2. Install required packages:
pip install -r requirements.txt


3. Start the Streamlit application:
streamlit run app.py

## Live Demo
 You can access the live version at:
 https://diabetespredictionsystem-ml.streamlit.app/

## Input Parameters

The app requires the following health parameters as input:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## Output

The application returns:
- 0 → Non-Diabetic
- 1 → Diabetic

## Possible Improvements

- Add multiple model options and allow users to choose
- Display prediction probability
- Include data visualizations and charts
- Add authentication for saving user history

## License

This project is licensed under the MIT License.

## Acknowledgements

- Pima Indians Diabetes Dataset from Kaggle
- Streamlit for the frontend framework
- scikit-learn for machine learning algorithms


