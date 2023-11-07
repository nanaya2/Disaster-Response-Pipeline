# Disaster Response Message Classification Pipeline
Disaster Response Pipeline Udacity project by Nadia Anaya

### Table of Contents

1. [Objective](#Objective)
2. [Prerequesites](#Libraries)
3. [Data/File Description](#FileDescription)
4. [Analysis](#Analysis)
5. [Results](#Results)
6. [Instructions](#Instructions)
7. [Preview](#Preview)
8. [Licensing and Acknowledgements](#Licensing)

## 1. Objective <a name="Objective"></a>
Figure Eight Data Set:  [Disaster Response Messages](https://www.figure-eight.com/dataset/combined-disaster-response-data/) provides thousands of messages that have been sorted into 36 categories. These messages are sorted into specific categories such as Water, Hospitals, Aid-Related, that are specifically aimed at helping emergency personnel in their aid efforts.

The main goal of this project is to build an app that can help emergency workers analyze incoming messages and sort them into specific categories to speed up aid and contribute to more efficient distribution of people and other resources. 

## 2. Prerequisites <a name="Libraries"></a>
All the required libraries are included in the file <code>requirements.txt</code>
* flask
* joblib
* json
* matplotlib
* NLTK
* numpy
* pandas
* pickle
* plotly
* re
* sklearn
* sqlalchemy
* sys

## 3. Data/File Description <a name="FileDescription"></a>
List of Folders and contents:
* app
    - run.py: Flask file to run the web application
    - go.html  and master.html : Also files for the web application
* data
    - disaster_categories.csv: category dataset
    - disaster_messages.csv: messages datasete
    - process_data.py: ETL pipeline script to read, clean, and save data into a table in a database 
    - disaster_response_pl.pb: ETL pipeline output, a SQLite database
* models
    - train_classifier.py: ML pipeline script to train and export a classifier
    - disaster_model.pkl: trained classifier pipeline output

## 4. Analysis <a name="Analysis"></a>

*Data Preparation; Build ETL Pipeline*
- Modify the Category csv; split each category into a separate column
- Merge Data from the two csv files (messages.csv & categories.csv)
- remove duplicates and any non-categorized valued
- create SQL database DisasterResponse.db for the merged data sets

*Text Preprocessing*
- Tokenize text 
- Lemmatize text

*Build ML Pipeline*
- Build Pipeline with countevectorizer and tfidtransformer
- Seal pipeline with multioutput classifier with Randomforest 
- Train pipeline
- Print classification report and accuracy scores

*Improve Model*
- Use GirdSearchCV to build pipein
- Find and use the best parameters

*Export Model*
-  Use pickle to dump the model into disaster_model.pkl

## 5. Results <a name="Results"></a>
1. Created an ETL pipeline to read data from two csv files, clean data, and save data into a SQLite database.
2. Created a machine learning pipeline to train a multi-output classifier on the various categories in the dataset.
3. Created a Flask app to show data visualization and classify any message that users would enter on the web page.

## 6. Instructions <a name="Instructions"></a>
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves model
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3000/

## 7. Preview <a name="Preview"></a>


## 8. Licensing and Acknowledgements <a name="Licensing"></a>
Thanks to Udacity for the starter code and FigureEight for providing the data set to be used by this project.

