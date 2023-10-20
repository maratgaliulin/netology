import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', lambda x: '%.1f' % x)




iris = load_iris()

iris_data = pd.DataFrame(iris['data'], columns=iris['feature_names'])
iris_data = iris_data.loc[:, ['sepal length (cm)', 'sepal width (cm)']]

iris_target = iris['target']

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.25, random_state=43)


lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_predict = lr.predict(X_test)
lr_predict_proba = lr.predict_proba(X_test)

print(lr_predict)
print(lr_predict_proba)
print(accuracy_score(y_test, lr_predict))



# ------------------   ТРЕНИРОВОЧНЫЙ ГРАФИК:  ------------------------

# plt.scatter(x=X_train['sepal length (cm)'], y=X_train['sepal width (cm)'], c=y_train)


# Сетка:
# nx, ny = 200, 100
# x_min, x_max = plt.xlim()
# y_min, y_max = plt.ylim()
# xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx),
#                      np.linspace(y_min, y_max, ny))

# Предсказание класса каждой точки сетки:
# Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)

# Закрашивание классов разными цветами:
# plt.pcolormesh(xx, yy, Z, cmap='Pastel1', zorder=-1)
#
# plt.show()


# ---------------------  ТЕСТОВЫЙ ГРАФИК: ----------------------

# plt.scatter(x=X_test['sepal length (cm)'], y=X_test['sepal width (cm)'], c=lr.predict(X_test))
# plt.title('LOGISTIC REGRESSION')
# nx, ny = 2000, 1000
# x_min, x_max = plt.xlim()
# y_min, y_max = plt.ylim()
# xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx),
#                      np.linspace(y_min, y_max, ny))
#
# Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
#
# plt.pcolormesh(xx, yy, Z, cmap='Pastel2', zorder=-1)
#
# plt.show()



