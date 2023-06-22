import os

from dash import Dash, callback, dcc, html
from dash.dependencies import Input, Output
from pages import login_layout, registry_layout
from pages_conf.main_page import main_page_conf
from pages_conf.import_pages import *

id_page = "initial_layout"

app = Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    [
        dcc.Location(id=f"{id_page}_url"),
        html.Div("", f"{id_page}_content", className="panel-content-app"),
    ],
    className="panel-app",
)


# Update page content
import contextlib
@callback(
        Output(f"{id_page}_content", "children"),
        Input(f"{id_page}_url", "pathname")
)
def display_page(pathname):
    pages_list = {
        "/": login_layout.layout,
        "/registro": registry_layout.layout,
        "/app": main_page_conf.layout,
    }

    if pathname == "/":
        with contextlib.suppress(OSError):
            os.remove("user.txt")
    if pathname == "/app" and not os.path.exists("user.txt"):
        pathname = "/"

    if pathname in pages_list:
        return pages_list[pathname]
    

if __name__ == "__main__":
    app.run_server(debug=True)