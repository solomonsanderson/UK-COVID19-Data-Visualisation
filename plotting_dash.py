'''
plotting data on a plotly dash window.
'''

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from data_get import data_get
from rolling_average import rolling_average


df = data_get()
print(df.head())
daily_values = ["dailyCases","dailyDeaths", "newPeopleVaccinatedFirstDoseByPublishDate", "newPeopleVaccinatedSecondDoseByPublishDate"]
cumulative_values = ["cumulativeCases", "cumulativeDeaths", "cumPeopleVaccinatedFirstDoseByPublishDate", "cumPeopleVaccinatedSecondDoseByPublishDate" ]

for value in daily_values:
    ra = rolling_average(df[value], 7)
    
    df[f'{value}-7dra'] = ra['7dayavg']




app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.Label(['Covid-19 Data']),

        # Dropdown to switch between new and cumulative cases
        dcc.Dropdown(id='cumnew_dropdown',
            options=[
                {'label':'New Values', 'value':daily_values},
                {'label':'Cumulative Values', 'value': cumulative_values}
            ],
            value=daily_values
            
        ),
    ]),

    html.Div([dcc.Graph(id='graph')
    ]),
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='cumnew_dropdown', component_property='value')]
)

def update_graph(cumnew_dropdown):
    dff = df
    print(dff.columns)
    graph = px.line(dff, x='date', y=cumnew_dropdown)
    return graph

if __name__ == "__main__":
    app.run_server(debug=False)

