# ML Prediction

This folder contains scripts and notebooks for machine learning model training and prediction for ERW basalt properties.

- `model_training.ipynb`: Jupyter notebook for training a regression model on geochemical data.
- `madeira_ml_predict.py`: Script for making predictions from new data using the trained model.
- `sample_basalt_data.csv`: Example input data for prediction.

## Usage

1. Train a model in the notebook and save it as `madeira_basalt_model.pkl`.
2. Use `madeira_ml_predict.py` to predict on new data:
   ```bash
   python ml_prediction/madeira_ml_predict.py
   ``` 