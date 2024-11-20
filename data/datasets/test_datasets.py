import unittest
from .clean_category_data import *
import pandas as pd

class TestDatasets(unittest.TestCase):
    def test_headline_data_clean(self):
        clean_category_data()
        df = pd.read_csv('clean_category_data.csv')
        expected_categories = [
            "POLITICS", 
            "WELLNESS", 
            "CULTURE", 
            "FASHION", 
            "MINORITY", 
            "SCIENCE", 
            "BUSINESS", 
            "GOOD NEWS", 
            "RELIGION"
        ]
        actual_categories = set(df['category'].unique())
        
        # Check if all expected categories are in the actual categories
        for category in expected_categories:
            with self.subTest(category=category):
                self.assertIn(category, actual_categories, f"{category} not found in CSV categories.")

if __name__ == '__main__':
    unittest.main()