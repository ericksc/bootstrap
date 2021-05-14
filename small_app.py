import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.P('hola'),
    html.P('a todos'),
])

app.run_server(debug=False)