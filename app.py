from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

DATA_PATH = 'data/pink_morsel_sales.csv'
COLORS = {
    'primary': '#F8F8F8',
    'secondary-white': '#FCFCFC',
    'border-grey': '#CCCCCC',
    'pink': '#FFDED4'
}

app = Dash(__name__)
df = pd.read_csv(DATA_PATH).sort_values(by="date")

fig = px.line(df, x="date", y="sales")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales"
)

header = html.H1(
    id="title-header",
    children="Effect of Pink Morsel Price Increase on Sales",
    style={'text-align': 'center',
           'padding-top': '2rem'}
)

graph = dcc.Graph(
    id='pink-morsel-sales-graph',
    figure=fig,
    style={'padding': '20px'}
)

region_filter = dcc.RadioItems(
    ['north', 'south', 'east', 'west', 'all'],
    'all',
    id="region-filter",
    inline=True,
    style={'display': 'flex',
           'align-items': 'center,',
           'background': COLORS['secondary-white'],
           'padding': '10px 20px 10px 20px',
           'border-radius': '0px 6px 6px 0px'
    }
)

region_filter_wrapper = html.Div(
    id='filter-container',
    children=[
        html.H6(children="Filter by Region",
                style={'color': 'slate grey',
                       'background': COLORS['pink'],
                       'display': 'flex',
                       'align-items': 'center',
                       'padding': '13.5px',
                       'margin-left': '4.5%'
                      }
                ),

        region_filter,
    ],
    style={
           'display': 'flex',
           'justify-content': 'left',
           'align-items': 'center',
           'border-radius': '0px 6px 6px 0px',
           'text-align': 'center'
    }
)


app.layout = html.Div(
    [
        header,
        graph,
        region_filter_wrapper
    ],
    style={'font-family': 'Roboto, sans-serif',
           'background': COLORS['primary'],
           'border': f"0.2px solid {COLORS['border-grey']}"
    }
)

@callback(
    Output('pink-morsel-sales-graph', 'figure'),
    Input('region-filter', 'value'))
def update_figure(selected_region):
    default_df = df
    if selected_region != "all":
        filtered_df = df[df.region == selected_region]
        fig = px.line(filtered_df, x='date', y='sales', color='region')
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Total Sales",
            transition_duration=300)
        return fig
    else:
        fig = px.line(default_df, x='date', y='sales', color="region")
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Total Sales",
            transition_duration=300)
        return fig


if __name__ == '__main__':
    app.run(debug=True)
