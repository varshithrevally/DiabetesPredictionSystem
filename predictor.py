import numpy as np
import pandas as pd
import joblib

def predict_diabetes(input_data):
    model = joblib.load('model/logistic_regression_model.joblib')
    scaler = joblib.load('model/scaler.joblib')
    columns = joblib.load('model/column_names.joblib')

    input_array = np.asarray(input_data).reshape(1, -1)
    input_df = pd.DataFrame(input_array, columns=columns)
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    return prediction[0]
