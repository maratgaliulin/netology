import pandas as pd


# Задание 1

# log_df = pd.read_csv('ml-latest/visit_log.csv', sep=';')
#
# log_df.loc[:, 'source_type'] = log_df.loc[:, 'traffic_source']
# log_df.loc[(log_df['traffic_source'] == 'yandex') | (log_df['traffic_source'] == 'google'), 'source_type'] = 'google'
# log_df.loc[((log_df['region'] == 'Russia') & (log_df['traffic_source'] == 'paid')) | ((log_df['region'] == 'Russia')
#                                                                                       & (log_df['traffic_source'] ==
#                                                                                          'email')), 'source_type'] = 'ad'
# log_df.loc[((log_df['region'] != 'Russia') & (log_df['traffic_source'] == 'paid')) | ((log_df['region'] != 'Russia')
#                                                                                       & (log_df['traffic_source'] ==
#                                                                                          'email')), 'source_type'] = \
#     'other'
#
# print(log_df.loc[:, ['visit_id', 'region', 'traffic_source', 'source_type']].head(50))


# Задание 2


# templ = '/\\d{8}-'
#
# txturl = pd.read_table('ml-latest/URLs.txt')['url']
#
# print(txturl[txturl.str.contains(templ, regex=True)].sort_values())


# Задание 3


# ratings_by_user = pd.read_csv('ml-latest/ratings.csv').groupby('userId').agg({'userId': ['count'], 'timestamp': ['max', 'min']})
#
# ratings_by_user['diff'] = ratings_by_user['timestamp']['max'] - ratings_by_user['timestamp']['min']
# ratings_by_user['user_count'] = ratings_by_user['userId']['count']
#
# ratings_by_user_more_than_100 = ratings_by_user[ratings_by_user['user_count'] > 100][['diff', 'user_count']]
#
# print(ratings_by_user_more_than_100)
#
# print(f'Среднее время жизни пользователей с > 100 оценок в днях: 'f'{round((ratings_by_user_more_than_100["diff"].mean() / 86400), 2)}')



rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)

auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)

air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)

client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)


join_wo_address = rzd.merge(auto.merge(air, on='client_id', how='outer'), on='client_id', how='outer').fillna(0)

join_with_address = client_base.merge(rzd.merge(auto.merge(air, on='client_id', how='outer'), on='client_id',
                                               how='outer'), how='outer', on='client_id').fillna(0)

print(join_with_address)