import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

from pylab import rcParams
rcParams['figure.figsize'] = 11,7

df = pd.read_csv('https://raw.githubusercontent.com/obulygin/pyda_homeworks/master/stat_case_study/vgsales.csv')
# print(df.head())



df['User_Score'] = df['User_Score'].replace('tbd', np.NaN)

df['User_Score'] = df['User_Score'].astype('float64')
df['Year_of_Release'] = df['Year_of_Release'].astype('Int64')
df['User_Count'] = df['User_Count'].astype('Int64')
df['Critic_Count'] = df['Critic_Count'].astype('Int64')

df['User_Score'] = df['User_Score'] * 10

dynamics_by_region = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release']].groupby('Year_of_Release').sum()



# Обычные линейные графики



# print(dynamics_by_region)
# print(dynamics_by_region.describe())

# plt.plot(dynamics_by_region.index, dynamics_by_region[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']], label=['Северная Америка', 'Еврозона', 'Япония', 'Другие страны', 'Глобальные продажи'])
# plt.title('Динамика продаж видеоигр')
# plt.xlabel('Год')
# plt.ylabel("Продажи, млн.")
# plt.text(2008, (df[['Global_Sales', 'Year_of_Release']].groupby('Year_of_Release').sum().loc[2007][0] + 50),  f"{df[['Global_Sales', 'Year_of_Release']].groupby('Year_of_Release').sum().loc[2008][0]}, Почему падение \n       началось отсюда?")
# plt.legend(loc='upper left')
# plt.show()


# Свечной график (box chart)


# dynbyreg = dynamics_by_region[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]

# fig, ax = plt.subplots()
# VP = ax.boxplot(dynamics_by_region, widths=0.5, patch_artist=True,
#                 showmeans=False, showfliers=False,
#                 medianprops={"color": "white", "linewidth": 0.5},
#                 boxprops={"facecolor": "C0", "edgecolor": "white",
#                           "linewidth": 1.5},
#                 whiskerprops={"color": "C0", "linewidth": 1.5},
#                 capprops={"color": "C0", "linewidth": 1.5})
#
# ax.set(xlim=(0, 5), xticks=(np.arange(1, 7)),
#        ylim=(0, 700), yticks=np.arange(0, 700, 50))
# xtickNames = plt.setp(ax, xticklabels=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', ''])
# plt.setp(xtickNames, rotation=45, fontsize=8)
#
# plt.show()


# Линейные графики с закрашенной площадью:

# x = dynamics_by_region.index
# y = dynamics_by_region.drop('Global_Sales', axis=1)[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

# fig, ax = plt.subplots()
# ax.fill(x, y, alpha=.5, linewidth=0)
# ax.plot(x,y, label=['Северная Америка', 'Еврозона', 'Япония', 'Другие страны'])
# plt.title('Динамика продаж видеоигр')
# plt.xlabel('Год')
# plt.ylabel("Продажи, млн.")
# plt.legend(loc='upper left')
# plt.show()



# Гистограмма:

# x = df['User_Score']
# n, bins, patches = plt.hist(x, bins=50, alpha=0.75)
# plt.title('Распределение оценок пользователей')
# plt.xlabel('Оценка')
# plt.ylabel("Частота")
# plt.show()

# x = df['Critic_Score']
# n, bins, patches = plt.hist(x, bins=50, alpha=0.75)
# plt.title('Распределение оценок пользователей')
# plt.xlabel('Оценка')
# plt.ylabel("Частота")
# plt.show()


x = df[['Critic_Score', 'User_Score']]
plt.hist(x, bins=20, alpha=0.75, label=['Critic_Score', 'User_Score'], stacked=False)
plt.title('Распределение оценок пользователей')
plt.xlabel('Оценка')
plt.ylabel("Частота")
plt.legend(loc='upper left')
plt.show()