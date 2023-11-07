import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar, Heatmap, Scatter
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/disaster_response_pl.db')
df = pd.read_sql_table('disaster_response', engine)

# load model
model = joblib.load("../models/disaster_model.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    # For ploting of category counts
    categories =  df[df.columns[4:]]
    category_counts = categories.sum().sort_values(ascending=False)
    category_names = list(category_counts.index)
    
    # For plotting of Top 10 Categories Distribution in News Genre
    news_category = df[df.genre == 'news']
    news_category = news_category[news_category.columns[4:]]
    news_category_counts =  news_category.sum().sort_values(ascending=False)[1:11]
    news_category_names = list(news_category_counts.index)
        
    # extracting categories for heatmap of Direct genre
    direct_category = df[df.genre == 'direct']
    category_map = direct_category.iloc[:,4:].corr().values
    category_names_map = list(df.iloc[:,4:].columns)
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts,                
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Counts"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
       },      
       #Visualization 2: Distribution of Message Categories  
          {
            'data': [
                Scatter(
                      x=category_names,
                      y=category_counts
                )    
            ],
            'layout': {
                  'title': 'Distribution of Message Categories',                  
                  'yaxis': {
                      'title': "Counts"
                  },
                  'xaxis': {
                      'title': "Categories",
                      'padding' : 15,
                      'tickangle': -35
                  }
              } 
        },
        #Visualization 3 : Direct Genre Category Correlation Heatmap
         {
            'data': [
                Heatmap(
                    x=category_names_map,
                    y=category_names_map[::-1],
                    z=category_map,
                    colorscale='Viridis'                   
                )    
            ],

            'layout': {
                'title': 'Direct Genre Category Correlation Heatmap',              
                'xaxis': {
                    'tickangle': -45
                   }
            }
        },
         #Visualization 4: Top 10 Categories Distribution in News Genre
          {
              'data': [
                  Bar(
                      y=news_category_names,
                      x=news_category_counts,
                      orientation = 'h'
                  )
              ],

              'layout': {
                  'title': 'Top 10 Categories Distribution in the News Genre',                       
                  'yaxis': {
                      'title': "Top 10 Categories",
                      'tickangle': -35,
                      'padding' : 15                  
                  },
                  'xaxis': {
                      'title': "Counts"
                  }
              }   
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 
    
    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3000, debug=True)


if __name__ == '__main__':
    main()
