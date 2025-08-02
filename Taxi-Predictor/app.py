from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    # Get inputs from the form
    price = float(request.form["v1"])
    population = float(request.form["population"])
    income = float(request.form["income"])
    parking = float(request.form["parking"])

    # ✅ Use correct variable name: price instead of priceperweek
    features = np.array([[price, population, income, parking]])
    prediction = model.predict(features)

    return render_template("result.html", prediction_text=f"Predicted weekly riders: {int(prediction[0])}")

if __name__ == '__main__':
    print("✅ Flask app running...")
    app.run(debug=True)
