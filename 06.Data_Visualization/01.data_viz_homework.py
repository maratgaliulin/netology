import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns
from datetime import datetime as dt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', lambda x: '%.1f' % x)
rcParams['figure.figsize'] = 11,7

# index_data = pd.read_csv('files/indexData.csv')[['Index', 'Date', 'Volume']]
#
# index_data['Date_mod'] = index_data.apply(lambda row: int(row['Date'].split('-')[0]), axis=1)
# index_data['Volume'] = index_data['Volume'].astype('float64')
#
# index_data = index_data.loc[index_data['Date_mod'] > 1995]
#
# index_data_groupped = index_data.groupby(['Index', 'Date_mod']).median(numeric_only=True).round(2)
#
# pt = pd.pivot_table(index_data_groupped, index='Date_mod', columns='Index')

# ---------------------  ЛИНЕЙНЫЕ ГРАФИКИ  ---------------------

# plt.plot(pt['Volume'])
# plt.title('Динамика роста среднего дневного объема \n основных биржевых ETF рынка США')
# plt.legend(pt['Volume'].columns)
# plt.show()

# ---------------------  АНАЛИЗ ДАННЫХ ИЗ ПРЕДЫДУЩЕГО ДЗ (об исходах лечения лошадей) ---------------------


# horses_health = pd.read_csv('files/horse_data.csv')
#
# cols = [
#     'surgery',
#     'age',
#     'hospital_number',
#     'rectal_temperature',
#     'pulse',
#     'respiratory_rate',
#     'temperature_of_extremities',
#     'peripheral_pulse',
#     'mucous_membranes',
#     'capill_refill_time',
#     'pain',
#     'peristalsis',
#     'abdom_distension',
#     'nasogastric_tube',
#     'nasogastric_reflux',
#     'nasogast_reflux_ph',
#     'rectal_exam_feces',
#     'abdomen',
#     'packed_cell_vol',
#     'total_protein',
#     'abdomenocentesis_appearance',
#     'abdomenocenteses_total_protein',
#     'outcome',
#     'surgical_lesion',
#     'lesion_site',
#     'lesion_type',
#     'lesion_subtype',
#     'cp_data'
# ]


# ПРЕДВАРИТЕЛЬНАЯ ПОДГОТОВКА ФАЙЛА horse_data_clean.csv:

# horses_health_data = pd.DataFrame(horses_health)
# horses_health_data.columns = cols
#
# horses_health_data_copy = horses_health_data[['surgery', 'age', 'rectal_temperature', 'pulse', 'respiratory_rate',
#                                          'temperature_of_extremities', 'pain', 'outcome']].replace('?', np.nan)
#
# working_horses_health_data = horses_health_data_copy.copy()
#
# working_horses_health_data['surgery'] = working_horses_health_data['surgery'].astype('Int64')
# working_horses_health_data['rectal_temperature'] = working_horses_health_data['rectal_temperature'].astype('float64')
# working_horses_health_data['pulse'] = working_horses_health_data['pulse'].astype('Int64')
# working_horses_health_data['respiratory_rate'] = working_horses_health_data['respiratory_rate'].astype('Int64')
# working_horses_health_data['temperature_of_extremities'] = working_horses_health_data['temperature_of_extremities'].astype('Int64')
# working_horses_health_data['pain'] = working_horses_health_data['pain'].astype('Int64')
# working_horses_health_data['outcome'] = working_horses_health_data['outcome'].astype('Int64')
#
# working_horses_health_data.dropna(subset='outcome', inplace=True)
# working_horses_health_data.dropna(subset='temperature_of_extremities', inplace=True)
# working_horses_health_data.dropna(subset='pain', inplace=True)
# working_horses_health_data['age'].replace(9, 2, inplace=True)
#
# fill_median_horses_data = working_horses_health_data.copy()
#
# fill_median_horses_data['rectal_temperature'] = fill_median_horses_data['rectal_temperature'].fillna(working_horses_health_data.groupby(['age', 'pain'])['rectal_temperature'].transform('median'))
# fill_median_horses_data['pulse'] = fill_median_horses_data['pulse'].fillna(working_horses_health_data.groupby(['age', 'pain'])['pulse'].transform('median'))
# fill_median_horses_data['respiratory_rate'] = fill_median_horses_data['respiratory_rate'].fillna(working_horses_health_data.groupby(['age', 'pain'])['respiratory_rate'].transform('median'))
#
# fill_median_horses_data.to_csv('files/horse_data_clean.csv', index=False)
#
# print(fill_median_horses_data.head())
# print(fill_median_horses_data.info())


horse_data = pd.read_csv('files/horse_data_clean.csv')

print(horse_data.head())

# print(horse_data.info())


# ---------------------   HEATMAP  -----------------------------

# pain = {
#     1: 'В ясном сознании, боли нет',
#     2: 'Животное угнетено',
#     3: 'Преходящая легкая боль',
#     4: 'Преходящая сильная боль',
#     5: 'Постоянная сильная боль'
# }
#
# outcome = {
#     1: 'Животное выжило',
#     2: 'Животное погибло',
#     3: 'Животное было подвергнуто эфтаназии'
# }
#
# pain_data = horse_data.copy()[['pain', 'outcome']]
#
# for k, v in pain.items():
#     pain_data.loc[pain_data['pain'] == k, 'pain_val'] = v
#
# for k, v in outcome.items():
#     pain_data.loc[pain_data['outcome'] == k, 'outcome_val'] = v
#
#
#
# pain_pivot_table = pd.pivot_table(pain_data[['pain', 'pain_val', 'outcome_val']], sort=['pain'].sort(), index='pain_val', columns='outcome_val', aggfunc=np.count_nonzero)
#
# # print(pain_pivot_table['pain'])
#
# sns.heatmap(pain_pivot_table['pain'], annot=True)
# plt.show()

# ---------------------  BOXPLOT  ---------------------



# fig, ax = plt.subplots()

# ax.tick_params(axis = 'both',    #  Применяем параметры к обеим осям
#                which = 'major',    #  Применяем параметры к основным делениям
#                direction = 'inout',    #  Рисуем деления внутри и снаружи графика
#                length = 20,    #  Длинна делений
#                width = 4,     #  Ширина делений
#                color = 'm',    #  Цвет делений
#                pad = 10,    #  Расстояние между черточкой и ее подписью
#                labelsize = 15,    #  Размер подписи
#                labelcolor = 'r',    #  Цвет подписи
#                bottom = True,    #  Рисуем метки снизу
#                top = True,    #   сверху
#                left = True,    #  слева
#                right = True,    #  и справа
#                labelbottom = True,    #  Рисуем подписи снизу
#                labeltop = True,    #  сверху
#                labelleft = True,    #  слева
#                labelright = True,    #  и справа
#                labelrotation = 45)

# ax.tick_params(
#     axis='x',
#     labelcolor='w'
# )
# sns.boxplot(horse_data['rectal_temperature'])
# plt.xlabel('Rectal temperature')
# plt.show()

# ------------------  SCATTERPLOT MATRIX  -----------------------

# sns.pairplot(horse_data[['rectal_temperature', 'respiratory_rate', 'pulse']])
# plt.show()


# ------------------   LINE CHARTS   ------------------

# sns.set_theme()
# plt.plot(horse_data['rectal_temperature'])
# plt.legend(['rectal_temperature'])
# plt.show()

# plt.plot(horse_data['pulse'])
# plt.legend(['pulse'])
# plt.show()

# plt.plot(horse_data['respiratory_rate'])
# plt.legend(['respiratory_rate'])
# plt.show()


# --------------------  HISTOGRAM  -------------------------

# sns.set_theme()
# plt.hist(horse_data['rectal_temperature'], bins=30)
# plt.legend(['rectal_temperature'])
# plt.show()

# plt.hist(horse_data['respiratory_rate'], bins=20)
# plt.legend(['respiratory_rate'])
# plt.show()