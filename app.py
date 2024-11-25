import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, request, jsonify, redirect, url_for
from tensorflow.keras.models import load_model

app = Flask(__name__)

with open('models/scaleing.pkl', 'rb') as file:
    scaler = pickle.load(file)

model = load_model('models/ANN_Model.h5')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():

    if request.method == 'POST':
        gender = request.form.get('GENDER')
        age = request.form.get('AGE')
        smoking = request.form.get('SMOKING')
        yellow_fingers = request.form.get('YELLOW_FINGERS')
        anxiety = request.form.get('ANXIETY')
        peer_pressure = request.form.get('PEER_PRESSURE')
        chronic_disease = request.form.get('CHRONIC_DISEASE')
        fatigue = request.form.get('FATIGUE')
        allergy = request.form.get('ALLERGY')
        wheezing = request.form.get('WHEEZING')
        alcohol_consuming = request.form.get('ALCOHOL_CONSUMING')
        couging = request.form.get('COUGHING')
        shortness_of_breath = request.form.get('SHORTNESS_OF_BREATH')
        swallowing_difficulty = request.form.get('SWALLOWING_DIFFICULTY')
        chest_pain = request.form.get('CHEST_PAIN')

        inputs = np.array([[gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, couging, shortness_of_breath, swallowing_difficulty, chest_pain]])
        df = pd.DataFrame(inputs, columns=scaler.get_feature_names_out())

        scaled_inputs = scaler.transform(df)
        prediction = model.predict(scaled_inputs)[0][0]
        output = 'Have Cancer' if prediction >= 0.5 else 'No Cancer'

        return render_template('form.html', prediction=output)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True, port=80)