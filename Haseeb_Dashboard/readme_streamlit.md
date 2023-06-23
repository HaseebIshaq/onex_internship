# Sales Data Analysis
## Introduction
The sales data analysis is a summarised example of e-commerce sales data for a retail store, which needs to analyze its sales and derive different relationships,in order to measure the performance of certain products in the market and analyze the sales from a particular location and store outlet.A web application is created here, in the form of an interactive dashboard to do so. The dataset used for this analysis is ***sales_data.csv*** (attached).

### Note
***IMPORTANT NOTE:***
Please note that there are two Python files for this analysis. The main file is named as **streamlit.py** and then there is another file, **Dash.py**, which shows the secondary method for this analysis. You should checkout the **streamlit.py** one for the actual and final results for this analysis. The other file is just the prototype of executing this analysis.

## Working
1. There are several libraries needed to be installed. Following is the format to do so: 
```py
pip install <requirements_streamlit.docx>
```
2. The given code in *streamlit.py* file could be executed on any standardized python environment or IDE e.g. *VScode, Jupyter Notebook etc*, by typing the following command in the terminal:
```py
python streamlit.py
```
3. After running the main code, in your terminal, you have to type a specific streamlit run command to launch the web app on your localhost. ***The web application could also be launched by typing this command directly in the terminal, without executing the above commands.***
```py
streamlit run <file path>
```
4. All of the necessary comments are added with each block of code to easily comprehend its working. 
## Dataset
The dataset was composed of eight columns, **Sr. (receipt no.), Date, Product ID, Store Location,	Store ID, Sale (Percentage of discount), Sale Price (Actual Price),  Price Sold (Price after discount)**. There were 300 rows in total. The dataset also contained some null values for a certain feature.
## General Treatment
Firstly the exploratory data analysis was performed to derive all of the necessary relationships. Any missing values in dataset were replaced accordingly. An additional column of *'Discounted Price'* was also added to deduce the subtracted amount from the actual price, after applying the sales parameter.

In **streamlit.py**, the main library used is streamlit along with pandas and plotly. 
The **streamlit.py** file is the main file for this analysis as the library used in this code, *Streamlit*, allows us to execute more convenient integrated dashboards as compared to *Dash*. Its self designing feature elevated the user's experience of UI/UX.
## Web Dashboard
The created dashboard is highly interactive. There are two main filters to control the sales behaviours. Initially when both of the filters are not applied, the neutral graphs appear on dashboard. These graphs depict the Hot-Selling Products, Top Locations and stores for sales.

The Date filter allows us to analyze statistics for sales for a certain duration. This is achieved by measuring the time count between start and enddate. The location filter allows us to analyze the sales in a particular location. Both of these filters could be applied via dropdown options. 

Their are three perspectives in total to analyze the sales_data relationships. One of them is by only giving the duration and this is independent of store location. The other perspective is visualising relationships with respect to Store Location. Lastly, by putting both filters of location and duration and getting the mutual results.

There are three neutral graphs and five graphs to analyze the sales behaviour with respect to date. Moreover, there are four more plots to depict the relationships with regard to location applied. Lastly, three other graphs are added to visualise the sales features when both of the mentioned filters are marked.
## Results
There could be countless angles to deduce the results and analyze the sales behaviour but the most significant ones are listed below:
- Product 1 and Product 2 have more number of sales than products, 3 and 4.
- Los Angeles has the highest amount of sales while Chicago has the lowest number of sales.
- Top three stores of the month are store no. 301,302 and 401. 
- On the contrary, store no. 102 marked the lowest sales of the month.