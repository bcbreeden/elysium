import unittest
from data_classification import *

class TestData(unittest.TestCase):
    def test_score_classification(self):
        test_sentence = 'The murderous government maintained order by disrupting the election, sending the populace into chaos, displacing trust.'
        score = categorize_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 1)
        self.assertEqual(score['lawful_score'], 1)
        self.assertEqual(score['good_score'], 1)
        self.assertEqual(score['evil_score'], 2)
    
    def test_neutral_classification(self):
        test_sentence = 'A perfect sunny day.'
        score = categorize_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
        self.assertEqual(score['good_score'], 0)
        self.assertEqual(score['evil_score'], 0)
    
    def test_null_sentence_classification(self):
        test_sentence = ''
        score = categorize_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
        self.assertEqual(score['good_score'], 0)
        self.assertEqual(score['evil_score'], 0)
    
    def test_incorrect_type_classification(self):
        test_sentence = 23543456
        score = categorize_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
        self.assertEqual(score['good_score'], 0)
        self.assertEqual(score['evil_score'], 0)

    def test_none_type_classification(self):
        test_sentence = None
        score = categorize_sentence(test_sentence)
        self.assertEqual(score['chaotic_score'], 0)
        self.assertEqual(score['lawful_score'], 0)
        self.assertEqual(score['good_score'], 0)
        self.assertEqual(score['evil_score'], 0)


if __name__ == '__main__':
    unittest.main()