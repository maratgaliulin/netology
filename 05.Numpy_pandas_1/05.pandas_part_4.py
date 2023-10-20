import pandas as pd

data = pd.read_csv('ml-latest/power.csv')
"""Сортировка по количеству восходящее (еще я добавил условие по стране - Украина)"""
# print(data[data.country == 'Ukraine'].sort_values(by='quantity', ascending=False))
# print('---------------')
#
# print(data[data.country == 'Ukraine'][['country', 'quantity']].groupby('country').sum())

"""Сортировка по нескольким столбцам: """

data.sort_values(by=['year', 'country', 'quantity'], ascending=[False, True, False], inplace=True)

print(data)