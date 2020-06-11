import requests
from bs4 import BeautifulSoup
import pandas as pd


kompas_id = []

for x in range(1,11):
    url = 'https://kompas.id/kategori/english/page/'
    response = requests.get(url + str(x))
    soup = BeautifulSoup(response.content, 'html5lib')
    content = soup.find_all('div', attrs={'class': 'border-b border-gray-100 clearfix py-4 text-gray-600'})

    for news in content:
        title = news.find('h2').text.strip()
        date = news.find('time').text
        highlight = (news.find('p').text.strip())
        image_link = news.find('div')['style'].replace('background-image: url', '')
        link = (news.find('a')['href'])

        news_detail = {
            'title': title,
            'date': date,
            'highlight': highlight,
            'img link': image_link,
            'link': link
        }
        kompas_id.append(news_detail)
    print('Kompas.id english edition found: ',len(kompas_id))


df = pd.DataFrame(kompas_id)
print(df.head())

df.to_csv('results.csv')