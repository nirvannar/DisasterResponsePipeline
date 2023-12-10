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
For this project, I used a data set from [Appen](https://appen.com/) (formally Figure 8) containing real messages that were sent during previous disaster events.    Different visualisations and analyses of data can assist disaster relief organizations such as [The Red Cross](https://www.redcross.org/about-us/our-work/international-services/international-disasters-and-crises.html), [The International Rescue Committee](https://www.rescue.org/) and [the United Nations Office for the Coordination of Humanitarian Affairs](https://www.unocha.org/)

The disaster data set  was used to build a model for an API that the classifies disaster messages. A machine learning pipeline was created to categorize these events so that the messages could be sent to an appropriate disaster relief agency. This project included a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display three visualizations of the data. 

Below are a few screenshots of the web app.



**_Project Components_**
 
**_1. ETL Pipeline_** *The Extract, Transform, and Load process reads the dataset, cleans the data, and then store it in a SQLite database.*  
**_2. Machine Learning Pipeline_** *Split the data into a training set and a test set. Then, you will create a machine learning pipeline that uses NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model that uses the message column to predict classifications for 36 categories (multi-output classification). Finally, you will export your model to a pickle file. After completing the notebook, you'll need to include your final machine learning code in train_classifier.py.*  
**_3. Flask Web App Deployment_** *The flask web app was customised Data visualizations were created using Plotly in the web app*  



## File Descriptions and Analyses <a name="File-Descriptions-and-Analyses"></a>
**_ETL Pipeline Preparation_**
Two datasets ```messages.csv``` and ```categories.csv``` containing real messages that were sent during disaster events were merged using the common ```'id'```.  This combined dataset was assigned to ```df```which was then cleaned. Finally it was stored in a SQLite database ```DisasterResponse.db```.



**_ML Data Preparation_**  
The data was split into a training set and a test set. A machine learning pipeline was created that used NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model that uses the message column to predict classifications for 36 categories (multi-output classification). The model was exported to a pickle file ```classifier,pkl```. The final machine learning code in ```train_classifier.py```.


## Results <a name="Results"></a>

**ETL Pipeline** *How can I identify potential travel destinations for enthusiasts of volcano tourism?*  

*This was answered firstly via using Folium and datapane with volcano markers to the world map.*  


**Machine Learning Pipeline** *How can I customise the travel destination for those tourists with no travel restriction?*  


**Flask Web App Deployment** *The web app runs without errors*  
Type in the command line Project Workspace IDE as below to run the Flask app.

```python
python run.py
```

```python
 

[A Medium blog](https://medium.com/@nirvannsramp/intrepid-explosive-voyages-77f23e47e24e?source=friends_link&sk=b97c94187c9f435b0b955aa12acc408d) was created using the results. 

## Licensing, Authors, and Acknowledgements<a name="Licensing,-Authors,-and-Acknowledgements"></a>
The data was provided by [Appen](https://appen.com/) (formally Figure 8). Scikit-learn.org, Stack Overflow, [Plotly](https://plotly.com/graphing-libraries/), Udacity, Kaggle, Medium,[freeCodeCamp](https://www.freecodecamp.org/news/how-to-sort-values-in-pandas/), [Geeks for Geeks](https://www.geeksforgeeks.org/) and Github were consulted for this project.  

