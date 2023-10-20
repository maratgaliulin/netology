import pandas as pd
import numpy as np
import pandas.core.series

horses_health = pd.read_csv('https://raw.githubusercontent.com/obulygin/pyda_homeworks/master/statistics_basics/horse_data.csv')

# 1) НАЗВАНИЯ СТОЛБЦОВ:

cols = [
    'surgery',
    'age',
    'hospital_number',
    'rectal_temperature',
    'pulse',
    'respiratory_rate',
    'temperature_of_extremities',
    'peripheral_pulse',
    'mucous_membranes',
    'capill_refill_time',
    'pain',
    'peristalsis',
    'abdom_distension',
    'nasogastric_tube',
    'nasogastric_reflux',
    'nasogast_reflux_ph',
    'rectal_exam_feces',
    'abdomen',
    'packed_cell_vol',
    'total_protein',
    'abdomenocentesis_appearance',
    'abdomenocenteses_total_protein',
    'outcome',
    'surgical_lesion',
    'lesion_site',
    'lesion_type',
    'lesion_subtype',
    'cp_data'
]


horses_health_data = pd.DataFrame(horses_health)
horses_health_data.columns = cols



horses_health_data_copy = horses_health_data[['surgery', 'age', 'rectal_temperature', 'pulse', 'respiratory_rate',
                                         'temperature_of_extremities', 'pain', 'outcome']].replace('?', np.nan)

working_horses_health_data = horses_health_data_copy.copy()




# 2) АНАЛИЗ ПРОПУСКОВ:

# Общая информация по непропущенным строкам:
# print(working_horses_health_data.info())

# Количество пропущенных строк:
# print(working_horses_health_data.isna().sum())

# Процент пропусков:
# print((working_horses_health_data.isna().mean() * 100).round(2))



# 3) РАБОТА С ПРОПУСКАМИ:

# Так как нам вероятно в последующем необходимо проанализировать зависимость исхода лечения от тех или иных параметров, нам не нужны строки, в которых исход неизвестен.
# Тем более что такая строка всего одна:

working_horses_health_data.dropna(subset='outcome', inplace=True)

# Когда я убрал строку с неизвестным исходом, автоматически скорректировались данные по лечению (хирургическое / консервативное), там также был 1 пропуск данных; из этого
# можно сделать вывод, что это была одна и та же строка (лечение неизвестно и исход неизвестен).

# а) Номинальные данные (surgery, temperature of extremities, pain, outcome):

# Из номинальных данных, которые нас интересуют (которые мы должны были оставить согласно ДЗ), остались столбцы Температура Конечностей и Боль (степень выраженности болевого синдрома) - в surgery, age, outcome пропусков нет.
# В обоих столбцах процент пропусков около 19%. Можно конечно заменить недостающие данные Модой, но думаю это сильно исказит статистику по зависимости исхода лечения от этих параметров.
# Поэтому решил удалить строки, в которых данные из этих столбцов отсутствуют:

working_horses_health_data.dropna(subset='temperature_of_extremities', inplace=True)
working_horses_health_data.dropna(subset='pain', inplace=True)

# Заменяем 9 на 2 в столбце age (см.ниже):
working_horses_health_data['age'].replace(9, 2, inplace=True)

# б) Непрерывные данные (rectal temperature, pulse, respiratory rate). Планировал сгруппировать лошадей по age, temperature of extremities, pain, и заполнить пропуски в rectal temperature, pulse, resp.rate соответствующими Медианами (с предположением что у лошадей схожего возраста, температурой конечностей и степенью выраженности болевого синдрома медиана вероятно будет схожей)
# Однако при включении temperature of extremities в группировку появлялась ошибка, в связи с чем убрал эту категорию из группировки (сгруппировал только по возрасту и выраженности болевого синдрома)

fill_median_horses_data = working_horses_health_data.copy()

fill_median_horses_data['rectal_temperature'] = fill_median_horses_data['rectal_temperature'].fillna(working_horses_health_data.groupby(['age', 'pain'])['rectal_temperature'].transform('median'))
fill_median_horses_data['pulse'] = fill_median_horses_data['pulse'].fillna(working_horses_health_data.groupby(['age', 'pain'])['pulse'].transform('median'))
fill_median_horses_data['respiratory_rate'] = fill_median_horses_data['respiratory_rate'].fillna(working_horses_health_data.groupby(['age', 'pain'])['respiratory_rate'].transform('median'))

# print(working_horses_health_data.groupby(['age', 'pain'])['rectal_temperature'].median()) # - проверка значений медиан

# print((fill_median_horses_data.isna().mean() * 100).round(2))   # - проверка отсутствия пропусков


# print(working_horses_health_data.info())

# Для анализа осталось 222 строки из 299, или 74 процента данных

# Функция, подсчитывающая количество и процент встретившихся значений номинальных переменных, и склеивающая значения с соответствующим словарем

def nominal_values_base_stats(data_value_counts: pandas.core.series.Series, data_dict: dict):
    final_outcome = {}
    data_value_counts_sum = data_value_counts.sum()
    for k, v in data_dict.items():
        for i in range(len(data_value_counts)):
            if int(data_value_counts.index.tolist()[i]) == k:
                final_outcome[v] = {
                    'Абсолютное количество': data_value_counts[data_value_counts.index.tolist()[i]],
                    'Процент': round(
                        (data_value_counts[data_value_counts.index.tolist()[i]] / data_value_counts_sum * 100), 2)
                }
    for k, v in final_outcome.items():
        print(k, ':')
        for key, val in v.items():
            print(' ', key, ':', val)
    print('')


# Value_counts Series и словари расшифровки индексов значений - для вставки в функцию nominal_values_base_stats:

#  1) Surgery:

surgery = {
    1: 'Хирургическое лечение',
    2: 'Консервативное лечение'
}
surgery_values = fill_median_horses_data['surgery'].value_counts()

# 2) Age:

# NB!: в описании столбца говорится что 1 означает взрослую лошадь, а 2 - молодую, однако в столбце не оказалось ни одной двойки, вместо нее были девятки
# Не уверен, как необходимо интерпретировать такие данные, напрашиваются 2 варианта:
# 1) предположить что девятки были выставлены ошибочно вместо двоек, и заменить девятки двойками
# 2) убрать данный столбец из анализа, так как данные ненадежны.
# Если исходить из первого варианта, то получится следующее:

# working_horses_health_data['age'].replace(9, 2, inplace=True) - замена 9 на 2 (сделано выше для более корректного отображения строк по замене пропусков температуры, пульса и частоты дыхания медианами

age = {
    1: 'Взрослая лошадь',
    2: 'Молодая лошадь (< 6 месяцев)'
}
age_values = fill_median_horses_data['age'].value_counts()

# 3) Temperature of extremities:

temp_of_extremities = {
    1: 'Нормальная температура конечностей',
    2: 'Конечности теплые',
    3: 'Конечности прохладные',
    4: 'Конечности холодные'
}
temp_extr_values = fill_median_horses_data['temperature_of_extremities'].value_counts()

# 4) Pain:

pain = {
    1: 'В ясном сознании, боли нет',
    2: 'Животное угнетено',
    3: 'Преходящая легкая боль',
    4: 'Преходящая сильная боль',
    5: 'Постоянная сильная боль'
}
pain_values = fill_median_horses_data['pain'].value_counts()

# 5) Outcome:

outcome = {
    1: 'Животное выжило',
    2: 'Животное погибло',
    3: 'Животное было подвергнуто эфтаназии'
}
outcome_values = fill_median_horses_data['outcome'].value_counts()

# Данные о количестве и процентном соотношении встретившихся номинальных значений - surgery, age, rectal_temperature, pulse, respiratory_rate, temperature_of_extremities, pain, outcome (как результат работы функции nominal_values_base_stats):

nominal_values_base_stats(surgery_values, surgery)
nominal_values_base_stats(age_values, age)
nominal_values_base_stats(temp_extr_values, temp_of_extremities)
nominal_values_base_stats(pain_values, pain)
nominal_values_base_stats(outcome_values, outcome)

# 6) Непрерывные данные:

#  a) Базовые стат параметры:

print(fill_median_horses_data[['rectal_temperature', 'pulse', 'respiratory_rate']].astype(float).describe(), '\n')

print('Значения медианы для непрерывных данных:')
print(fill_median_horses_data[['rectal_temperature', 'pulse', 'respiratory_rate']].astype(float).median(), '\n')

print('Значения моды для непрерывных данных:')
print(fill_median_horses_data[['rectal_temperature', 'pulse', 'respiratory_rate']].astype(float).mode(), '\n')

print('Значения дисперсии для непрерывных данных:')
print((fill_median_horses_data[['rectal_temperature', 'pulse', 'respiratory_rate']].astype(float).std()) ** 2, '\n')

# б) Функция для расчета выбросов:

def outliers_detector(data_with_outliers: pandas.core.frame.DataFrame, column_name: str):
    q1 = data_with_outliers[column_name].astype(float).quantile(0.25)
    q3 = data_with_outliers[column_name].astype(float).quantile(0.75)
    iqr = q3 - q1
    lower_bond = q1 - (1.5 * iqr)
    upper_bond = q3 + (1.5 * iqr)
    remove_outliers = data_with_outliers[data_with_outliers[column_name].astype(float).between(lower_bond, upper_bond, inclusive='both')]
    print(column_name, ':')
    print(remove_outliers[column_name], '\n')

# Применение функции для удаления выбросов:

print("Данные без выбросов: \n")

outliers_detector(fill_median_horses_data, 'rectal_temperature')
outliers_detector(fill_median_horses_data, 'pulse')
outliers_detector(fill_median_horses_data, 'respiratory_rate')







