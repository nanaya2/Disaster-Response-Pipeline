# Disaster Response Message Classification Pipeline
Disaster Response Pipeline Udacity project

### Table of Contents

1. [Objective](#Objective)
2. [Prerequesites](#Libraries)
3. [Data/File Description](#FileDescription)
4. [Analysis](#Analysis)
5. [Results](#Results)
6. [Instructions](#Instructions)
7. [Licensing, Authors, and Acknowledgements](#Licensing)

## Objective <a name="Objective"></a>
Figure Eight Data Set:  [Disaster Response Messages](https://www.figure-eight.com/dataset/combined-disaster-response-data/) provides thousands of messages that have been sorted into 36 categories. These messages are sorted into specific categories such as Water, Hospitals, Aid-Related, that are specifically aimed at helping emergency personnel in their aid efforts.

The main goal of this project is to build an app that can help emergency workers analyze incoming messages and sort them into specific categories to speed up aid and contribute to more efficient distribution of people and other resources. 

## Prerequisites <a name="Libraries"></a>
All the required libraries are included in the file <code>requirements.txt</code>
* pandas
* numpy
* sqlalchemy
* matplotlib
* plotly
* NLTK
* NLTK [punkt, wordnet, stopwords]
* sklearn
* joblib
* flask

## Data/File Description <a name="FileDescription"></a>
List of Folders and contents:
* app
    - run.py: Flask file to run the web application
    - templates contains html file for the web application
* data
    - disaster_categories.csv: category dataset
    - disaster_messages.csv: messages datasete
    - process_data.py: ETL pipeline scripts to read, clean, and save data into a table in a database 
    - disaster_response_pl: ETL pipeline output, a SQLite database
* models
    - train_classifier.py: pipeline scripts to train and export a classifier
    - disaster_model.pkl: trained classifier pipeline output

## Analysis <a name="Analysis"></a>
*Data Preparation*
- Modify the Category csv; split each category into a separate column
- Merge Data from the two csv files (messages.csv & categories.csv)
- remove duplicates and any non-categorized valued
- create SQL database DisasterResponse.db for the merged data sets

*Text Preprocessing*
- Tokenize text 
- lemmatize text
- remove stop words

*Build Machine Learning Pipeline*
- Build Pipeline with countevectorizer and tfidtransformer
- Seal pipeline with multioutput classifier with random forest 
- Train Pipeline (with Train/Test Split)
- Print classification reports and accuracy scores

*Improve Model*
- Preform GirdSearchCV
- Find best parameters

*Export Model as .pkl File*
- You could also use Joblib as it can be faster. read more [here](https://stackoverflow.com/questions/12615525/what-are-the-different-use-cases-of-joblib-versus-pickle)

## Results <a name="Results"></a>
1. Created an ETL pipeline to read data from two csv files, clean data, and save data into a SQLite database.
2. Created a machine learning pipeline to train a multi-output classifier on the various categories in the dataset.
3. Created a Flask app to show data visualization and classify any message that users would enter on the web page.

## Instructions <a name="Instructions"></a>
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves model
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Licensing, Authors, and Acknowledgements <a name="Licensing"></a>
Thanks to Udacity for the starter code and FigureEight for providing the data set to be used by this project.

