import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def prepare_data(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['hours_since_start'] = (df['date'] - df['date'].min()).dt.total_seconds() / 3600
    inputs = df['hours_since_start'].values.reshape(-1, 1)
    outputs = df['position'].values
    return inputs, outputs, df

def train_polynomial_model(inputs, outputs, degree=2):
    polynomial_features = PolynomialFeatures(degree=degree)
    inputs_poly = polynomial_features.fit_transform(inputs)
    model = LinearRegression()
    model.fit(inputs_poly, outputs)
    return model, polynomial_features

def predict_time_polynomial(data, target_position, degree=2):
    inputs, outputs, df = prepare_data(data)
    model, poly_features = train_polynomial_model(inputs, outputs, degree)
    
    max_time = inputs.max()
    times = np.linspace(0, max_time * 2, 10000).reshape(-1, 1)
    times_poly = poly_features.transform(times)
    predicted_positions = model.predict(times_poly)
    
    if predicted_positions.min() > target_position or predicted_positions.max() < target_position:
        raise ValueError(f"A posição alvo {target_position} está fora do intervalo previsto.")
    
    target_time_in_hours = np.interp(target_position, predicted_positions[::-1], times[::-1].flatten())
    
    if target_time_in_hours < 0:
        raise ValueError(f"A previsão resultou em um valor negativo: {target_time_in_hours}")

    predicted_date = df['date'].min() + pd.to_timedelta(target_time_in_hours, unit='h')
    
    return target_time_in_hours, predicted_date

data = [
    {"position": 295, "date": "2024-08-01 14:00:13"},
    {"position": 295, "date": "2024-08-01 14:00:14"},
    {"position": 294, "date": "2024-08-01 15:00:11"},
    {"position": 294, "date": "2024-08-01 16:00:10"},
    {"position": 294, "date": "2024-08-01 17:00:16"},
    {"position": 294, "date": "2024-08-01 18:00:14"},
    {"position": 296, "date": "2024-08-01 19:00:15"},
    {"position": 295, "date": "2024-08-01 20:00:11"},
    {"position": 295, "date": "2024-08-01 21:00:10"},
    {"position": 295, "date": "2024-08-01 22:00:11"},
    {"position": 295, "date": "2024-08-01 23:00:12"},
    {"position": 295, "date": "2024-08-02 00:00:25"},
    {"position": 295, "date": "2024-08-02 01:00:11"},
    {"position": 295, "date": "2024-08-02 02:00:13"},
    {"position": 295, "date": "2024-08-02 03:00:10"},
    {"position": 295, "date": "2024-08-02 04:00:11"},
    {"position": 295, "date": "2024-08-02 05:00:10"},
    {"position": 295, "date": "2024-08-02 06:00:10"},
    {"position": 295, "date": "2024-08-02 07:00:11"},
    {"position": 295, "date": "2024-08-02 08:00:11"},
    {"position": 295, "date": "2024-08-02 09:00:12"},
    {"position": 295, "date": "2024-08-02 10:00:09"},
    {"position": 295, "date": "2024-08-02 11:00:12"},
    {"position": 295, "date": "2024-08-02 12:00:16"},
    {"position": 294, "date": "2024-08-02 13:00:10"},
    {"position": 296, "date": "2024-08-02 14:00:14"},
    {"position": 296, "date": "2024-08-02 15:00:16"},
    {"position": 296, "date": "2024-08-02 16:00:12"},
    {"position": 295, "date": "2024-08-02 17:00:14"},
    {"position": 294, "date": "2024-08-02 18:00:12"},
    {"position": 288, "date": "2024-08-02 19:00:14"},
    {"position": 289, "date": "2024-08-02 20:00:15"},
    {"position": 286, "date": "2024-08-02 21:00:10"}
]

target_position = 283
predicted_time_in_hours, predicted_date = predict_time_polynomial(data, target_position)

print(f"O tempo previsto para atingir a posição {target_position} é {predicted_time_in_hours} horas, aproximadamente em {predicted_date}")
