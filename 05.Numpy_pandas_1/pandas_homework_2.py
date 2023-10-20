import pandas as pd

movies = pd.read_csv('ml-latest/movies.csv')
ratings = pd.read_csv('ml-latest/ratings.csv')

#
# def rating_classifier(data):
#     if data['rating'] <= 2.0:
#         return 'низкий рейтинг'
#     elif data['rating'] <= 4.0:
#         return 'средний рейтинг'
#     elif data['rating'] == 4.5 or data['rating'] == 5.0:
#         return 'высокий рейтинг'
#     return 'Error'
#
# ratings['class'] = ratings.apply(rating_classifier, axis=1)
#
# movies_combined = ratings.merge(movies, on='movieId', how='left')[['userId', 'title', 'rating', 'class']]
# print(movies_combined.head())


# keywords_list = pd.read_csv('ml-latest/keywords.csv', nrows=150)
#
# def geo_classifier(data):
#     geo_data = {
#         'Центр':['москва', 'тула', 'ярославль'],
#         'Северо-Запад': ['петербург', 'псков', 'мурманск'],
#         'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
#         }
#
#     for substr in data['keyword'].split(' '):
#         if substr in geo_data['Центр']:
#             return 'Центр'
#         elif substr in geo_data['Северо-Запад']:
#             return 'Северо-Запад'
#         elif substr in geo_data['Дальний Восток']:
#             return 'Дальний Восток'
#         return 'undefined'
#
# keywords_list['region'] = keywords_list.apply(geo_classifier, axis=1)
# print(keywords_list)


movies_merged = ratings.merge(movies, on='movieId', how='left')[['title', 'rating']]


def production_year(data):
    years = list(map(str, range(1950, 2011)))
    str_concat = data['title'][-5:-1]
    if str_concat in years:
        return int(str_concat)
    return 1900


movies_merged['year'] = movies_merged.apply(production_year, axis=1)

print(movies_merged[['year', 'rating']].groupby('year').mean().sort_values('rating', ascending=False))



