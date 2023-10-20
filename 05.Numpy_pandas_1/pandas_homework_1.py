import pandas as pd

# ratings = pd.read_csv('ml-latest/ratings.csv')
# movies = pd.read_csv('ml-latest/movies.csv')

"""Задание 1
Скачайте с сайта grouplens.org...movielens/ датасет любого размера. Определите, какому фильму было выставлено больше всего оценок 5.0."""

# groupped_data = ratings.merge(movies, on='movieId', how='left')
#
# winners = (
#     groupped_data[['title', 'rating']]
#     .query('rating == 5.0')
#     .groupby('title')
#     .count()
#     .sort_values('rating', ascending=False)
#     .head()
# )
#
# the_winner = winners.iloc[0].name
#
# print(winners)
# print(f'Наибольшее количество оценок 5.0 у фильма: {the_winner}')


"""Задание 2
По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) 
категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity."""
def baltic(country):
    """Объединение стран прибалтики"""

    if country in ['Lithuania', 'Latvia', 'Estonia']:
        return 'Прибалтика'
    return 'Other'

power_data = pd.read_csv('ml-latest/power.csv')
power_data['baltic'] = power_data['country'].apply(baltic)

pd_baltic = (power_data
            .query('baltic == "Прибалтика"')
            .query('quantity >= 0')
            .query('2005 <= year <= 2010')
            .query('category == 4 or category == 12 or category == 21')
            .quantity
            .sum()
             )

print(pd_baltic)

"""Задание 3
Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe."""

# html_table = pd.read_html('https://fortrader.org/quotes')[1]
#
# print(html_table)