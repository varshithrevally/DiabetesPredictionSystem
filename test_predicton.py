from predictor import predict_diabetes

sample = (1, 85, 66, 29, 0, 26.6, 0.351, 31)
result = predict_diabetes(sample)

print("Diabetic" if result else "Non-diabetic")
