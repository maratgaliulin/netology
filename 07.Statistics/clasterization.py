import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist
from scipy.cluster import hierarchy

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.float_format', lambda x: '%.1f' % x)
# rcParams['figure.figsize'] = 11, 7



# Возьмите датасет с цветками iris’а (функция load_iris из библиотеки sklearn)
# Оставьте два признака -sepal_length и sepal_width и целевую переменную - variety
# Разделите данные на выборку для обучения и тестирования
# Постройте модель LDA
# Визуализируйте предсказания для тестовой выборки и центры классов
# Отбросьте целевую переменную и оставьте только два признака - sepal_length и sepal_width
# Подберите оптимальное число кластеров для алгоритма kmeans и визуализируйте полученную кластеризацию

iris = load_iris()

iris_data = pd.DataFrame(iris['data'], columns=iris['feature_names'])
iris_data = iris_data.loc[:, ['sepal length (cm)', 'sepal width (cm)']]

iris_target = iris['target']

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.25, random_state=43)

# print(X_train.shape, X_test.shape)

lda = LinearDiscriminantAnalysis()

lda.fit(X_train, y_train)

# print(lda.predict(X_test))

res = pd.DataFrame([y_test, lda.predict(X_test)]).T

predict_accuracy = accuracy_score(y_test, lda.predict(X_test))

# print('PREDICT ACCURACY: ', predict_accuracy)
# print('LDA COEFFICIENT:', lda.coef_)
# print('MEANS: ', lda.means_)

print(res)


# 1) Тренировочные данные:

# Точечный график:
# plt.scatter(x=X_train['sepal length (cm)'], y=X_train['sepal width (cm)'], c=y_train)

# Центры классов:
# plt.scatter(lda.means_[:, 0], lda.means_[:, 1], c='r', s=150, marker='*')

# Сетка:
# nx, ny = 200, 100
# x_min, x_max = plt.xlim()
# y_min, y_max = plt.ylim()
# xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx),
#                      np.linspace(y_min, y_max, ny))

# Предсказание класса каждой точки сетки:
# Z = lda.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)

# Закрашивание классов разными цветами:
# plt.pcolormesh(xx, yy, Z, cmap='Pastel1', zorder=-1)
#
# plt.show()



# Тестовые данные:

# plt.scatter(x=X_test['sepal length (cm)'], y=X_test['sepal width (cm)'], c=lda.predict(X_test))
# plt.title('LINEAR REGRESSION')
# plt.scatter(lda.means_[:, 0], lda.means_[:, 1], c='r', s=150, marker='*')
# nx, ny = 2000, 1000
# x_min, x_max = plt.xlim()
# y_min, y_max = plt.ylim()
# xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx),
#                      np.linspace(y_min, y_max, ny))
#
# Z = lda.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
#
# plt.pcolormesh(xx, yy, Z, cmap='Pastel2', zorder=-1)
#
# plt.show()



# ---------------------- КЛАСТЕРИЗАЦИЯ: ------------------------------

scaler = StandardScaler()

x_scaled = scaler.fit_transform(X_train)

# print('SCALED: ', x_scaled)
#
# plt.scatter(x=x_scaled[:, 0], y=x_scaled[:, 1], cmap='autumn', s=60)
# plt.title('КЛАСТЕРИЗОВАННЫЙ SCATTERPLOT')
# plt.show()


kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(x_scaled)

# print('CLUSTERS: ', clusters)

# plt.scatter(x=x_scaled[:, 0], y=x_scaled[:, 1], cmap='autumn', c=clusters, s=60)
# plt.title('КЛАСТЕРИЗОВАННЫЙ ЦВЕТНОЙ SCATTERPLOT')
# plt.show()


k_inertia = []
ks = range(1,20)

for k in ks:
    clf_kmeans = KMeans(n_clusters=k)
    clf_kmeans.fit_predict(x_scaled)
    k_inertia.append(clf_kmeans.inertia_)

# plt.plot(ks, k_inertia)
# plt.plot(ks, k_inertia, 'ro')
# plt.show()


# ---------------- ИЕРАРХИЯ КЛАСТЕРОВ --------------------------

distance_mat = pdist(x_scaled)
Z = hierarchy.linkage(distance_mat)

plt.figure(figsize=(20, 9))
dn = hierarchy.dendrogram(Z)

plt.show()

