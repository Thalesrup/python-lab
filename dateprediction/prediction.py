import pandas as pd

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
    {"position":"286","date":"2024-08-05 14:00:15"},
    {"position":"286","date":"2024-08-05 15:00:12"},
    {"position":"286","date":"2024-08-05 16:00:11"},
    {"position":"286","date":"2024-08-05 16:00:11"},
    {"position":"285","date":"2024-08-05 17:00:11"},
    {"position":"284","date":"2024-08-05 18:00:13"},
    {"position":"284","date":"2024-08-05 18:00:13"},
    {"position":"284","date":"2024-08-05 19:00:14"},
    {"position":"285","date":"2024-08-05 20:00:15"},
    {"position":"285","date":"2024-08-05 20:00:15"},
    {"position":"283","date":"2024-08-05 21:00:11"},
    {"position":"283","date":"2024-08-05 22:00:12"},
    {"position":"283","date":"2024-08-05 23:00:10"},
    {"position":"283","date":"2024-08-06 00:00:22"},
    {"position":"283","date":"2024-08-06 01:00:11"},
    {"position":"283","date":"2024-08-06 02:00:15"},
    {"position":"283","date":"2024-08-06 02:00:15"},
    {"position":"283","date":"2024-08-06 03:00:12"},
    {"position":"283","date":"2024-08-06 04:00:13"},
    {"position":"283","date":"2024-08-06 04:00:13"},
    {"position":"283","date":"2024-08-06 05:00:10"},
    {"position":"283","date":"2024-08-06 05:00:10"},
    {"position":"283","date":"2024-08-06 06:00:10"},
    {"position":"283","date":"2024-08-06 07:00:11"},
    {"position":"283","date":"2024-08-06 08:00:13"},
    {"position":"283","date":"2024-08-06 08:00:13"},
    {"position":"283","date":"2024-08-06 09:00:11"},
    {"position":"283","date":"2024-08-06 10:00:11"},
    {"position":"283","date":"2024-08-06 10:00:11"},
    {"position":"283","date":"2024-08-06 11:00:10"},
    {"position":"283","date":"2024-08-06 11:00:10"},
    {"position":"283","date":"2024-08-06 12:00:13"},
    {"position":"282","date":"2024-08-06 13:00:11"},
    {"position":"282","date":"2024-08-06 14:00:15"},
    {"position":"281","date":"2024-08-06 15:00:15"},
    {"position":"281","date":"2024-08-06 16:00:13"},
    {"position":"279","date":"2024-08-06 17:00:11"},
    {"position":"277","date":"2024-08-06 18:00:13"},
    {"position":"276","date":"2024-08-06 19:00:10"},
    {"position":"276","date":"2024-08-06 20:00:11"},
    {"position":"275","date":"2024-08-06 21:00:11"},
    {"position":"275","date":"2024-08-06 21:00:11"},
    {"position":"275","date":"2024-08-06 22:00:12"},
    {"position":"275","date":"2024-08-06 22:00:12"},
    {"position":"275","date":"2024-08-06 23:00:14"},
    {"position":"275","date":"2024-08-06 23:00:14"},
    {"position":"274","date":"2024-08-07 00:00:31"},
    {"position":"274","date":"2024-08-07 01:00:11"},
    {"position":"274","date":"2024-08-07 02:00:15"},
    {"position":"274","date":"2024-08-07 03:00:18"},
    {"position":"274","date":"2024-08-07 04:00:15"},
    {"position":"274","date":"2024-08-07 05:00:12"},
    {"position":"274","date":"2024-08-07 06:00:15"},
    {"position":"274","date":"2024-08-07 08:00:10"},
    {"position":"274","date":"2024-08-07 09:00:11"},
    {"position":"274","date":"2024-08-07 09:00:11"},
    {"position":"274","date":"2024-08-07 10:00:11"},
    {"position":"273","date":"2024-08-07 11:00:10"},
    {"position":"273","date":"2024-08-07 11:00:10"},
    {"position":"272","date":"2024-08-07 12:00:12"},
    {"position":"270","date":"2024-08-07 13:00:12"},
    {"position":"270","date":"2024-08-07 14:00:13"},
    {"position":"271","date":"2024-08-07 15:00:13"},
    {"position":"270","date":"2024-08-07 16:00:16"},
    {"position":"269","date":"2024-08-07 17:00:11"},
    {"position":"269","date":"2024-08-07 17:00:11"},
    {"position":"268","date":"2024-08-07 18:00:12"},
    {"position":"268","date":"2024-08-07 18:00:12"},
    {"position":"268","date":"2024-08-07 19:00:11"},
    {"position":"268","date":"2024-08-07 19:00:11"},
    {"position":"267","date":"2024-08-07 20:00:13"},
    {"position":"267","date":"2024-08-07 21:00:11"},
    {"position":"267","date":"2024-08-07 21:00:11"},
    {"position":"267","date":"2024-08-07 22:00:11"},
    {"position":"267","date":"2024-08-07 23:00:11"}
]

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['position'] = df['position'].astype(int)

df = df.sort_values('date')

max_position = df['position'].max()
min_position = df['position'].min()

first_max_date = df[df['position'] == max_position]['date'].iloc[0]

min_position_after_max = df[(df['position'] == min_position) & (df['date'] > first_max_date)]

if not min_position_after_max.empty:
    last_min_date = min_position_after_max['date'].iloc[-1]


    time_diff_hours = (last_min_date - first_max_date).total_seconds() / (60 * 60)

    days = int(time_diff_hours // 24)
    hours = int(time_diff_hours % 24)

    position_diff = max_position - min_position

    if days > 0:
        average_positions_per_day = position_diff / days
    else:
        average_positions_per_day = position_diff

    average_positions_per_month = average_positions_per_day * 30

    last_position = df['position'].iloc[-1]
    positions_to_1 = last_position - 1

    days_to_1 = positions_to_1 / average_positions_per_day
    months_to_1 = days_to_1 / 30
    weeks_to_1 = days_to_1 / 7

    full_months = int(months_to_1)
    remaining_weeks = (months_to_1 - full_months) * 4.33

    print(f"A posição mais alta ({max_position}) ocorreu em {first_max_date}")
    print(f"A última posição mais baixa ({min_position}) ocorreu em {last_min_date}")
    print(f"Tempo para ir da posição máxima para a última mínima: {days} dias e {hours} horas")
    print(f"Diferença entre as posições: {position_diff}")
    print(f"Média de posições por dia: {average_positions_per_day:.2f}")
    print(f"Média de posições por mês: {average_positions_per_month:.2f}")
    print(f"Tempo estimado para chegar à posição 1: {days_to_1:.2f} dias ou {months_to_1:.2f} meses")
    print(f"Isso é aproximadamente {full_months} meses e {remaining_weeks:.2f} semanas")
else:
    print("Não há transições da posição máxima para a mínima nos dados fornecidos.")
