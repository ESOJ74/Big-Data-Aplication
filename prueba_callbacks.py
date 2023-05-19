import json
from importlib import import_module
import numpy as np
import plotly.graph_objects as go
from dash import callback, dcc
from dash.dependencies import Input, Output

from assets.my_dash.my_html.my_div import my_div
import os


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NumpyEncoder, self).default(obj)

def save_panel(fig, name_panel):
    with open(f"figures/{name_panel}.json", "w") as file:
        json.dump(fig.to_dict(), file, cls=NumpyEncoder)

@callback(Output("drop_", "options"), Input("url_", "pathname"))
def display_page(pathname):
    return os.listdir("figures")


@callback(Output("app_content_prueba", "children"), Input("drop_", "value"))
def display_page(lista1):    
    divs = []
    for archivo in lista1:
        with open(f"figures/{archivo}", "r") as file:
            loaded_fig_dict = json.load(file)
            figu = go.Figure(loaded_fig_dict)
            divs.append(
                my_div(
                    {
                        "float": "left",
                        "position": "relative",
                        "top": "1%",
                        "width": "49.8%",
                        "height": "49%",
                        "background": "blue",
                    },
                    "app_content",
                    dcc.Graph(figure=figu, style={"width": "99%", "height": "99%"}),
                )
            )
    return divs
