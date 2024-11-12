import sqlite3
from news_api import make_news_articles_api_call
from data_classification import categorize_sentence
from datetime import datetime

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
            publish_date = _format_datetime(article['publishedAt'])
            insert_query = """
            INSERT OR REPLACE INTO headlines (id, headline, chaotic_score, lawful_score, sentiment_score, publish_date)
            VALUES (?, ?, ?, ?, ?, ?);
            """
            data = (headline_id,
                    article['title'],
                    headline_scores['chaotic_score'],
                    headline_scores['lawful_score'],
                    headline_scores['sentiment_score'],
                    publish_date)
            cursor.execute(insert_query, data)
            conn.commit()
    print('Headlines data insertion successful. Closing conn.')
    conn.close()

def get_all_headlines():
    print('Attempting to get all headlines from the database.')
    conn = sqlite3.connect('elysium.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM headlines')
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    print('All headlines have been returned.')
    return rows

def _generate_id(headline_text):
    return sum(ord(char) for char in headline_text)

def _format_datetime(datetime_string):
    # Replace 'Z' with an empty string (indicating UTC)
    if datetime_string.endswith('Z'):
        datetime_string = datetime_string[:-1]  # Remove the 'Z'

    # If there are more than six digits in microseconds, truncate to six
    if '.' in datetime_string:
        datetime_string = datetime_string[:datetime_string.index('.') + 7]  # Keep six digits of precision

    try:
        # Attempt to parse with microseconds if present
        timestamp = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        # Fallback to parse without microseconds
        timestamp = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S')
    return timestamp
