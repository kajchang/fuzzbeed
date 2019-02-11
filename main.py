import requests
from bs4 import BeautifulSoup

import json
import re
import os

if os.path.exists('titles.json'):
    with open('titles.json') as titles_file:
        titles = json.load(titles_file)

else:
    print('Scraping Buzzfeed Article Titles...')
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

            titles.append(title)

        page += 1

word_regex = r'((?:[A-Z][a-z]+ ?)+)'

patterns = [
    [r'Can We Guess {word_regex} Based On {word_regex}\?', True]
]

sources = []
results = []

for title in titles:
    for pattern, flipped in patterns:
        match = re.match(pattern.format(word_regex=word_regex), title)

        if match:
            source = match.group(1)
            result = match.group(2)

            if flipped:
                source, result = result, source

            sources.append(source)
            results.append(result)

            pattern = pattern.format(word_regex='_____').replace('\\', '')

            print('''--------
Title: {title}
Source: {source}
Result: {result}
Pattern: {pattern}
--------'''.format(**locals()))

            continue


with open('titles.json', 'w') as titles_file:
    json.dump(titles, titles_file, indent=4)

with open('sources.json', 'w') as sources_file:
    json.dump(sources, sources_file, indent=4)

with open('results.json', 'w') as results_file:
    json.dump(results, results_file, indent=4)
