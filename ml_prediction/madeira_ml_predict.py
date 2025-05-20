import pandas as pd
import joblib

def predict_from_csv(csv_path, model_path='madeira_basalt_model.pkl'):
    df = pd.read_csv(csv_path)
    X = df[['SiO2', 'MgO', 'CaO', 'Fe2O3']]
    model = joblib.load(model_path)
    predictions = model.predict(X)
    return predictions

if __name__ == "__main__":
    preds = predict_from_csv('sample_basalt_data.csv')
    print("Predictions:", preds) 