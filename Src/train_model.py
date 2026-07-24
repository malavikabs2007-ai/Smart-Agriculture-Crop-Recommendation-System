import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from data_preprocessing import prepare_data


# Load data

X, y = prepare_data()


# Convert crop names into numbers

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)


# Save encoder

joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)


# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)


# -------------------------
# Random Forest
# -------------------------

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


rf_model.fit(
    X_train,
    y_train
)


rf_prediction = rf_model.predict(
    X_test
)


rf_accuracy = accuracy_score(
    y_test,
    rf_prediction
)


print("Random Forest Accuracy:",
      rf_accuracy)



# -------------------------
# XGBoost
# -------------------------

xgb_model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)


xgb_model.fit(
    X_train,
    y_train
)


xgb_prediction = xgb_model.predict(
    X_test
)


xgb_accuracy = accuracy_score(
    y_test,
    xgb_prediction
)


print("XGBoost Accuracy:",
      xgb_accuracy)



# Choose best model

if rf_accuracy > xgb_accuracy:

    best_model = rf_model

    print("Best Model: Random Forest")

else:

    best_model = xgb_model

    print("Best Model: XGBoost")



# Save model

joblib.dump(
    best_model,
    "models/crop_model.pkl"
)


print("Model Saved Successfully!")