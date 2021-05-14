import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P("This card has some text content, but not much else"),
            dbc.Button("Go somewhere", color="primary", id='boton_izquierdo' , n_clicks=0),
        ]
    )
)


second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This card also has some text content and not much else, but "
                "it is twice as wide as the first card."
            ),
            dbc.Button("Go somewhere", color="primary"),
            html.Div(id='contenedor_derecho')
        ]
    )
)


cards = dbc.Row([dbc.Col(first_card, width=4),
                 dbc.Col(second_card, width=8)])

app.layout = html.Div(cards)

@app.callback(Output('contenedor_derecho', 'children'),
              Input('boton_izquierdo', 'n_clicks'))
def patito1(n_clicks):
    return f'El botón se ha presionado {n_clicks} veces'


if __name__ == "__main__":
    app.run_server(debug=True)