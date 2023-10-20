import pandas as pd
import numpy as np

# Ищем:
#
# max()
# min()
# range = max() - min()
# mean()
# count()
# mode:
# Выбросы, среднее значение до и после удаления выбросов
# Пропуски в абсолютных значениях и в процентах, статистика до и после удаления пропусков
# Заполнение пропусков средним значением, медианой, модой, удаление столбцов с слишком большим количеством пропусков
# Модой можно заполнять категориальные значения (номер каюты, ответы да/нет и тд)
# Можно заменить медианой по полу




horse_health_raw = pd.read_csv('ml-latest/horse_data.csv')
# horse_health_raw = pd.read_csv('https://raw.githubusercontent.com/obulygin/pyda_homeworks/master/statistics_basics/horse_data.csv')
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

horses_health_data = pd.DataFrame(horse_health_raw)
horses_health_data.columns = cols

horses_health_data = horses_health_data[['surgery', 'age', 'rectal_temperature', 'pulse', 'respiratory_rate',
                                         'temperature_of_extremities', 'pain', 'outcome']].replace('?', np.nan)

horses_health_data['rectal_temperature'] = horses_health_data['rectal_temperature'].astype(float)

# Ручной подсчет моды:
# Создаем пустой словарь в котором считаем количество появлений значений ректальной температуры

rect_temp_data = horses_health_data['rectal_temperature']
rect_temp_counts = {}
for rtemp in rect_temp_data.values:
    if rtemp not in rect_temp_counts:
        rect_temp_counts[rtemp] = 1
    else:
        rect_temp_counts[rtemp] += 1

    if np.isnan(rtemp):
        del rect_temp_counts[rtemp]

# Проходимся по словарю и ищем макс кол-во повторений

max_rect_temp_count = 0
mode_rect_temp = None

for k, v in rect_temp_counts.items():
    if max_rect_temp_count < v:
        max_rect_temp_count = v
        mode_rect_temp = k


# Ручной подсчет медианы:

sorted_rect_temp_counts = sorted(rect_temp_counts)
len_rect_temp_counts = len(rect_temp_counts)

middle = len_rect_temp_counts // 2

if len_rect_temp_counts % 2 == 0:
    result = round((sorted_rect_temp_counts[middle - 1] + sorted_rect_temp_counts[middle]) / 2, 2)
else:
    result = round(sorted_rect_temp_counts[middle], 2)

# print(result)
#
# print(rect_temp_data.median())




# print(f'Значение моды: {mode_rect_temp}, количество встречаемости: {max_rect_temp_count}')
# print('Mode: ', horses_health_data['rectal_temperature'].mode()[0])

# print(horses_health_data)
# print(rect_temp_counts)

# print(rect_temp_data.describe())


# Поиск выбросов:

q1 = rect_temp_data.quantile(0.25)
q3 = rect_temp_data.quantile(0.75)

iqr = q3-q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

print(lower_bound, upper_bound)

remove_outliers = horses_health_data[horses_health_data['rectal_temperature'].between(lower_bound, upper_bound, inclusive='both')]

print(remove_outliers)
print(horses_health_data[~horses_health_data['rectal_temperature'].between(lower_bound, upper_bound, inclusive='both')])
