import requests
from bs4 import BeautifulSoup

import json

base_url = 'https://www.buzzfeed.com/us/feedpage/feed/quizzes-can-we-guess?page={}&page_name=quizzes&'
page = 1

titles = []

while True:
    resp = requests.get(base_url.format(page))

    if resp.status_code == 404:
        break

    soup = BeautifulSoup(resp.text, 'html.parser')

    for article in soup.find_all(attrs={'data-buzzblock': ['featured-card', 'story-card']}):
        if 'featured-card' in article['class']:
            title = article.find('h1').text

        else:
            title = article.find('h2').text

        print(title)
        titles.append(title)

    page += 1


with open('titles.json', 'w') as titles_file:
    json.dump(titles, titles_file, indent=4)
