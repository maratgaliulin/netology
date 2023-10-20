import pandas as pd
import requests
from bs4 import BeautifulSoup

# https://habr.com
#           /ru/search/?
#           q=python
#           &
#           target_type=posts
#           &
#           order=relevance



# https://habr.com
#           /ru/search/page2/
#           ?q=python
#           &
#           target_type=posts
#           &
#           order=relevance

BASE_URL = 'https://habr.com'

page = 2

resp = requests.get(BASE_URL + f'/ru/search/page{page}', params=dict(
    q='python',
    target_type='posts',
    order='relevance'
    ))

soup = BeautifulSoup(resp.text, features="lxml")

data = []

for article_tag in soup.find_all('article'):

    # print (article_tag.prettify())

    dt = article_tag.find('time').get('datetime')

    h2_tag = article_tag.find('h2')
    title = h2_tag.get_text()
    link = BASE_URL + h2_tag.find('a').get('href')

    article_resp = requests.get(link)
    article_soup = BeautifulSoup(article_resp.text, features="lxml")
    article_full_text = article_soup.find('div', attrs={'class' : 'tm-article-body'}).get_text().strip()

    # tm-votes-meter__value
    rating = article_tag.find('span', attrs={'class': 'tm-votes-meter__value'}).get_text()

    data.append([dt, title, link, rating, article_full_text])


X = pd.DataFrame(data, columns=['date', 'title', 'link', 'rating', 'article_full_text'])
X.drop_duplicates(inplace=True)
X['date'] = pd.to_datetime(X['date']).dt.date
pd.set_option('display.max_colwidth', None)

print(X['article_full_text'].head())