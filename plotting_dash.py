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

df = data_get()
print(df)
# Vaccines 
# Deaths 
# Cases
# 

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.Label(['Covid-19 Data']),

        # Dropdown to switch between new and cumulative cases
        dcc.Dropdown(id='cumnew_dropdown',
            options=[
                {'label':'New Values', 'value':["dailyCases","dailyDeaths", "newPeopleVaccinatedFirstDoseByPublishDate", "newPeopleVaccinatedSecondDoseByPublishDate"]},
                {'label':'Cumulative Values', 'value':["cumulativeCases", "cumulativeDeaths", "cumPeopleVaccinatedFirstDoseByPublishDate", "cumPeopleVaccinatedSecondDoseByPublishDate" ]}
            ],
            value=["dailyCases","dailyDeaths", "newPeopleVaccinatedFirstDoseByPublishDate", "newPeopleVaccinatedSecondDoseByPublishDate"]
            
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
    graph = px.line(dff, x='date', y=cumnew_dropdown)
    return graph

if __name__ == "__main__":
    app.run_server(debug=False)

