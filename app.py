from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('data/pink_morsel_sales.csv').sort_values(by="sales")

fig = px.line(df, x="date", y="sales")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales"
)

app.layout = html.Div(children=[
    html.H1(children="Effect of Pink Morsel Price Increase on Sales",
            style={'text-align': 'center'}),

    dcc.Graph(
        id='pink-morsel-sales-graph',
        figure=fig
    )],
    style={'font-family': 'Roboto, sans-serif'}
)

if __name__ == '__main__':
    app.run(debug=True)
