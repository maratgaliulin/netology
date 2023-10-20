import pandas as pd
import numpy as np

# cbr_data = pd.read_html('https://cbr.ru/key-indicators/')[2]

# print(cbr_data)


d = {'price': pd.Series([1,2,3], index=['v1', 'v2', 'v3']), 'count': pd.Series([12,13,15], index=['v1', 'v2', 'v3'])}
df1 = pd.DataFrame(d)
# print(df1)

d2 = {'price': np.array([1,2,3]), 'count': np.array([4,5,6])}

df2 = pd.DataFrame(d2, index=['v1', 'v2', 'v3'])

# print(df2)

d = {'price': np.array([1,2,3]), 'count': np.array([10, 20, 30])}
df = pd.DataFrame(d, index=['a', 'b', 'c'])

# print(df)

"""Выбор столбца: """
# print(df['count'])

"""Выбор строки по метке: """
# print(df.loc['a'])

"""Выбор строки по индексу: """
# print(df.iloc[1])

"""Срез по строкам: """
# print(df[0:2])

"""Выбор строк по условию: """
print(df[df['count'] >= 20])