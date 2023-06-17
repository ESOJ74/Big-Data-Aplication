from sqlalchemy import create_engine
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import os
from dash.exceptions import PreventUpdate
from utils.in_out import read_data
from utils.utils_functions import create_msg

id_page = "load_data"


@callback(
    Output(f"{id_page}_content_down", "children"),
    Input(f"{id_page}_archivos", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def load_data(n_clicks, data):
    obj = create_msg("No tiene archivos")
    options = os.listdir(f"""users/{data["user"]}/data""")
    if len(options) > 0:
        obj = [
            dcc.Dropdown(
                id=f"{id_page}_drop_file",
                options=options,
                value=options[0],
                className="dropdown-load-data",
            ),
            dbc.Button(
                "Load",
                f"{id_page}_aceptar",
                className="btn-load_data",
            ),
        ]
    return obj


@callback(
    [
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"main_page_div_functionalities", "hidden", allow_duplicate=True),
        Output(f"main_page_panel_load_save", "hidden", allow_duplicate=True),
        Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_aceptar", "n_clicks"),
    [State(f"{id_page}_drop_file", "value"), State("main_page_store", "data")],
    prevent_initial_call=True,
)
def load_data(accept, input_value, data):
    if accept:
        path = f"""users/{data["user"]}/data/{input_value}"""
        data["df"] = read_data(input_value.split(".")[-1], path)
        data["name_df"] = input_value.split(".")[0]
        ext = input_value.split(".")[1]

        actions = [
            "import pandas as pd",
            "",
            f"""df = pd.read_{ext}("{input_value}")""",
        ]

        with open(f"""users/{data["user"]}/workflow.txt""", "w") as file:
            for action in actions:
                file.write(action + "\n")

        div_data_hidden = True
    else:
        raise PreventUpdate
    return [
        data,
        False,
        div_data_hidden,
        create_msg(
            f"DataFrame {input_value.split('.')[0]} preparado"
        ),
    ]
