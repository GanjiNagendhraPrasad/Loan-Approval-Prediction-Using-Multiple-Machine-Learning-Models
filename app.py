from flask import Flask, render_template, request
import numpy as np
import pickle

# Load trained model (Random Forest / best model)
with open('load.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        features = np.array([[
            float(request.form['person_age']),
            float(request.form['person_gender']),
            float(request.form['person_income']),
            float(request.form['person_emp_exp']),
            float(request.form['loan_amnt']),
            float(request.form['loan_int_rate']),
            float(request.form['loan_percent_income']),
            float(request.form['cb_person_cred_hist_length']),
            float(request.form['credit_score'])
        ]])

        pred = model.predict(features)[0]

        if pred == 1:
            prediction = "Yes"
        else:
            prediction = "No"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)