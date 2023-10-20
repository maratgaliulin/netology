import pandas as pd

data = pd.read_csv('ml-latest/power.csv')

"""Выводит уникальные значения из столбцов в виде списка"""
# print(data.category.unique())

"""Выводит длину списка уникальных значений из столбца"""
# print(data.category.nunique())

"""Выводит количество значений определенного элемента: """
# print(data.category.value_counts().head(5))

"""Выводит процентное количество значений определенного элемента: """
# print(data.category.value_counts(normalize=True).head())


"""Фильтрация строк с потреблением энергии выше среднего (из файла power.csv): """

# Находим среднее арифметическое столбца quantity:
# power_mean = data.quantity.mean()

# Делаем строку условие - количество больше среднего арифметического:
# condition = f'quantity > {power_mean}'

# Фильтруем данные при помощи метода query():
# filtered_data = data.query(condition).head()

# Либо фильтруем данные в квадратных скобках:
# filtered_data = data[data.quantity > power_mean].head()

# Выводим на печать:
# print(filtered_data)


"""Фильтрация по содержанию фрагмента строки в столбце: """

# Более обобщенный поиск с широкими условиями:
# filtered_country_data = data[data['country'].str.contains('us', case=False)]['country'].unique()
# print(filtered_country_data)

# Более конкретизированный поиск с несколькими условиями:
# filtered_country_data = data[(data['country'] == 'Russian Federation') | (data['country'] == 'Belarus')]
#
# print(filtered_country_data.head())


"""Фильтрация по номерам строк: """

# data_filtered_by_number = data.loc[1000:1005]
#
# print(data_filtered_by_number)