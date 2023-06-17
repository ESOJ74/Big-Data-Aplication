from dash import dcc, html
from pandas import set_option


def create_obj(msg, fig, state_button, axis=0):
    set_option("display.max_columns", 500)
    set_option("display.width", 1000)
    obj = html.Div(
        html.Pre(msg, className="panel-funtions-text"),        
        style={"position": "relative", "top": "0%"},
    )
    if state_button == "btn-on":
        if axis == 0:
            obj = dcc.Graph(
                figure=fig,
                style={"height": "100%"},
            )
        else:
            obj = html.H6(
                "Gráfico disponible solo para axis=0",
                style={
                    "color": "white",
                    "font-size": "1vmax",
                    "margin-left": "2%",
                },
            )
    return obj


def create_msg(msg):
    return html.Div(
        msg.__str__(),
        style={
            "position": "relative",
            "top": "4%",
            "left": "5%",
            "color": "white",
            "font-family": "inherit",
            "font-size": "1vmax",
            "font-weight": "bold",
        },
    )
