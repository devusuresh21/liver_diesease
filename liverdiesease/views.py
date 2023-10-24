from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression

import pickle

# Load the trained model
with open('logreg_model.pkl', 'rb') as model_file:
    logreg = pickle.load(model_file)

def predict(request):
    if request.method == 'POST':
        # Get input values from the form
        input_values = np.array([
            float(request.POST['age']),
            float(request.POST['total_bilirubin']),
            float(request.POST['direct_bilirubin']),
            float(request.POST['alkaline_phosphatase']),
            float(request.POST['alamine_aminotransferase']),
            float(request.POST['aspartate_aminotransferase']),
            float(request.POST['total_proteins']),
            float(request.POST['albumin']),
            0.78,
            float(request.POST['albumin_and_globulin_ratio']),
            float(request.POST['gender']),

        ]).reshape(1, -1)
        inp=np.array([0.36046510, 0.1, 0.00671141, 0.01020408, 0.39590255, 0.06180905, 0.01870679, 0.75362319, 0.52173913, 0.16, 1.0]).reshape(1, -1)

        print([input_values])

        # Make the prediction using the loaded model
        # prediction = logreg.predict([inp])[0]
        prediction = logreg.predict(input_values)

# Map the predicted labels to meaningful class names
        predicted_class = "Healthy" if prediction[0] == 0 else "You have Liver Disease"

# Display the result
        print("Predicted Class:", predicted_class)

        # Determine the result message based on the prediction
        result_message = "You have Liver Disease" if prediction == 1 else "Healthy"

        return render(request, 'result.html', {'result_message': result_message})

    return render(request, 'predict.html')
