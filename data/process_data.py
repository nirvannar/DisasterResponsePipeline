import sys
# import libraries
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    
    # load messages dataset
    messages = pd.read_csv(messages_filepath)
        
    # load categories dataset
    categories = pd.read_csv(categories_filepath)
        
    # merge datasets
    df = messages.merge(categories, on=('id'))
    
    return df
    


def clean_data(df):
    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand=True)
    
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes  everything 
    # up to the second to last character of each string with slicing

    category_colnames = list(map(lambda x: x[:-2], row))
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1:]
    
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        
    # check which columns are binary
    check = categories.columns[~categories.isin([0,1]).all()]
    
    # replace 2 with 1 in related category
    for column in categories:    
        if (column == 'related'):
            categories[column].replace(2, 1, inplace=True)
    
    # check all columns are binary after replace
    check = categories.columns[categories.isin([0,1]).all()] 
    
    # drop the original categories column from `df`
    df.drop('categories', axis=1, inplace=True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    
    # check number of duplicates
    df.duplicated().sum()
   
    # drop duplicates
    df.drop_duplicates(inplace=True)
    # check number of duplicates
    df.duplicated().sum()
    
    return df

    


def save_data(df, database_filename):
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('DisResPipe', engine, index=False, if_exists='replace') 
    return  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
