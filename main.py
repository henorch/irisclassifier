from flask import Flask, render_template,request
import joblib


app = Flask("__name__");
model = joblib.load("./models/irisflower.pkl")


@app.route('/')
def home():
    return render_template("./predict.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    features = [sepal_length, sepal_width, petal_length, petal_width]

    prediction = model.predict([features])

    return render_template("./predict.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)