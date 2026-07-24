import joblib
import pandas as pd


# Load model

model = joblib.load(
    "models/crop_model.pkl"
)


# Load encoder

encoder = joblib.load(
    "models/label_encoder.pkl"
)



# Input values

input_data = pd.DataFrame(
    {
        "N":[90],
        "P":[42],
        "K":[43],
        "temperature":[25],
        "humidity":[80],
        "ph":[6.5],
        "rainfall":[200]
    }
)



# Prediction

prediction = model.predict(
    input_data
)



# Convert number to crop name

crop = encoder.inverse_transform(
    prediction
)



print(
    "Recommended Crop:",
    crop[0]
)



# Confidence

probability = model.predict_proba(
    input_data
)


confidence = max(probability[0])*100


print(
    "Confidence:",
    round(confidence,2),
    "%"
)