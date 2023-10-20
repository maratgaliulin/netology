import pandas as pd
from urllib import parse

"""Статистика рекламных кампаний"""

stats = pd.read_excel('ml-latest/ad_campaigns.xlsx')
stats.columns = ['group', 'phrase', 'effect', 'ad_id', 'title', 'text', 'link']
"""Ламбда функции: """
"""Хотим посчитать распределение количества слов в столбце с фразами"""


"""Вариант 1, без передачи целой строки: """
# stats['word count'] = stats['phrase'].apply(lambda word: len(word.split(' ')))

"""Вариант 2, с передачей всей строки: """
stats['word count'] = stats.apply(lambda x: len(x['phrase'].split(' ')), axis=1)

# print(stats.head())

res = stats['word count'].value_counts()
url = stats.loc[0, 'link']
# print(url)
# print(res)

parsed = parse.urlsplit(url)

"""Как достать из всей ссылки параметры: """

"""1. Параметр utm_campaign из строки вручную: """
# utm_camp = parsed.query.split('&')[2].split('=')[1]
# print(utm_camp)

"""2. По-питоновски: """
# utm_camp = parse.parse_qs(parsed.query)['utm_campaign'][0]
# print(utm_camp)

def campaign_name(row):
    """Получение названия компании из ссылки внутри строки row: """
    parsed_campaign_name = parse.urlsplit(row['link'])
    params_dict = parse.parse_qs(parsed_campaign_name.query)
    return params_dict['utm_campaign'][0]

def power_up(row, n):
    """Возводит значение столбца effect в степень n"""
    return row['effect'] ** n

def mrt(row):
    if ('мрт' not in row['group']) and ('24 часа' in row['text']):
        return True
    return False


stats['campaign'] = stats.apply(campaign_name, axis=1)
stats['power_up'] = stats.apply(power_up, n=3, axis=1)
stats['mrt'] = stats.apply(mrt, axis=1)

"""Просто выводим stats: """
# print(stats.head())

"""Выводим статистику по количеству True/False из колонки 'mrt' """
# print(stats.mrt.value_counts())

"""Отдельно выводим строки где 'mrt' ==  True """
# print(stats[stats['mrt'] == True])

