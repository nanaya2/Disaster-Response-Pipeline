# Disaster Response Message Classification Pipeline
Disaster Response Pipeline Udacity project by Nadia Anaya

## Table of Contents

1. [Objective](#Objective)
2. [Prerequesites](#Libraries)
3. [Data/File Description](#FileDescription)
4. [Analysis](#Analysis)
5. [Results](#Results)
6. [Instructions](#Instructions)
7. [Preview](#Preview)
8. [Licensing and Acknowledgements](#Licensing)

## 1. Objective <a name="Objective"></a>

The objective of this project is to build a web app to analyze manually captured messages from disaster areas and classify them into one or more specific categories. The goal is that this can help emergency workers, medical personal, goverment and others, speed up aid and improve distrubution of all resources to disaster areas.

Appen (formally Figure Eight) has provided a dataset that provides thousands of messages from disaster areas. These messages haven already sorted into categories such as food, water, weather and others totaling 36 categories. This is what will be used to create ETL and ML pipelines for the project.

## 2. Prerequisites <a name="Libraries"></a>
The required libraries for this application are:
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
    - go.html and master.html: Also files for the web application
* data
    - disaster_categories.csv: categories dataset
    - disaster_messages.csv: messages datasete
    - process_data.py: ETL pipeline script to read, clean, and save data into a table in a database 
    - disaster_response_pl.pb: ETL pipeline output, a SQLite database
* models
    - train_classifier.py: ML pipeline script to train and export a classifier
    - disaster_model.pkl: trained classifier pipeline output

## 4. Analysis <a name="Analysis"></a>

*Build ETL Pipeline*

     Data Preparation
    - Modify the Category csv; split each category into a separate column
    - Merge Data from the two csv files (messages.csv & categories.csv)
    - remove duplicates and any non-categorized valued
    - create SQL database disaster_response_pl.pb for the merged data sets
    
     Text Preprocessing
    - Tokenize text 
    - Lemmatize text

*Build ML Pipeline*
    - Build Pipeline with countevectorizer and tfidtransformer
    - Seal pipeline with multioutput classifier with Randomforest 
    - Train pipeline
    - Print classification report and accuracy scores

*Improve Model*
    - Use GridSearchCV to build better pipeline
    - Find and use the best parameters

*Export Model*
    -  Use pickle to dump the model into disaster_model.pkl

## 5. Results <a name="Results"></a>
1. Created an ETL pipeline to read data from two csv files, clean data, and save data into a SQLite database.
2. Created a machine learning pipeline to train a multi-output classifier on the various categories in the dataset.
3. Created a Flask app to show data visualization and classify any message that users would enter on the web page.

## 6. Instructions <a name="Instructions"></a>
1. In the root directory, run the ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/disaster_response_pl.pb'
   
2. Again in root, run the ML pipeline that trains the classifier and saves the model
        `python models/train_classifier.py data/disaster_response_pl.pb models/disaster_model.pkl`
   
3. Next, run your web app from the app folder
    `python run.py`

4. Go to http://0.0.0.0:3000/

## 7. Preview <a name="Preview"></a>
![classifymessages](https://github.com/nanaya2/Disaster-Response-Pipeline/assets/75550215/6bcb7bba-1be3-41df-a4b4-2cc823942c78)
![distofgenre](https://github.com/nanaya2/Disaster-Response-Pipeline/assets/75550215/e9feeb5d-45a4-4040-855e-a6fdfaa3789a)
![distcat](https://github.com/nanaya2/Disaster-Response-Pipeline/assets/75550215/9a12ebfa-d58f-4a9b-b5b7-edcfae1e66ee)
![directcathist](https://github.com/nanaya2/Disaster-Response-Pipeline/assets/75550215/0305877f-1f12-4cf3-9593-2d7a44352943)
![top10newscat](https://github.com/nanaya2/Disaster-Response-Pipeline/assets/75550215/58d78a6e-fcc5-4ae3-b5fc-53cbcbfe1ce1)

## 8. Licensing and Acknowledgements <a name="Licensing"></a>
Thanks to FigureEight for providing the valuable dataset used in this important project. Data can be found here
 [Disaster Response Messages](https://www.figure-eight.com/dataset/combined-disaster-response-data/)

 Also thanks to Udacity for the code templates which help me complete this project.


