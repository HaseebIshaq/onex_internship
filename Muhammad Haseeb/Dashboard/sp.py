import pandas as pd
import plotly.express as px
import streamlit as st

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("sales_data.csv")
dff = df.copy()
df['Discounted Amount'] = df['Sale Price'] - df['Price Sold']
df['Store Location'].fillna('Other', inplace=True)

# App layout
st.markdown("<h1 style='font-size: 24px; text-align: center;'>Web Application Dashboards for the sales data </h1>", unsafe_allow_html=True)
st.markdown("---")

# Filter options
# date_options = ['1/2/2023', '1/3/2023', '1/4/2023', '1/5/2023']
date_options = df['Date'].unique()
all_locations = ['New York', 'San Francisco', 'Nevada', 'Los Angeles']

# Sidebar filters
st.sidebar.markdown("## Filters")
date_filter = st.sidebar.checkbox("Select Date")
location_filter = st.sidebar.checkbox("Filter by Store Location")

selected_location = None
selected_date = None

if location_filter:
    selected_location = st.sidebar.selectbox(
        "Select Store Location", all_locations)

if date_filter:
    selected_date = st.sidebar.selectbox('Select Date', date_options)

# Display filter selections
st.sidebar.markdown("### Filter Selections")
st.sidebar.write("Selected Date:", selected_date)
st.sidebar.write("Selected Store Location:", selected_location)

filtered_data = df

# Apply filters
if selected_date and selected_location:
    filtered_data = df[(df["Date"] == selected_date) & (
        df["Store Location"] == selected_location)]
elif selected_date:
    filtered_data = filtered_data[filtered_data["Date"] == selected_date]
elif selected_location:
    filtered_data = filtered_data[filtered_data["Store Location"]
                                  == selected_location]
else:
    st.markdown("<h2 style='font-size: 20px; text-align: center;'>DataFrame of Sales Data, which is used for this analysis. </h2>", unsafe_allow_html=True)
    st.write(dff)  # Display the DataFrame with details

# Graphs w.r.t. Date
fig1 = px.bar(
    filtered_data['Store Location'].value_counts().reset_index(),
    x='index',
    y='Store Location',
    labels={'index': 'Store Location', 'Store Location': 'No of Sales'},
    title='No. of Products sold from Each Location on A Given Date',
    color_discrete_sequence=['#FFA500']
)
# col1.plotly_chart(fig1)

fig2 = px.line(
    filtered_data.groupby('Store ID')['Price Sold'].sum().reset_index(),
    y='Price Sold',
    x='Store ID',
    labels={'Price Sold': "Earned Revenue"},
    markers=True,
    title='Amount of Sales from Each Store on A Given Date'
)
# col1.plotly_chart(fig2)

fig3 = px.bar(
    filtered_data['Product ID'].value_counts().reset_index(),
    x='index',
    y='Product ID',
    labels={'index': 'Product ID', 'Product ID': "No. of Sales"},
    title='Particular Product Sale on A Given Date',
    color_discrete_sequence=['#f44336']
)
# col1.plotly_chart(fig3)

fig4 = px.bar(
    filtered_data.groupby('Store Location')['Price Sold'].sum().reset_index(),
    x='Store Location',
    y='Price Sold',
    title='Sales of Particular Amount w.r.t. Location on a Given Date',
    color_discrete_sequence=['#1e5008']
)
# col2.plotly_chart(fig4)

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

# fig10 = px.bar(
#     filtered_data.groupby('Date')['Product ID'].value_counts().reset_index(),
#     x='Date',
#     y='Product ID',
#     labels={'Product ID':'Total No. of Products'},
#     title='Total No. of Products Sold on each Date from a Given Location',
#     color_discrete_sequence=['#FFA500']
# )

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

# Create a container for the grid layout
container = st.container()

if selected_date and selected_location:
    with container:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(fig10, use_container_width=True)
        with col2:
            st.plotly_chart(fig11, use_container_width=True)
        with col3:
            st.plotly_chart(fig2, use_container_width=True)
elif selected_date:
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
