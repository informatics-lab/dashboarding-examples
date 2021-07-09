import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

app = dash.Dash(__name__)


def make_plot(n, m):
    t = np.linspace(-m*np.pi, m*np.pi, n)
    r = t % n
    x = r * np.sin(t)
    y = r * np.cos(t)
    return x, y


@app.callback(
    Output('spirograph', 'figure'),
    Input('n-slider', 'value'),
    Input('m-slider', 'value')
)
def update_plot(n, m):
    x, y = make_plot(n, m)
    fig = px.line(x=x, y=y, width=800, height=800)
    fig.update_layout()
    return fig


app.layout = html.Div(children=[
    html.H1(children='Spirograph'),
    html.H4(children="Using Plotly / Dash"),
    dcc.Graph(id='spirograph'),
    html.P(children="n"),
    dcc.Slider(
        id="n-slider",
        min=50, max=1000,
        value=100, step=5,
        marks={str(i): str(i) for i in np.arange(50, 1001, 50)}
    ),
    html.P(children="m"),
    dcc.Slider(
        id="m-slider",
        min=2, max=20,
        value=2, step=1,
        marks={str(i): str(i) for i in np.arange(2, 21, 1)}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)