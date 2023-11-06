#import libraries
import sys
import re
import numpy as np
import pandas as pd
import pickle
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import TruncatedSVD

def load_data(database_filepath):
    """
    Function to connect to database and read the disaster_reponse table to create features and label arrays
    Input:  database path and filename
    Output: features and label arrays
    """  
    #load data from database
    engine = create_engine('sqlite:///'+database_filepath)     
    df = pd.read_sql_table('disaster_response',engine) 
    
    # define features and label arrays
    X = df['message']
    Y = df.drop(['id','message','original','genre'],axis=1)
    category_names = Y.columns.tolist()    
    
    return X, Y, category_names 
    

def tokenize(text):
    """ 
    Function to tokenize a text
    Input: text
    Output: clean tokens
    """  
    
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

def build_model():
    """ 
    Function to build and return the GridSearchCV object to be used as the model
    Input:   None
    Output: cv (scikit-learn GridSearchCV): Grid search model object
    """     
    pipeline = Pipeline([
        ('vect', CountVectorizer()),      
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))       
    ])

    # specify parameters for grid search
    parameters = { 
         #'tfidf__use_idf': (True, False), 
         'clf__estimator__n_estimators': [50, 100],
         'clf__estimator__min_samples_split': [2, 4]          
         #'clf__estimator__n_estimators': [8, 15],
         #'clf__estimator__min_samples_split': [2],
    }
        
    #Create Model
    cv = GridSearchCV(pipeline, parameters, cv=3,  n_jobs=-1, verbose=0)
    
    return cv 

def evaluate_model(model, X_test, y_test, category_names ):
    '''
    Function to generate classification report and report accurracy scores on the model
    Input: Model, test set, category names
    Output: Prints the Classification report and accuracy scores
    '''
    y_pred = model.predict(X_test)
    for i, col in enumerate(y_test):
       print(col)
       print(classification_report(y_test[col], y_pred[:, i]))        

    for i, column in enumerate(y_test.columns):
        print('%25s accuracy : %.2f' %(category_names[i], accuracy_score(y_test.loc[:, column].values, y_pred[:, i])))
            
def save_model(model, model_filepath):
    '''
    Function to export model as a pickle file
    Input: Model, model pickle filename
    Output: pickle file
    '''
    with open(model_filepath, 'wb') as f:
        pickle.dump(model, f)

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2 )
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/disaster_response_pl.db disaster_model.pkl')


if __name__ == '__main__':
    main()
    