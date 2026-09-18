# Dashboards
import dash
from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard tutorial"),

    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {
                    "x": [1, 2, 3, 4, 5],
                    "y": [5, 4, 7, 4, 8],
                    "type": "line",
                    "name": "Trucks"
                },
                {
                    "x": [1, 2, 3, 4, 5],
                    "y": [6, 3, 5, 3, 7],
                    "type": "bar",
                    "name": "Ships"
                }
            ],
            "layout": {
                "title": "Basic dashboard"
            }
        }
    )
])

app.run(debug=False, port=8050)