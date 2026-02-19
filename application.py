import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Import ridge regressor and standard scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Home page


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
            Temperature = float(request.form["Temperature"])
            RH = float(request.form["RH"])
            WS = float(request.form["WS"])
            Rain = float(request.form["Rain"])
            FFMC = float(request.form["FFMC"])
            DMC = float(request.form["DMC"])
            ISI = float(request.form["ISI"])
            Classes = float(request.form["Classes"])
            Region = float(request.form["Region"])

            data = [[Temperature, RH, WS, Rain, FFMC, DMC, ISI, Classes, Region]]

            scaled_data = standard_scaler.transform(data)
            prediction = ridge_model.predict(scaled_data)

            return render_template('home.html', results=prediction[0])

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
