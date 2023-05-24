from flask import Flask, render_template, request
import joblib

model = joblib.load("../artifacts/training/model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == 'POST':
        square_foot = int(request.form['squarefoot'])
        room = int(request.form['room'])
        predict = model.predict([[square_foot, room]])
    return render_template('index.html', prediction=predict)

if __name__ == '__main__':
    app.run(debug=True)    