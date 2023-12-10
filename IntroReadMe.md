# Disaster Response Pipeline Project
My second Udacity Project creates a machine learning pipeline to categorize disaster events so that the messages can be viewed by emergency workers and sent to the appropriate disaster relief agencies.

# Table of Contents

* [Installation](#Installation)
* [Project Motivation](#Project-Motivation)
* [File Descriptions and Analyses](#File-Descriptions-and-Analyses)
* [Results](#Results)
* [Licensing, Authors, and Acknowledgements](#Licensing,-Authors,-and-Acknowledgements)


## Installation <a name="Installation"></a>
The code should run with no issues using Python version 3.6.3 using Jupyter Notebook server version 5.7.0 in the Udacity Project Workspace.  Packages that were imported include Pandas,sqlite3, sqlalchemy create_engine, NumPy,  matplotlib.pyplot.  

## Project Motivation <a name="Project-Motivation"></a>
For this project, I used a data set from [Appen](https://appen.com/) (formally Figure 8) containing real messages that were sent during previous disaster events. 

A machine learning pipeline was created to categorize these events so that the messages could be sent to an appropriate disaster relief agency. This project included a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display three visualizations of the data. 

**_Project Components_**
 
**_1. ETL Pipeline_** *The Extract, Transform, and Load (ETL) process read the dataset, cleaned the data, and then stored it in a SQLite database.*  
**_2. Machine Learning Pipeline_** *The data was loaded from the SQLite database.  The data was then split  into a training set and a test set. A text processing and machine learning pipeline was built.  GridSearchCV was used to train and tune the model.  The results on the test set were outputted, and the model was exported to a pickle file*  
**_3. Flask Web App Deployment_** *The flask web app design was customised with html and css.  Data visualizations were created using Plotly in the web app*  



## File Descriptions and Analyses <a name="File-Descriptions-and-Analyses"></a>
**_ETL Pipeline Preparation_**
Two datasets ```messages.csv``` and ```categories.csv``` containing real messages that were sent during disaster events were merged using the common ```'id'```.  This combined dataset was assigned to ```df```which was then cleaned. Finally it was stored in a SQLite database ```DisResPipe.db``` using the pandas dataframe ```.to_sql()``` method.



**_ML Data Preparation_**  
The data was split into a training set and a test set. A machine learning pipeline was created that used NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model that uses the message column to predict classifications for 36 categories (multi-output classification). The model was exported to a pickle file ```classifier,pkl```. The final machine learning code in ```train_classifier.py```.


## Results <a name="Results"></a>

**ETL Pipeline** *Python ETL script ```process_data.py``` which contained the data cleaning code ran in the terminal without errors.*  


**Machine Learning Pipeline** *The machine learning script, ```train_classifier.py```, runs in the terminal without errors*  


**Flask Web App Deployment** *The web app ran without errors. When a user inputs a message into the app, the app returns classification results for all 36 categories as shown in the screenshots below.*  
Type in the command line Project Workspace IDE as below to run the Flask app.

```python
python run.py
```



![image](https://github.com/nirvannar/DisasterResponsePipeline/assets/52913504/1f5b13a0-9d57-44cc-8b6f-c0db43e7be5e)
![image](https://github.com/nirvannar/DisasterResponsePipeline/assets/52913504/36987932-4d63-42fc-a5f9-7209ed944b02)
![image](https://github.com/nirvannar/DisasterResponsePipeline/assets/52913504/1dff5d30-c10e-4b01-9582-2061d859d642)

The MLP visualisations and analyses of data suggested that messages could go to disaster relief organizations such as [The Red Cross](https://www.redcross.org/about-us/our-work/international-services/international-disasters-and-crises.html), [The International Rescue Committee](https://www.rescue.org/) and [the United Nations Office for the Coordination of Humanitarian Affairs](https://www.unocha.org/).

This dataset is imbalanced (ie some labels like water have few examples). In your README, discuss how this imbalance, how that affects training the model, and your thoughts about emphasizing precision or recall for the various categories.


## Licensing, Authors, and Acknowledgements <a name="Licensing,-Authors,-and-Acknowledgements"></a>
The data was provided by [Appen](https://appen.com/). [Scikit-learn.org](https://scikit-learn.org/), [Stack Overflow](https://stackoverflow.com/), [Plotly](https://plotly.com/graphing-libraries/), Udacity, Kaggle, Medium,[freeCodeCamp](https://www.freecodecamp.org/news/how-to-sort-values-in-pandas/), [Geeks for Geeks](https://www.geeksforgeeks.org/) and Github were consulted for this project.  

