from data_classification import categorize_sentence, _sentiment_analysis
import constants
import requests

def make_news_articles_api_call(news_source):
    print('Fetching top stories from:', news_source)
    api_key = constants.NEWS_API
    request_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(news_source,api_key)
    response = requests.get(request_url)
    if response.status_code == 200:
        print('News API Call Successful.')
    else:
        print('There was an error during the News API call.')
        print('Response:', response.status_code)
        print(response.json())
    return[response.status_code, response.json()['articles']]

def get_sources():
    api_key = constants.NEWS_API
    request_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'.format(api_key)
    response = requests.get(request_url)
    if response.status_code == 200:
        print('News API Call Successful.')
    else:
        print('There was an error during the News API call.')
        print('Response:', response.status_code)
    return[response.status_code, response.json()['sources']]


sources = ['bbc-news', 'abc-news', 'the-wall-street-journal']
for source in sources:
    data = make_news_articles_api_call(source)[1]
    for article in data:
        print(article['title'])
        print(categorize_sentence(article['title']))


