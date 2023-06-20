import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)  # initializing dash app

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("sales_data.csv")
df['Store Location'].fillna('Other', inplace=True)
print(df['Store Location'].value_counts())

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([
    html.H1("Web Application Dashboards for the sales data (w.r.t. Location)",
            style={'text-align': 'center', 'background-color': '#99ccff'}),

    html.Hr(),
    dcc.Dropdown(id="Select Store Location",
                 options=[
                     {"label": "Los Angeles", "value": 'Los Angeles'},
                     {"label": "New York", "value": 'New York'},
                     {"label": "Nevada", "value": 'Nevada'},
                     {"label": "San Francisco", "value": 'San Francisco'}],
                 multi=False,
                 value='Nevada',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container2', children=[]),
    html.Br(),

    dcc.Graph(id='dash_map1', figure={}),
    dcc.Graph(id='dash_map2', figure={}),
    dcc.Graph(id='dash_map3', figure={}),
    dcc.Graph(id='dash_map4', figure={})
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container2', component_property='children'),
     Output(component_id='dash_map1', component_property='figure'),
     Output(component_id='dash_map2', component_property='figure'),
     Output(component_id='dash_map3', component_property='figure'),
     Output(component_id='dash_map4', component_property='figure')],
    [Input(component_id='Select Store Location', component_property='value')]
)
def update_graph(option_slctd2):
    print(option_slctd2)
    print(type(option_slctd2))

    container2 = "The location chosen by user was: {}".format(option_slctd2)

    dff = df.copy()
    dff = dff[dff['Store Location'] == option_slctd2]
    # dff = dff[dff['Store ID'] == 101]

    # Plotly Express
    fig1 = px.bar(
        dff.groupby('Date')['Price Sold'].sum().reset_index(),
        x='Date',
        y="Price Sold",
        title='Earned Revenue on a Particular Date'
    )

    # *could be added with both filters*
    fig2 = px.bar(
        dff.groupby('Store ID')['Price Sold'].sum().reset_index(),
        x="Store ID",
        y='Price Sold',
        title='Revenue of a Single Store in particular Location')

    fig3 = px.bar(
        dff,
        x='Date',
        y='Product ID',
        color='Product ID',
        title='Particular Product sold on all Dates w.r.t. Given Location'
    )

    fig4 = px.bar(
        dff['Product ID'].value_counts().reset_index(),
        x='index',
        y='Product ID',
        labels={'index': 'Product ID', 'Product ID': 'No. Of Products Sold'},
        title='Particular Product Sale from a Given Location'
    )

    return container2, fig1, fig2, fig3, fig4


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
