import pandas as pd
import plotly.express as px
import streamlit as st

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("sales_data.csv")
print(df.info())
dff = df.copy()

# Adding another column of Discounted Amount
df['Discounted Amount'] = df['Sale Price'] - df['Price Sold']
# Dealing Missing Values
df['Store Location'].fillna('Other', inplace=True)

# App layout
st.markdown("<h1 style='font-size: 24px; text-align: center;'>Web Application Dashboards for the sales data </h1>", unsafe_allow_html=True)
st.markdown("---")

# Filter options (Drop Down Options)
# date_options = pd.to_datetime(df['Date']).dt.date.unique()
date_options = df['Date'].unique()
all_locations = df['Store Location'].unique()
# all_locations = ['New York', 'San Francisco', 'Nevada', 'Los Angeles']

# Sidebar filters (removing/adding filters with checkboxes)
st.sidebar.markdown("## Filters")
date_filter = st.sidebar.checkbox("Select Date")
location_filter = st.sidebar.checkbox("Select Store Location")

selected_location = None
start_date = None
end_date = None

# When checkbox marked, then Dropdown appears
if location_filter:
    selected_location = st.sidebar.selectbox(
        "Select Store Location", all_locations)

if date_filter:
    st.sidebar.markdown("### Select Date Range")
    start_date = st.sidebar.selectbox('Start Date', date_options)
    end_date = st.sidebar.selectbox('End Date', date_options)

# Display filter selections in side margin
st.sidebar.markdown("### Filter Selections")
st.sidebar.write("Start Date:", start_date)
st.sidebar.write("End Date:", end_date)
st.sidebar.write("Selected Store Location:", selected_location)

filtered_data = df

# Apply filters w.r.t. location and date possibilities
if start_date and end_date:
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_data = df[(pd.to_datetime(df['Date']).dt.date >= start_date) & (
        pd.to_datetime(df['Date']).dt.date <= end_date)]
elif start_date:
    start_date = pd.to_datetime(start_date)
    filtered_data = filtered_data[pd.to_datetime(
        filtered_data['Date']).dt.date >= start_date]
elif end_date:
    end_date = pd.to_datetime(end_date)
    filtered_data = filtered_data[pd.to_datetime(
        filtered_data['Date']).dt.date <= end_date]

if selected_location:
    filtered_data = filtered_data[filtered_data['Store Location']
                                  == selected_location]

# Graphs w.r.t. Date
fig1 = px.bar(
    filtered_data['Store Location'].value_counts().reset_index(),
    x='index',
    y='Store Location',
    labels={'index': 'Store Location', 'Store Location': 'No of Sales'},
    title='No. of Products sold from Each Location on A Given Date',
    color_discrete_sequence=['#FFA500']
)

fig2 = px.line(
    filtered_data.groupby('Store ID')['Price Sold'].sum().reset_index(),
    y='Price Sold',
    x='Store ID',
    labels={'Price Sold': "Earned Revenue"},
    markers=True,
    title='Amount of Sales from Each Store on A Given Date'
)

fig3 = px.bar(
    filtered_data['Product ID'].value_counts().reset_index(),
    x='index',
    y='Product ID',
    labels={'index': 'Product ID', 'Product ID': "No. of Sales"},
    title='Particular Product Sale on A Given Date',
    color_discrete_sequence=['#f44336']
)

fig4 = px.bar(
    filtered_data.groupby('Store Location')['Price Sold'].sum().reset_index(),
    x='Store Location',
    y='Price Sold',
    title='Sales of Particular Amount w.r.t. Location on a Given Date',
    color_discrete_sequence=['#1e5008']
)

fig5 = px.pie(
    filtered_data.groupby('Store Location')[
        'Discounted Amount'].sum().reset_index(),
    values='Discounted Amount',
    names='Store Location',
    title='Discount of Particular Amount w.r.t. Location on a Given Date'
)

# Graphs w.r.t. Location
fig6 = px.bar(
    filtered_data.groupby('Date')['Price Sold'].sum().reset_index(),
    x='Date',
    y="Price Sold",
    title='Earned Revenue on a Particular Date',
    color_discrete_sequence=['#f44336']
)

fig7 = px.pie(
    filtered_data.groupby('Store ID')['Price Sold'].sum().reset_index(),
    names="Store ID",
    values='Price Sold',
    title='Revenue of a Single Store in particular Location'
)

fig8 = px.bar(
    filtered_data,
    x='Date',
    y='Product ID',
    color='Product ID',
    title='Particular Product sold on all Dates w.r.t. Given Location'
)

fig9 = px.bar(
    filtered_data['Product ID'].value_counts().reset_index(),
    x='index',
    y='Product ID',
    labels={'index': 'Product ID', 'Product ID': 'No. Of Products Sold'},
    title='Particular Product Sale from a Given Location',
    color_discrete_sequence=['#1e5008']
)

# Graphs when Both filters applied (Also include fig2)
fig10 = px.pie(
    filtered_data['Store ID'].value_counts().reset_index(),
    names='index',
    values='Store ID',
    title='No. of sales from a store'
)

fig11 = px.bar(
    filtered_data['Product ID'].value_counts().reset_index(),
    x='index',
    y='Product ID',
    labels={'index': 'Product ID', 'Product ID': 'No. of Products Sold'},
    title='No. of products sold'
)

# Neutral Graphs
fig12 = px.pie(
    filtered_data['Product ID'].value_counts().reset_index(),
    values='Product ID',
    names='index',
    title='Top Selling Products'
)

fig13 = px.pie(
    filtered_data['Store Location'].value_counts().reset_index(),
    names='index',
    values='Store Location',
    title='Top Locations'
)

fig14 = px.pie(
    filtered_data['Store ID'].value_counts().reset_index(),
    names='index',
    values='Store ID',
    title='Top Stores'
)

# Create a container for the grid layout 
container = st.container()

# Displaying Graphs w.r.t. selection of filters (conditional)
if start_date and end_date and selected_location:
    with container:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(fig10, use_container_width=True)
        with col2:
            st.plotly_chart(fig11, use_container_width=True)
        with col3:
            st.plotly_chart(fig2, use_container_width=True)
elif start_date and end_date:
    with container:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.plotly_chart(fig3, use_container_width=True)
        with col3:
            st.plotly_chart(fig4, use_container_width=True)
    with container:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig5, use_container_width=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)
elif selected_location:
    with container:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig6, use_container_width=True)
        with col2:
            st.plotly_chart(fig7, use_container_width=True)
    with container:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig8, use_container_width=True)
        with col2:
            st.plotly_chart(fig9, use_container_width=True)
else:
    with container:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(fig12, use_container_width=True)
        with col2:
            st.plotly_chart(fig13, use_container_width=True)
        with col3:
            st.plotly_chart(fig14, use_container_width=True)
