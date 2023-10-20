import pandas as pd
from urllib import parse

stats = pd.read_excel('ml-latest/ad_campaigns.xlsx')
stats.columns = ['group', 'phrase', 'effect', 'ad_id', 'title', 'text', 'link']
def campaign_name(row):
    """Получение названия компании из ссылки внутри строки row: """
    parsed_campaign_name = parse.urlsplit(row['link'])
    params_dict = parse.parse_qs(parsed_campaign_name.query)
    return params_dict['utm_campaign'][0]

stats['campaign'] = stats.apply(campaign_name, axis=1)

df = pd.DataFrame(
    {
        'order_id': [1, 2, 3, 4, 5],
        'country': ['Россия', 'Китай', 'Китай', 'Россия', 'Россия'],
        'category': ['Электроника', 'Авто', 'Электроника', 'Авто', 'Авто'],
        'amount': [100, 80, 90, 140, 90]
        }
    )
# print(df)

def groupby_function(data):
    return data.amount.max() - data.amount.min()

# df_groupped = df.groupby('country')
# print(df_groupped.apply(groupby_function))

# print(stats.groupby('campaign').count()[['group', 'effect']].reset_index().head())

print(stats['campaign'].value_counts().reset_index().head())