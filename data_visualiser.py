import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the formatted data 
data = pd.read_csv("processed_data.csv")
data = data.sort_values(by="date")

# Initialize the Dash app
app = Dash(__name__)

# layout
app.layout = html.Div(children=[
    html.H1("Pink Morsel Visualizer", style={'textAlign': 'center'}),
    
    # Region picker radio buttons
    dcc.RadioItems(
        id='region-picker',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        style={'textAlign': 'center', 'marginBottom': '20px'}
    ),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update the graph
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(region):
    if region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'] == region]

    fig = px.line(filtered_data, x="date", y="sales", title="Sales Data")
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)