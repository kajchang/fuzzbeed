import requests
from bs4 import BeautifulSoup

import json
import re

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

patterns = [
    [r'Can We Guess ((?:[A-Z][a-z]+ )+)Based On ((?:[A-Z][a-z]+ ?)+)\?', True]
]

for title in titles:
    for pattern, flipped in patterns:
        match = re.match(pattern, title)

        if match:
            source = match.group(1)
            result = match.group(2)

            if flipped:
                source, result = result, source

            print('''--------
Title: {title}
Source: {source}
Result: {result}
Pattern: {pattern}
--------'''.format(**locals()))

            continue
