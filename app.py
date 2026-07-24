from flask import Flask, render_template, request
import joblib
import pandas as pd

from fertilizer_recommendation import fertilizer_advice
from model_info import MODEL_INFO


app = Flask(__name__)


model = joblib.load(
    "models/crop_model.pkl"
)


encoder = joblib.load(
    "models/label_encoder.pkl"
)



# Store values for dashboard

chart_data = {}



@app.route("/")
def home():

    return render_template(
        "index.html",
        model_info=MODEL_INFO
    )



@app.route("/predict", methods=["POST"])
def predict():

    global chart_data


    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])

    temperature = float(
        request.form["temperature"]
    )

    humidity = float(
        request.form["humidity"]
    )

    ph = float(
        request.form["ph"]
    )

    rainfall = float(
        request.form["rainfall"]
    )


    input_data = pd.DataFrame({

        "N":[N],
        "P":[P],
        "K":[K],
        "temperature":[temperature],
        "humidity":[humidity],
        "ph":[ph],
        "rainfall":[rainfall]

    })



    prediction = model.predict(
        input_data
    )


    crop = encoder.inverse_transform(
        prediction
    )[0]



    probability = model.predict_proba(
        input_data
    )


    confidence = round(
        max(probability[0])*100,
        2
    )



    fertilizer = fertilizer_advice(
        N,
        P,
        K
    )



    chart_data = {

        "N":N,
        "P":P,
        "K":K,

        "temperature":temperature,
        "humidity":humidity,
        "rainfall":rainfall

    }



    return render_template(

        "index.html",

        prediction=crop,

        confidence=confidence,

        fertilizer=fertilizer,

        model_info=MODEL_INFO

    )




@app.route("/dashboard")
def dashboard():

    return render_template(

        "dashboard.html",

        data=chart_data,

        model_info=MODEL_INFO

    )



if __name__=="__main__":

    app.run(debug=True)