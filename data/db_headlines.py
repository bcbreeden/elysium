import sqlite3
from news_api import make_news_articles_api_call
from data_classification import categorize_sentence

def insert_headlines():
    print('Attempting to insert headlines into the database.')
    conn = sqlite3.connect('elysium.db')
    cursor = conn.cursor()
    sources = ['bbc-news', 'abc-news', 'the-wall-street-journal','fox-news', 'associated-press', 'cnn']
    for source in sources:
        data = make_news_articles_api_call(source)[1]
        for article in data:
            headline_scores = categorize_sentence(article['title'])
            headline_id = _generate_id(article['title'])
            insert_query = """
            INSERT INTO headlines (id, headline, chaotic_score, lawful_score, sentiment_score)
            VALUES (?, ?, ?, ?, ?);
            """
            data = (headline_id,
                    article['title'],
                    headline_scores['chaotic_score'],
                    headline_scores['lawful_score'],
                    headline_scores['sentiment_score'])
            cursor.execute(insert_query, data)
            conn.commit()
    print('Headlines data insertion successful. Closing conn.')
    conn.close()

def _generate_id(headline_text):
    return sum(ord(char) for char in headline_text)
