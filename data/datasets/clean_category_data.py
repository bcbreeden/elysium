import pandas as pd
import json
import os

def clean_category_data():
    '''
    Opens the news category dataset and drops/combines categories into a more managable set.

    Saves the result as a csv.
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'News_Category_Dataset.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        data = [json.loads(line) for line in file]

    df = pd.DataFrame(data)

    categories_to_drop = [
        "U.S. NEWS",
        "PARENTING",
        "WORLD NEWS",
        "CRIME",
        "FOOD & DRINK",
        "TRAVEL",
        "IMPACT",
        "COLLEGE",
        "PARENTS",
        "TASTE",
        "THE WORLDPOST",
        "WORLDPOST",
        "FIFTY",
        "DIVORCE",
        'SPORTS'
    ]
    df = df[~df['category'].isin(categories_to_drop)]

    # SCIENCE
    categories_to_combine = ['ENVIRONMENT',
                            'SCIENCE',
                            'GREEN',
                            'TECH']
    df['category'] = df['category'].replace(categories_to_combine, 'SCIENCE')

    # CULTURE
    categories_to_combine = ['CULTURE & ARTS',
                            'ENTERTAINMENT',
                            'MEDIA',
                            'ARTS & CULTURE',
                            'ARTS']
    df['category'] = df['category'].replace(categories_to_combine, 'CULTURE')

    # WELLNESS
    categories_to_combine = ['EDUCATION',
                            'WELLNESS',
                            'HEALTHY LIVING']
    df['category'] = df['category'].replace(categories_to_combine, 'WELLNESS')

    # BUSINESS
    categories_to_combine = ['BUSINESS',
                            'MONEY']
    df['category'] = df['category'].replace(categories_to_combine, 'BUSINESS')

    # RELIGION
    categories_to_combine = ['RELIGION',
                            'WEIRD NEWS']
    df['category'] = df['category'].replace(categories_to_combine, 'RELIGION')

    # FASHION
    categories_to_combine = ['STYLE & BEAUTY',
                            'HOME & LIVING',
                            'WEDDING',
                            'WEDDINGS',
                            'STYLE']
    df['category'] = df['category'].replace(categories_to_combine, 'FASHION')

    # MINORITY
    categories_to_combine = ['QUEER VOICES',
                            'WOMEN',
                            'BLACK VOICES',
                            'LATINO VOICES']
    df['category'] = df['category'].replace(categories_to_combine, 'MINORITY')

    # GOOD NEWS
    categories_to_combine = ['GOOD NEWS',
                            'COMEDY']
    df['category'] = df['category'].replace(categories_to_combine, 'GOOD NEWS')

    category_counts = df['category'].value_counts()
    df.to_csv('clean_category_data.csv', index=False)
    print('Data cleaning successful, category counts:')
    print(category_counts)