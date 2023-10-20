import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime as dt

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', lambda x: '%.1f' % x)
rcParams['figure.figsize'] = 11, 7


water_mortality_corr_data = pd.read_csv('files/water.csv', index_col='Index')

mort = water_mortality_corr_data['mortality']
hardness = water_mortality_corr_data['hardness']
hardness_shape = water_mortality_corr_data[['hardness']]


# АНАЛИЗ ВСЕГО ОБЪЕМА ДАННЫХ, ПРОСЛЕЖИВАЕТСЯ ДОСТАТОЧНО СИЛЬНАЯ ЛИНЕЙНАЯ КОРРЕЛЯЦИЯ

# pearson_corr = water_mortality_corr_data[['hardness', 'mortality']].corr('pearson')
# spearman_corr = water_mortality_corr_data[['hardness', 'mortality']].corr('spearman')


# КОЭФФИЦИЕНТ КОРРЕЛЯЦИИ СПИРМАНА РАВЕН 0,7

# a, b = np.polyfit (hardness, mort, 1)
#
# fig = plt.figure()
# axes = fig.add_axes([.1, .1, .8, .8])
# axes.scatter(hardness, mort)
# axes.set_xlabel('Жесткость воды')
# axes.set_ylabel('Смертность')
# axes.set_title('Корреляция между жесткостью воды и смертностью')
# axes.plot (hardness, a * hardness + b)
# plt.show()


# 3.23
# 1676.36


# print(pearson_corr)
# print(spearman_corr)


# ---------------  SCIKIT-LEARN LINEAR REGRESSION MODEL:  --------------------

# x_train, x_test, y_train, y_test = train_test_split(hardness_shape, mort, test_size=0.30, random_state=42)

# x_train.shape
# y_train.shape
#
#
# model = LinearRegression()
# model.fit(x_train, y_train)
#
# LinearRegression()

# print(model.coef_)
# print(model.intercept_)


# y_pred = model.predict(x_test)


# df_pred_and_test = pd.DataFrame()
# df_pred_and_test['predicted'] = y_pred
# df_pred_and_test['test'] = np.array(y_test)

# print(df_pred_and_test)

# print(model.score(x_test, y_test))   # КОЭФФИЦИЕНТ ДЕТЕРМИНАЦИИ


# --------------- АЛЬТЕРНАТИВНЫЙ МЕТОД С ИСПОЛЬЗОВАНИЕМ STATSMODELS: ----------------------

# x_const = sm.add_constant(x_train)

# print(x_const)

# model_sm = sm.OLS(y_train, x_const)
# results = model_sm.fit()
# print(results.summary())
#
# print('PARAMS: ', results.params)
#
# print(results.rsquared)
#
# plt.scatter(x_const.iloc[:, 1], results.resid)
# plt.show()













# РАЗДЕЛЕНИЕ ДАННЫХ НА ЮГ И СЕВЕР:


# ------------ СЕВЕРНЫЕ ДАННЫЕ: -----------------

# north_mort = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'North']['mortality']
# north_hardness = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'North']['hardness']
# north_hardness_shape = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'North'][['hardness']]
#
# x1_train, x1_test, y1_train, y1_test = train_test_split(north_hardness_shape, north_mort, test_size=0.30, random_state=42)
#
# x1_const = sm.add_constant(x1_train)
#
# model_sm1 = sm.OLS(y1_train, x1_const)
# results1 = model_sm1.fit()
# print(results1.summary())
#
# print('PARAMS: ', results1.params)
#
# print(results1.rsquared)
#
# plt.scatter(x1_const.iloc[:, 1], results1.resid)
# plt.show()


# ----------------- ЮЖНЫЕ ДАННЫЕ: -----------------------------------
#
# south_mort = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'South']['mortality']
# south_hardness = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'South']['hardness']
# south_hardness_shape = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'South'][['hardness']]
#
# x2_train, x2_test, y2_train, y2_test = train_test_split(south_hardness_shape, south_mort, test_size=0.30, random_state=42)
#
# x2_const = sm.add_constant(x2_train)
#
# model_sm2 = sm.OLS(y2_train, x2_const)
# results2 = model_sm2.fit()
# print(results2.summary())
#
# print('PARAMS: ', results2.params)
#
# print(results2.rsquared)
#
# plt.scatter(x2_const.iloc[:, 1], results2.resid)
# plt.show()
#
# fig, axes = plt.subplots(nrows=1, ncols=2)
# axes[0].scatter(north_hardness, north_mort)
# axes[0].set_xlabel('Жесткость воды')
# axes[0].set_ylabel('Смертность')
# axes[0].set_title('Корреляция между жесткостью \n воды и смертностью \n в северных регионах')
#
# axes[1].scatter(south_hardness, south_mort)
# axes[1].set_xlabel('Жесткость воды')
# axes[1].set_ylabel('Смертность')
# axes[1].set_title('Корреляция между жесткостью \n воды и смертностью \n в южных регионах')
# plt.show()
#
# north_pearson = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'North'][['hardness', 'mortality']].corr('pearson')
# north_spearman = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'North'][['hardness', 'mortality']].corr('spearman')
#
# south_pearson = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'South'][['hardness', 'mortality']].corr('pearson')
# south_spearman = water_mortality_corr_data.loc[water_mortality_corr_data['location'] == 'South'][['hardness', 'mortality']].corr('spearman')
#
# print(north_pearson)
# print(north_spearman)
#
# print('\n')
#
# print(south_pearson)
# print(south_spearman)