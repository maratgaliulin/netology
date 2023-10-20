import pandas as pd
import requests
from bs4 import BeautifulSoup


def habr_web_scraper(request_list: list, pages: int):
    BASE_URL = 'https://habr.com'
    for index, req in enumerate(request_list):
        data = []
        for page in range(pages):
            resp = requests.get(
                BASE_URL + f'/ru/search/page{page + 1}', params=dict(
                    q=req,
                    target_type='posts',
                    order='relevance'
                    )
                )

            soup = BeautifulSoup(resp.text, features="lxml")
            for article_tag in soup.find_all('article'):

                dt = article_tag.find('time').get('datetime')

                h2_tag = article_tag.find('h2')
                title = h2_tag.get_text()
                try:
                    link = BASE_URL + h2_tag.find('a').get('href')
                    article_resp = requests.get(link)
                    article_soup = BeautifulSoup(article_resp.text, features="lxml")
                    article_full_text = article_soup.find('div', attrs={'class': 'tm-article-body'}).get_text().strip()
                except:
                    link = ''
                    article_full_text = ''

                rating = article_tag.find('span', attrs={'class': 'tm-votes-meter__value'}).get_text()

                data.append([dt, title, link, rating, article_full_text])

            X = pd.DataFrame(data, columns=['date', 'title', 'link', 'rating', 'article_full_text'])
            X.drop_duplicates(inplace=True)
            X['date'] = pd.to_datetime(X['date']).dt.date

        print(X.head(10))


habr_web_scraper(['python', 'анализ данных'], 2)
