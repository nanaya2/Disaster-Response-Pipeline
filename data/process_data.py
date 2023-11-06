# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):    
    """
    Function to load messages and categories files to dataframes
    Input:  messages and categories path and filenames
    Output: dataframe
    """  
    # load messages dataset
    messages = pd.read_csv(messages_filepath)
        
    # load categories dataset
    categories = pd.read_csv(categories_filepath)
     
    # merge datasets
    df = messages.merge(categories, how='outer', on=['id'])
    
    return df

def clean_data(df): 
    """
    Function to clean the disaster dataframe
    Input:  dataframe
    Output: cleaned dataframe
    """  
    
    # create a dataframe of the 36 individual category columns
    categories = df["categories"].str.split(";", expand = True) 
     
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing    
    category_colnames = row.str.split('-').apply(lambda x: x[0])
    
    # rename the columns of `categories`
    categories.columns = category_colnames
        
    #convert values to 0 or 1
    for column in categories:
       # set each value to be the last character of the string
       categories[column] =  categories[column].str.strip().str[-1]
    
       # convert column from string to numeric
       categories[column] =  categories[column].astype(int)
        
    # drop the original categories column from `df`
    df = df.drop('categories', axis=1)
     
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    
    # drop duplicates
    df = df.drop_duplicates()
    
    return df


def save_data(df, database_filename):
    """
    Function to load datagframe into a database table
    Input:  dataframe and database name
    Output: loaded table in a database
    """  
   
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('disaster_response', engine, index=False)


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
              'disaster_response_pl.db')


if __name__ == '__main__':
    main()