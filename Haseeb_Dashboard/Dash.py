import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)  # initializing dash app

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("sales_data.csv")
df['Discounted Amount'] = df['Sale Price'] - df['Price Sold']
df['Store Location'].fillna('Other', inplace=True)

# ------------------------------------------------------------------------------
# App layout

app.layout = html.Div(
    style={'background-color': '#153d5a', 'padding': '20px'}
)

# the detailed layout
app.layout = html.Div([
    # heading
    html.H1("Web Application Dashboards for the sales data (w.r.t. Date)",
            style={'text-align': 'center', 'background-color': '#99ccff', 'color': '#153d5a',
                   'padding': '10px', 'margin-bottom': '20px', 'border-radius': '10px'}),
    html.Hr(),
    # Dropdown menu
    html.Div([
        dcc.Dropdown(
            id="SelectDate",
            options=[
                {"label": "1/2/2023", "value": '1/2/2023'},
                {"label": "1/3/2023", "value": '1/3/2023'},
                {"label": "1/4/2023", "value": '1/4/2023'},
                {"label": "1/5/2023", "value": '1/5/2023'},
                {"label": "None", "value": 'None'},
            ],
            multi=False,
            value='None',
            style={'width': "40%", 'color': '#333',
                   'background-color': '#f2f2f2', 'margin': 'auto', 'border': 'none'},
        ),
        dcc.Dropdown(
            id="Select Store Location",
            options=[
                {"label": "New York", "value": "New York"},
                {"label": "San Francisco", "value": "San Francisco"},
                {"label": "Nevada", "value": "Nevada"}
            ],
            multi=False,
            value=None,
            style={'width': "40%", 'color': '#333',
                   'background-color': '#f2f2f2', 'margin': 'auto', 'border': 'none'},
        ),
    ],
        style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'gap': '20px'}
    ),
    html.Div(id='output_container1', children=[], style={
             'color': '#f0edf7', 'align-items': 'center'}),
    html.Div(id='output_container2', children=[], style={
             'color': '#f0edf7'}),

    html.Br(),
    html.Div(
        children=[
            # Graphs arrangements
            html.Div([
                dcc.Graph(id='dash_map1', figure={}),
                dcc.Graph(id='dash_map2', figure={}),
                dcc.Graph(id='dash_map3', figure={}),
            ],
                style={
                    'display': 'grid',
                    'grid-template-columns': '1fr 1fr 1fr',
                    'gap': '20px',
                    'background-color': 'rgba(255, 255, 255, 0.8)',
                    'border-radius': '10px',
                    'padding': '20px',
                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.3)'
            },
            ),
            html.Div([
                dcc.Graph(id='dash_map4', figure={}),
                dcc.Graph(id='dash_map5', figure={}),
            ],
                style={
                    'display': 'grid',
                    'grid-template-columns': '1fr 1fr',
                    'gap': '20px',
                    'background-color': 'rgba(255, 255, 255, 0.8)',
                    'border-radius': '10px',
                    'padding': '20px',
                    'box-shadow': '0 2px 5px rgba(0, 0, 0, 0.3)'
            },
            ),
        ],
        style={
            'display': 'grid',
            'grid-template-rows': 'auto auto',
            'gap': '20px'
        },
    ),
],
    style={'background-color': '#153d5a', 'padding': '20px'}
)

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components

# Connection established and same goes for inputs and outputs of web application


@app.callback(
    [Output(component_id='output_container1', component_property='children'),
     Output(component_id='output_container2', component_property='children'),
     Output(component_id='dash_map1', component_property='figure'),
     Output(component_id='dash_map2', component_property='figure'),
     Output(component_id='dash_map3', component_property='figure'),
     Output(component_id='dash_map4', component_property='figure'),
     Output(component_id='dash_map5', component_property='figure')],
    [Input(component_id='SelectDate', component_property='value'),
     Input(component_id='Select Store Location', component_property='value')]
)
# the main method for execution
def update_graph(option_slctd1, option_slctd2):
    container1 = "The date chosen by the user was: {}".format(option_slctd1)
    container2 = "The Location chosen by the user was: {}".format(
        option_slctd2)

    dff = df.copy()
    dff = dff[dff["Date"] == option_slctd1]
    dff = dff[dff["Store Location"] == option_slctd2]

    # All possible graphs defined
    fig1 = px.bar(
        dff['Store Location'].value_counts().reset_index(),
        x='index',
        y='Store Location',
        labels={'index': 'Store Location', 'Store Location': 'No of Sales'},
        title='No. of Sales from Each Location on a Given Date',
        color_discrete_sequence=['#FFA500']
    )

    fig2 = px.line(
        dff.groupby('Store ID')['Price Sold'].sum().reset_index(),
        y='Price Sold',
        x='Store ID',
        labels={'Price Sold': "Earned Revenue"},
        markers=True,
        title='Amount of Sales from Each Store on a Given Date'
    )

    fig3 = px.bar(
        dff['Product ID'].value_counts().reset_index(),
        x='index',
        y='Product ID',
        labels={'index': 'Product ID', 'Product ID': "No. of Sales"},
        title='Particular Product Sale on a Given Date',
        color_discrete_sequence=['#f44336']
    )

    fig4 = px.bar(
        dff.groupby('Store Location')['Price Sold'].sum().reset_index(),
        x='Store Location',
        y='Price Sold',
        title="""Sales of Particular Amount w.r.t. Location on a Given Date""",
        color_discrete_sequence=['#1e5008']
    )

    fig5 = px.scatter(
        dff.groupby('Store ID')['Price Sold'].sum().reset_index(),
        x="Store ID",
        y='Price Sold',
        title='Revenue of a Single Store in particular Location'
    )

    return container1, container2, fig1, fig2, fig3, fig4, fig5


# The final main code
if __name__ == '__main__':
    app.run_server(debug=True)
