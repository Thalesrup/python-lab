import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from datetime import datetime

data = [
    {"position":"295","date":"2024-08-01 14:00:13"},
    {"position":"295","date":"2024-08-01 14:00:13"},
    {"position":"295","date":"2024-08-01 14:00:14"},
    {"position":"294","date":"2024-08-01 15:00:11"},
    {"position":"294","date":"2024-08-01 16:00:10"},
    {"position":"294","date":"2024-08-01 17:00:16"},
    {"position":"294","date":"2024-08-01 17:00:16"},
    {"position":"294","date":"2024-08-01 18:00:14"},
    {"position":"296","date":"2024-08-01 19:00:15"},
    {"position":"295","date":"2024-08-01 20:00:11"},
    {"position":"295","date":"2024-08-01 20:00:11"},
    {"position":"295","date":"2024-08-01 21:00:10"},
    {"position":"295","date":"2024-08-01 22:00:11"},
    {"position":"295","date":"2024-08-01 23:00:12"},
    {"position":"295","date":"2024-08-02 00:00:25"},
    {"position":"295","date":"2024-08-02 01:00:11"},
    {"position":"295","date":"2024-08-02 02:00:13"},
    {"position":"295","date":"2024-08-02 02:00:13"},
    {"position":"295","date":"2024-08-02 03:00:10"},
    {"position":"295","date":"2024-08-02 04:00:11"},
    {"position":"295","date":"2024-08-02 05:00:10"},
    {"position":"295","date":"2024-08-02 05:00:10"},
    {"position":"295","date":"2024-08-02 06:00:10"},
    {"position":"295","date":"2024-08-02 07:00:11"},
    {"position":"295","date":"2024-08-02 07:00:11"},
    {"position":"295","date":"2024-08-02 08:00:11"},
    {"position":"295","date":"2024-08-02 08:00:11"},
    {"position":"295","date":"2024-08-02 09:00:12"},
    {"position":"295","date":"2024-08-02 09:00:12"},
    {"position":"295","date":"2024-08-02 10:00:09"},
    {"position":"295","date":"2024-08-02 11:00:12"},
    {"position":"295","date":"2024-08-02 12:00:16"},
    {"position":"294","date":"2024-08-02 13:00:10"},
    {"position":"294","date":"2024-08-02 13:00:10"},
    {"position":"296","date":"2024-08-02 14:00:14"},
    {"position":"296","date":"2024-08-02 15:00:16"},
    {"position":"296","date":"2024-08-02 16:00:12"},
    {"position":"296","date":"2024-08-02 16:00:12"},
    {"position":"295","date":"2024-08-02 17:00:14"},
    {"position":"295","date":"2024-08-02 17:00:14"},
    {"position":"294","date":"2024-08-02 18:00:12"},
    {"position":"294","date":"2024-08-02 18:00:12"},
    {"position":"288","date":"2024-08-02 19:00:14"},
    {"position":"289","date":"2024-08-02 20:00:15"},
    {"position":"286","date":"2024-08-02 21:00:10"},
    {"position":"289","date":"2024-08-02 22:00:10"},
    {"position":"289","date":"2024-08-02 23:00:10"},
    {"position":"289","date":"2024-08-03 00:00:18"},
    {"position":"289","date":"2024-08-03 00:00:18"},
    {"position":"289","date":"2024-08-03 01:00:12"},
    {"position":"289","date":"2024-08-03 02:00:12"},
    {"position":"289","date":"2024-08-03 02:00:12"},
    {"position":"289","date":"2024-08-03 03:00:18"},
    {"position":"289","date":"2024-08-03 03:00:18"},
    {"position":"289","date":"2024-08-03 04:00:11"},
    {"position":"289","date":"2024-08-03 05:00:15"},
    {"position":"289","date":"2024-08-03 06:00:14"},
    {"position":"289","date":"2024-08-03 06:00:14"},
    {"position":"289","date":"2024-08-03 07:00:15"},
    {"position":"289","date":"2024-08-03 07:00:15"},
    {"position":"289","date":"2024-08-03 08:00:11"},
    {"position":"289","date":"2024-08-03 09:00:12"},
    {"position":"289","date":"2024-08-03 10:00:11"},
    {"position":"289","date":"2024-08-03 10:00:11"},
    {"position":"289","date":"2024-08-03 11:00:14"},
    {"position":"289","date":"2024-08-03 11:00:14"},
    {"position":"289","date":"2024-08-03 12:00:12"},
    {"position":"289","date":"2024-08-03 13:00:09"},
    {"position":"289","date":"2024-08-03 14:00:11"},
    {"position":"289","date":"2024-08-03 14:00:11"},
    {"position":"289","date":"2024-08-03 15:00:10"},
    {"position":"289","date":"2024-08-03 16:00:11"},
    {"position":"289","date":"2024-08-03 17:00:10"},
    {"position":"289","date":"2024-08-03 18:00:13"},
    {"position":"289","date":"2024-08-03 18:00:13"},
    {"position":"289","date":"2024-08-03 19:00:12"},
    {"position":"289","date":"2024-08-03 20:00:10"},
    {"position":"289","date":"2024-08-03 20:00:10"},
    {"position":"289","date":"2024-08-03 21:00:12"},
    {"position":"289","date":"2024-08-03 21:00:12"},
    {"position":"289","date":"2024-08-03 22:00:11"},
    {"position":"289","date":"2024-08-03 23:00:09"},
    {"position":"289","date":"2024-08-04 01:00:12"},
    {"position":"289","date":"2024-08-04 02:00:12"},
    {"position":"289","date":"2024-08-04 03:00:14"},
    {"position":"289","date":"2024-08-04 04:00:11"},
    {"position":"289","date":"2024-08-04 05:00:10"},
    {"position":"289","date":"2024-08-04 06:00:10"},
    {"position":"289","date":"2024-08-04 06:00:10"},
    {"position":"289","date":"2024-08-04 07:00:11"},
    {"position":"289","date":"2024-08-04 08:00:09"},
    {"position":"289","date":"2024-08-04 08:00:09"},
    {"position":"289","date":"2024-08-04 09:00:10"},
    {"position":"289","date":"2024-08-04 10:00:09"},
    {"position":"289","date":"2024-08-04 11:00:12"},
    {"position":"289","date":"2024-08-04 12:00:11"},
    {"position":"289","date":"2024-08-04 13:00:09"},
    {"position":"289","date":"2024-08-04 13:00:09"},
    {"position":"289","date":"2024-08-04 14:00:11"},
    {"position":"289","date":"2024-08-04 14:00:11"},
    {"position":"289","date":"2024-08-04 15:00:11"},
    {"position":"289","date":"2024-08-04 16:00:10"},
    {"position":"289","date":"2024-08-04 16:00:10"},
    {"position":"289","date":"2024-08-04 17:00:12"},
    {"position":"289","date":"2024-08-04 18:00:11"},
    {"position":"289","date":"2024-08-04 18:00:11"},
    {"position":"289","date":"2024-08-04 19:00:11"},
    {"position":"289","date":"2024-08-04 20:00:12"},
    {"position":"289","date":"2024-08-04 20:00:12"},
    {"position":"289","date":"2024-08-04 21:00:14"},
    {"position":"289","date":"2024-08-04 22:00:14"},
    {"position":"289","date":"2024-08-04 22:00:14"},
    {"position":"289","date":"2024-08-04 23:00:14"},
    {"position":"289","date":"2024-08-05 00:00:33"},
    {"position":"289","date":"2024-08-05 00:00:33"},
    {"position":"289","date":"2024-08-05 01:00:13"},
    {"position":"289","date":"2024-08-05 01:00:13"},
    {"position":"289","date":"2024-08-05 02:00:11"},
    {"position":"289","date":"2024-08-05 03:00:14"},
    {"position":"289","date":"2024-08-05 04:00:14"},
    {"position":"289","date":"2024-08-05 05:00:20"},
    {"position":"289","date":"2024-08-05 06:00:30"},
    {"position":"289","date":"2024-08-05 07:09:31"},
    {"position":"289","date":"2024-08-05 09:06:28"},
    {"position":"289","date":"2024-08-05 10:01:37"},
    {"position":"286","date":"2024-08-05 14:00:15"},
    {"position":"286","date":"2024-08-05 14:00:15"}
]

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
df['second'] = df['date'].dt.second
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

df = df.sort_values(by='date')

X = df[['hour', 'minute', 'second', 'day', 'month', 'year']]
y = df['position']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

import numpy as np

future_dates = pd.date_range(start=df['date'].max(), periods=24, freq='H')
future_features = pd.DataFrame({
    'hour': future_dates.hour,
    'minute': future_dates.minute,
    'second': future_dates.second,
    'day': future_dates.day,
    'month': future_dates.month,
    'year': future_dates.year
})

predicted_positions = model.predict(future_features)

# Encontrar o tempo estimado para alcançar a posição 1
position_1_time = future_dates[np.where(predicted_positions <= 1)[0][0]]
print(f"Estimativa de quando a posição 1 será alcançada: {position_1_time}")
