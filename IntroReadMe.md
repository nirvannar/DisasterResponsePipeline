# Disaster Response Pipeline Project
My second Udacity Project creates a machine learning pipeline to categorize disaster events so that the messages can be viewed by emergency workersabd sent to the appropriate disaster relief agencies

# Table of Contents

* [Installation](#Installation)
* [Project Motivation](#Project-Motivation)
* [File Descriptions and Analyses](#File-Descriptions-and-Analyses)
* [Results](#Results)
* [Licensing, Authors, and Acknowledgements](#Licensing,-Authors,-and-Acknowledgements)


## Installation <a name="Installation"></a>
The code should run with no issues using Python version 3.6.3 using Jupyter Notebook server version 5.7.0 in the Udacity Project Workspace.  Packages that were imported include Pandas,sqlite3, sqlalchemy create_engine, NumPy,  matplotlib.pyplot,  were used.  

  



## Project Motivation <a name="Project-Motivation"></a>
For this project, I used a data set containing real messages that were sent during previous disaster events.    Different visualisations and analyses of data can assist disaster relief organizations such as [The Red Cross](https://www.redcross.org/about-us/our-work/international-services/international-disasters-and-crises.html), [The International Rescue Committee](https://www.rescue.org/) and [the United Nations Office for the Coordination of Humanitarian Affairs](https://www.unocha.org/)

In this course, you've learned and built on your data engineering skills to expand your opportunities and potential as a data scientist. In this project, you'll apply these skills to analyze disaster data from Appen (formally Figure 8) to build a model for an API that classifies disaster messages.

In the Project Workspace, you'll find a data set containing real messages that were sent during disaster events. You will be creating a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency.

Your project will include a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. This project will show off your software skills, including your ability to create basic data pipelines and write clean, organized code!

Below are a few screenshots of the web app.

**_Project Components_**
 
**_ETL Pipeline_** *The Extract, Transform, and Load process reads the dataset, cleans the data, and then store it in a SQLite database.*  
**_Machine Learning Pipeline_** *Hplit the data into a training set and a test set. Then, you will create a machine learning pipeline that uses NLTK, as well as scikit-learn's Pipeline and GridSearchCV to output a final model that uses the message column to predict classifications for 36 categories (multi-output classification). Finally, you will export your model to a pickle file. After completing the notebook, you'll need to include your final machine learning code in train_classifier.py.*  
**_Flask Web App Deployment_** *How can I find the closest volcano and the closest most recently active volcanic island tour for tourists from South Africa?*  



## File Descriptions and Analyses <a name="File-Descriptions-and-Analyses"></a>
**_ETL Pipeline Preparation_**
Two datasets ```messages.csv``` and ```categories.csv``` containing real messages that were sent during disaster events.  These were merged using the common ```'id'```and this combined dataset was assigned to ```df```which was then cleaned.

The .csv file was analysed using a Jupyter Notebook.  There is one notebook available here to showcase work related to the above questions. The notebook is exploratory in searching through the data pertaining to the questions showcased by the notebook title. Markdown cells were used to assist in walking through the thought process for individual steps.  The notebook had 1398 rows of data and 4 columns of quantitative variables.  The total columns were 14 namely Volcano Number,	Volcano Name,	Country,	Primary Volcano Type,	Activity Evidence,	Last Known Eruption,	Region,	Subregion,	Latitude,	Longitude, 	Elevation (m),	Dominant Rock Type and	Tectonic Setting.   The columns of data "Dominant Rock Type" and "Tectonic Setting" contained blanks.  However these 2 columns were not used to obtain results and are excluded from any analysis.  

Pandas DataFrame.hist was used to see the distribution / shape of the data for the quantitative variables.  The only variables were volcano number, latitude, longitude and Elevation (m) that were analysed.  Elevation (m) was normally distributed while latitude had 2 peaks and the longitude and volcano numbers were spread out.

Seaborn pairplot and heatmap were used to check for any correlations between variables.  No strong correlations existed.  Thus no machine mearning models were considered in the analyses.  

**_Data Preparation_**  
The Country column was manipulated to show the name of the country before the "-" so as to count with the first country mentioned before the hyphen.
The Primary Volcano Types which was renamed to Types was manipulated to reflect singular instead of plural words using a combination of the string manipulation techniques of replace() and strip().  Some of the remaining columns names were simplified to enable ease of coding.The columns of data "Dominant Rock Type" and "Tectonic Setting" were not used to obtain results and are excluded from any analysis.


## Results <a name="Results"></a>

**ETL Pipeline** *How can I identify potential travel destinations for enthusiasts of volcano tourism?*  

*This was answered firstly via using Folium and datapane with volcano markers to the world map.*  
A person could chose to refine the travel destination by the most common type of volcano and/or by the country with the most volcanoes and/or Region and/or Elevation above sea level.  To summarise a traveler could choose one or a combination of the Holocene characteristics, or choose the highest or lowest elevation, or simply look at the interactive map to target where to start their travel search.  

**Machine Learning Pipeline** *How can I customise the travel destination for those tourists with no travel restriction?*  
Travel restrictions exist in terms of visa regulations, COVID_19 entry requirements and lockdown levels, availability of international and regional flights, etc. Question 2 was answered by using the results of Question 1 as inputs. A combination of characteristics indicates that Chile had the highest volcanoes in terms of Elevation and 69% (66 of 96) were stratovolcanoes (which is the most common primary type of volcano). In addition Chile is in the Region with the must volcanoes which is South America, and is number 5 on the list of countries with the most volcanoes. In addition *San Pedro de Atacama* is one of the most visited places in Chile's *Atacama* desert.
The Haversine formula was then used to calculate the distances between 2 sets of latitude and longitude points. This distance was calculated from San Pedro de Atacama, to other volcanic locations via a for loop. The closest distance was then calculated using dataframe.min(). This resulted in the selection of *Licancabur*. The closest volcano which had erupted in the last 5 years (2017) was *Lascar* which is at an elevation of 5592m and 70.2km away from San Pedro de Atacama.

**Flask Web App Deployment** *How can I find the closest volcano and the closest most recently active volcanic island tour for tourists from South Africa?*  
Type in the command line as below to run the Flask app.

```python
python run.py
```

```python
# Closest Volcano to Johannesburg

from math import radians, cos, sin, asin, sqrt
def dist(Longitude1,Latitude1,Longitude2,Latitude2 ):
   
    # convert decimal degrees to radians 
    Longitude1,Latitude1, Longitude2,Latitude2  = map(radians, [Longitude1, Latitude1,Longitude2,Latitude2])
    # haversine formula 
    dlon = Longitude2 - Longitude1  
    dlat = Latitude2 - Latitude1 
    a = sin(dlat/2)**2 + cos(Latitude1) * cos(Latitude2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

df['distance'] = [dist(df.Longitude[i],df.Latitude[i], 28.2411459,-26.1366728) 
                  for i in range(len(df))]
df['distance'] = df['distance'].round(decimals=3)

df.head(296)

print(df[df['distance']==df['distance'].min()])
```  


[A Medium blog](https://medium.com/@nirvannsramp/intrepid-explosive-voyages-77f23e47e24e?source=friends_link&sk=b97c94187c9f435b0b955aa12acc408d) was created using the results. 

## Licensing, Authors, and Acknowledgements<a name="Licensing,-Authors,-and-Acknowledgements"></a>
The data was provided by [Appen](https://appen.com/) (formally Figure 8). Scikit-learn.org, Stack Overflow, [Plotly](https://plotly.com/graphing-libraries/), Udacity, Kaggle, Medium,[freeCodeCamp](https://www.freecodecamp.org/news/how-to-sort-values-in-pandas/), [Geeks for Geeks](https://www.geeksforgeeks.org/) and Github were consulted for this project.  

