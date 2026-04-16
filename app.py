import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the processed sales data from Task 2
df = pd.read_csv("output.csv")

# Convert the date column to actual datetime objects so Plotly sorts them correctly
df["date"] = pd.to_datetime(df["date"])

# Build the line chart — one line per region, x-axis is date, y-axis is sales
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Daily Sales by Region",
    labels={"date": "Date", "sales": "Sales ($)", "region": "Region"},
)

# Add a vertical line marking the price increase on 15 Jan 2021
# This makes it visually obvious whether sales rose or fell after the change
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top right",
)

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig),
])

if __name__ == "__main__":
    app.run(debug=True)
