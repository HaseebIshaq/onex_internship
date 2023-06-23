# Sales Data Analysis
## Introduction
The sales data analysis is a summarised example of e-commerce sales data for a retail store, which needs to analyze its sales and derive different relationships,in order to measure the performance of certain products in the market and analyze the sales from a particular location and store outlet.A web application is created here, in the form of an interactive dashboard to do so. The dataset used for this analysis is ***sales_data.csv*** (attached).
## Working (Dash.py)
1. There are several libraries needed to be installed. Following is the format to do so: 
```py
pip install <requirements_Dash.docx>
```
2. The given code in *Dash.py* file could be executed on any standardized python environment or IDE e.g. *VScode, Jupyter Notebook etc*, by typing the following command in the terminal:
```py
python streamlit.py
```
3. All of the necessary comments are added with each block of code to easily comprehend its working.
## Dataset
The dataset was composed of eight columns, **Sr. (receipt no.), Date, Product ID, Store Location,	Store ID, Sale (Percentage of discount), Sale Price (Actual Price),  Price Sold (Price after discount)**. There were 300 rows in total. The dataset also contained some null values for a certain feature.
## General Treatment
Firstly the exploratory data analysis was performed to derive all of the necessary relationships. Any missing values in dataset were replaced accordingly. An additional column of *'Discounted Price'* was also added to deduce the subtracted amount from the actual price, after applying the sales parameter.

In **dash_test3,py**, plotly,pandas and Dash libraries were used. The Dash library allowed us to integrate html and css with python code, to design a dashboard.  

## Web Dashboard
The created dashboard is highly interactive. There are two main filters to control the sales behaviours. These filters are of date and location. The designed graphs are modified automatically whenever the filters of date and location are applied or ammended. Both of these filters appear as the dropdown menus and all of the unique occurances of date and location appear as the options for those two dropdowns.

In total, there are five graphs given to analyze the relationships in **sales_data.csv**, with regard to date and location filters.

## Results
There could be multiple angles to deduce the results and analyze the sales behaviour, each depending on the various combinations of date and location applied.