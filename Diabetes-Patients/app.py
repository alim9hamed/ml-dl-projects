from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the machine learning model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from form
    pregnancies = int(request.form['pregnancies'])
    glucose = int(request.form['glucose'])
    blood_pressure = int(request.form['blood_pressure'])
    skin_thickness = int(request.form['skin_thickness'])
    insulin = int(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetes_pedigree = float(request.form['diabetes_pedigree'])
    age = int(request.form['age'])

    # Make prediction using the loaded model
    prediction = model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])

    # Render the result template with the prediction result
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
