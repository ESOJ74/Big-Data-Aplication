import dash_bootstrap_components as dbc
from dash import dcc, html

from callbacks.workflow import * # noqa: F403

id_page = "workflow"


content_up = html.Div(
    [
        html.Div("Workflow", className="title-workflow"),
        dcc.Dropdown(
            id=f"{id_page}_drop_file",
            className="dropdown-workflow",
        ),
    ],
    className="panel-up-workflow",
)

content_down = html.Div(
    [
        html.Div(id=f"{id_page}_div_code"),        
        html.Div(
            [
                dbc.Button(
                    "Save",
                    f"{id_page}_apply",
                    className="button-workflow",
                ),
                dbc.Button(
                    "Download file",
                    "btn-download-txt",
                    className="button-workflow",
                ),
                dcc.Download(id="download-text"),
            ],
            className="panel-buttons-workflow"
        ),
    ],
    f"{id_page}_content_down",
)

params = [html.Div(className="no-params")]
