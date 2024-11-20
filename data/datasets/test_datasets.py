import unittest
from .clean_category_data import clean_category_data
import pandas as pd
import os

class TestDatasets(unittest.TestCase):
    def test_headline_data_clean(self):
        clean_category_data()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'category_data.csv')
        df = pd.read_csv(file_path)
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