import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the formatted data from Task 2
data = pd.read_csv("processed_data.csv")
data = data.sort_values(by="date")

# Initialize the Dash app
app = Dash(__name__)

# Create the line chart with x, y coordinates and title
fig = px.line(
    data, 
    x="date", 
    y="sales", 
    title="Pink morsel sales before and after price increase"
)
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Sales ($)")

# Define the app layout (Header + Graph)
app.layout = html.Div(children=[
    html.H1(
        children="Pink Morsel Visualizer", 
        style={'textAlign': 'center'}
    ),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)