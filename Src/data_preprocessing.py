import pandas as pd


def load_data():

    data = pd.read_csv(
        "dataset/Crop_recommendation.csv"
    )

    return data



def prepare_data():

    data = load_data()

    print("Dataset Shape:")
    print(data.shape)

    print("\nFirst 5 Rows:")
    print(data.head())


    X = data.drop("label", axis=1)

    y = data["label"]


    return X, y



if __name__ == "__main__":

    X, y = prepare_data()

    print("\nFeatures:")
    print(X.columns)

    print("\nTarget:")
    print(y.unique())