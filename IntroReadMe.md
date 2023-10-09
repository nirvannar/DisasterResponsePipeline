# Intrepid Explosive Voyages
My first Udacity Project based on CRISP-DM to assist volcano tourists to plan their travels.
# Table of Contents

* [Installation](#Installation)
* [Project Motivation](#Project-Motivation)
* [File Descriptions and Analyses](#File-Descriptions-and-Analyses)
* [Results](#Results)
* [Licensing, Authors, and Acknowledgements](#Licensing,-Authors,-and-Acknowledgements)


## Installation <a name="Installation"></a>
The code should run with no issues using Python versions 3.8.8 using Jupyter Notebook server version 6.3.0.  Numpy, Pandas, matplotlib.pyplot, math, seaborn, wordcount, Datapane and Folium libraries were used.  A datapane account must be created and then the API token created and viewed at https://datapane.com/settings/  

Datapane must then be installed as below

```python
pip install -U datapane
```

## Project Motivation <a name="Project-Motivation"></a>
For this project, I was interestested in using the characteristcs of Holocene volcanoes for the purpose of Volcano tourism.  A data science approach was taken using the CRISP-DM process.  A combination of the characteristics and the tourists location and base and appetite for distance travel will allow the traveller to use a combination of analyses to pick the locations for leisure travel purposes.  

**_Business Problem Understanding_**
 
**_Question 1_** *How can I identify potential travel destinations for enthusiasts of volcano tourism?*  
**_Question 2_** *How can I customise the travel destination for those tourists with no travel restriction?*  
**_Question 3_** *How can I find the closest volcano and the closest most recently active volcanic island tour for tourists from South Africa?*  



## File Descriptions and Analyses <a name="File-Descriptions-and-Analyses"></a>
**_Data Understanding_**
I was interestested in using Smithsonian Institution data from the Global Volcanism Program entitled Volcanoes of the World 4.10.1, downloaded on 24 Jul 2021 at 11:16 AM	as a .csv file to use characteristcs of Holocene volcanoes for the purpose of Volcano tourism. 

The .csv file was analysed using a Jupyter Notebook.  There is one notebook available here to showcase work related to the above questions. The notebook is exploratory in searching through the data pertaining to the questions showcased by the notebook title. Markdown cells were used to assist in walking through the thought process for individual steps.  The notebook had 1398 rows of data and 4 columns of quantitative variables.  The total columns were 14 namely Volcano Number,	Volcano Name,	Country,	Primary Volcano Type,	Activity Evidence,	Last Known Eruption,	Region,	Subregion,	Latitude,	Longitude, 	Elevation (m),	Dominant Rock Type and	Tectonic Setting.   The columns of data "Dominant Rock Type" and "Tectonic Setting" contained blanks.  However these 2 columns were not used to obtain results and are excluded from any analysis.  

Pandas DataFrame.hist was used to see the distribution / shape of the data for the quantitative variables.  The only variables were volcano number, latitude, longitude and Elevation (m) that were analysed.  Elevation (m) was normally distributed while latitude had 2 peaks and the longitude and volcano numbers were spread out.

Seaborn pairplot and heatmap were used to check for any correlations between variables.  No strong correlations existed.  Thus no machine mearning models were considered in the analyses.  

**_Data Preparation_**  
The Country column was manipulated to show the name of the country before the "-" so as to count with the first country mentioned before the hyphen.
The Primary Volcano Types which was renamed to Types was manipulated to reflect singular instead of plural words using a combination of the string manipulation techniques of replace() and strip().  Some of the remaining columns names were simplified to enable ease of coding.The columns of data "Dominant Rock Type" and "Tectonic Setting" were not used to obtain results and are excluded from any analysis.


## Results <a name="Results"></a>

**Question 1** *How can I identify potential travel destinations for enthusiasts of volcano tourism?*  

*This was answered firstly via using Folium and datapane with volcano markers to the world map.*  
A person could chose to refine the travel destination by the most common type of volcano and/or by the country with the most volcanoes and/or Region and/or Elevation above sea level.  To summarise a traveler could choose one or a combination of the Holocene characteristics, or choose the highest or lowest elevation, or simply look at the interactive map to target where to start their travel search.  

**Question 2** *How can I customise the travel destination for those tourists with no travel restriction?*  
Travel restrictions exist in terms of visa regulations, COVID_19 entry requirements and lockdown levels, availability of international and regional flights, etc. Question 2 was answered by using the results of Question 1 as inputs. A combination of characteristics indicates that Chile had the highest volcanoes in terms of Elevation and 69% (66 of 96) were stratovolcanoes (which is the most common primary type of volcano). In addition Chile is in the Region with the must volcanoes which is South America, and is number 5 on the list of countries with the most volcanoes. In addition *San Pedro de Atacama* is one of the most visited places in Chile's *Atacama* desert.
The Haversine formula was then used to calculate the distances between 2 sets of latitude and longitude points. This distance was calculated from San Pedro de Atacama, to other volcanic locations via a for loop. The closest distance was then calculated using dataframe.min(). This resulted in the selection of *Licancabur*. The closest volcano which had erupted in the last 5 years (2017) was *Lascar* which is at an elevation of 5592m and 70.2km away from San Pedro de Atacama.

**Question 3** *How can I find the closest volcano and the closest most recently active volcanic island tour for tourists from South Africa?*  
The interactive map shows the closest volcanos in the area around South Africa. The Haversine formula was used to calculate the distances from OR Tambo International Airport (in Johannesburg), to other volcanic locations via a for loop. The closest volcano to Johannesburg is the Stratovolcano *Kyejo* in Tanzania.  
The closest active volcanic island was found using a combination of characteristics including elevation from sea level (0m) to 3000m, eruption in 2021, located in the Indian Ocean and within 3000km away from Johannesburg resulted in selecting the shield volcano *Piton de la Fournaise*.

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
The data was downloaded from the Smithsonian Institution Global Volcanism Program. Stack Overflow, Kaggle, Medium and Github were consulted for syntax references.  
The Volcano marker used in the Folium map was created by Joris Hoogendoorn from the Noun Project
