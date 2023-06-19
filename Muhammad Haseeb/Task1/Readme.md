# Sensor Data
## Introduction
The realtionship between the Temperature and Humidity was needed to be measured at different times of the day for the couple of days. This has to be done by using the dataset, ***"Sensor_Data.csv"*** file. 
## Working
1. There are several libraries needed to be installed. Following is the format to do so: 
```py
pip install <requirements.docx>
```
2. The rest of the code is needed to run block by block in *jupyter notebook* or *google colabs*.
3. Each block has comments added to explain its respective working.
 
## Dataset
The dataset was composed of three columns, **Timestamp (including date and time), Temperature and Humidity**. There were initially 29 rows but I increased the number of rows by concatenating random samples of similar given data for upto 309 rows. This was done for improving accuracy. The dataset also contained rows without any values and some null values for a certain feature.
## General Treatment
I started off with exploratory data analysis. I handled missing values by dropping the rows which were not containing any values, later I filled in the *Nan* in the particular column with the mean value of the same column. I loaded the data and extracted all of the necessary parameters, *i.e. mean,median,quartiles and boundary values.* 
## Visualisation
For this part, I used plotly to visualise the  line chart, scatter plot and heatmap. 

For the heatmap and scatterplot, I added two additional features highlighting the hours and the time of day (morning,evening etc). Different colors indicates the difference of different time zones.
## Results
- This conclusion can be derived that Temperature and Humidity displays the positive correlation.
- It means that increase in temperature, also increases the humidity and vice versa. 
- In the afternoon, there is more temperature and humidity as compared to other times of the day. 
- However at night, these two parameters are in moderate ranges.