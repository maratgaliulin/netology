import pandas as pd

"""Чтение файла .csv"""

# data = pd.read_csv('ml-latest/power.csv')

# print(data.head())


"""Группировка информации по значениям определенного столбца, сортировка, ограничение запроса 
(query('category >16'))
"""
# print(data.groupby('country').count()
#       .sort_values('quantity')
#       .query('category > 16')
#       .reset_index()[['country', 'quantity']]
#       )

"""Применение функции к датасету: """
def baltic(country):
    """Объединение стран прибалтики"""

    if country in ['Lithuania', 'Latvia', 'Estonia']:
        return 'Прибалтика'
    return 'Other'

# data['baltic'] = data.country.apply(baltic)
# print(data["baltic"].value_counts())


ratings = pd.read_csv('ml-latest/ratings.csv')

# print(ratings.head())

# print(ratings.groupby('rating').count()
#       .sort_values('rating')
#       )

"""Вывод информации о датасете: """
# print(ratings.info())

"""Сколько уникальных фильмов содержится в базе: """
# print(ratings.movieId.unique())

"""Топ 5 пользователей по активности: """
# print(ratings
#       .groupby('userId').count()
#       .sort_values('movieId', ascending=False)
#       .head()
#       )

"""Подсчет времени жизни пользователя: """
# ratings_groupped = ratings.groupby('userId').agg([min, max])
# ratings_groupped['diff'] = ratings_groupped['timestamp']['max'] - ratings_groupped['timestamp']['min']

# print(ratings_groupped.head())
# print(ratings_groupped['diff'].mean()/24/3600)


"""Объединение таблиц: """

movies = pd.read_csv('ml-latest/movies.csv')

# print(movies[['title', 'genres']].head())

joined = ratings.merge(movies, on='movieId', how='left')

print(joined[['userId', 'rating', 'title']]
      .query('rating >= 4.5')
      .sort_values('rating', ascending=False)
      .head())