import pandas as pd

def watcher(param):
    """Мне только посмотреть"""
    return param == 0

def conversion(row):
    """Подсчет конверсий переходов в покупки"""
    return row['orders'] / row['clicks']

df = pd.DataFrame({'user_id': [1, 2, 3], 'clicks': [163, 130, 97], 'orders': [2, 4, 0]})

df['watcher'] = df['orders'].apply(watcher)
df['conversion'] = df.apply(conversion, axis=1)


print(df)