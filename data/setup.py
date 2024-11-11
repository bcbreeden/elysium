import nltk
import sqlite3

def _setup_nltk():
    nltk.download('all')

# Database Setup
def _create_tables():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('elysium.db')
    cursor = conn.cursor()
    print('Starting to build tables...')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS headlines (
        id INTEGER PRIMARY KEY,
        headline TEXT NOT NULL,
        chaotic_score INTEGER,
        lawful_score INTEGER,
        sentiment_score REAL
    )
    ''')
    print('Headlines table successfully constructed.')

if __name__ == '__main__':
    _setup_nltk()
    _create_tables()