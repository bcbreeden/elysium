import unittest
from data_classification import *
from news_api import *

class TestData(unittest.TestCase):
    def test_score_classification(self):
        test_sentence = 'The murderous government maintained order by disrupting the election, sending the populace into chaos, displacing trust.'
        score = score_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 3)
        self.assertEqual(score['lawful_score'], 2)
        self.assertEqual(score['sentiment_score'],-0.6808)
    
    def test_neutral_classification(self):
        test_sentence = 'A perfect sunny day.'
        score = score_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
        self.assertEqual(score['sentiment_score'], 0.7579)
    
    def test_null_sentence_classification(self):
        test_sentence = ''
        score = score_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
    
    def test_incorrect_type_classification(self):
        test_sentence = 23543456
        score = score_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)

    def test_none_type_classification(self):
        test_sentence = None
        score = score_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
    
    def test_headlines_api_call(self):
        response = make_news_articles_api_call('bbc-news')[0]
        self.assertEqual(response, 200)

    def test_sources_api_call(self):
        response = make_sources_api_call()[0]
        self.assertEqual(response, 200)

if __name__ == '__main__':
    unittest.main()