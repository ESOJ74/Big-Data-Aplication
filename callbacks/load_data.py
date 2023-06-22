import os

import dash_bootstrap_components as dbc
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_sql
from sqlalchemy import create_engine

from utils.in_out import read_data
from utils.parse_contents import parse_contents
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
        Output("main_page_div_functionalities", "hidden", allow_duplicate=True),
        Output("main_page_panel_load_save", "hidden", allow_duplicate=True),
        Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_aceptar", "n_clicks"),
    [
        State(f"{id_page}_drop_file", "value"),
        State("main_page_store", "data")
    ],
    prevent_initial_call=True,
)
def load_data(accept, input_value, data):
    if not accept:
        raise PreventUpdate
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
    return [
        data,
        False,
        div_data_hidden,
        create_msg(f"DataFrame {input_value.split('.')[0]} preparado"),
    ]


@callback(
    Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    Input(f"{id_page}_database", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def load_data(click_db, data):
    return html.Div(
        [
            html.Div("User", className="h6-input"),
            dcc.Input(id=f"{id_page}_user", className="input-database"),
            html.Div("Password", className="h6-input"),
            dcc.Input(id=f"{id_page}_password", className="input-database"),
            html.Div("Host", className="h6-input"),
            dcc.Input(id=f"{id_page}_host", className="input-database"),
            html.Div("Port", className="h6-input"),
            dcc.Input(id=f"{id_page}_port", className="input-database"),
            html.Div("DataBase", className="h6-input"),
            dcc.Input(id=f"{id_page}_bd", className="input-database"),
            html.Div("Schema", className="h6-input"),
            dcc.Input(id=f"{id_page}_schema", className="input-database"),
            html.Div("Table", className="h6-input"),
            dcc.Input(id=f"{id_page}_table", className="input-database"),
            dbc.Button(
                "Aceptar",
                f"{id_page}_aceptar_db",
                className="button-database",
            ),
        ],
        f"{id_page}_div_db",
        className="panel-database",
    )


@callback(
    Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    Input(f"{id_page}_aceptar_db", "n_clicks"),
    [
        State(f"{id_page}_user", "value"),
        State(f"{id_page}_password", "value"),
        State(f"{id_page}_host", "value"),
        State(f"{id_page}_port", "value"),
        State(f"{id_page}_bd", "value"),
        State(f"{id_page}_schema", "value"),
        State(f"{id_page}_table", "value"),
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
def load_data(n_clicks, user, password, host, port, bd, schema, table, data):
    if n_clicks:
        try:
            engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{bd}")
            query = f"select * from {table}"
            if schema:
                query = f"select * from {schema}.{table}"
            read_sql(query, engine).to_csv(f"""users/{data["user"]}/data/{table}.csv""")
            engine.dispose()
            msg = create_msg(f"Archivo guardardo como {table}.csv")
        except Exception:
            msg = create_msg("Datos Erroneos")
        return msg
    else:
        raise PreventUpdate


# up_file from local
@callback(
    Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    Input(f"{id_page}_up_file", "n_clicks"),
    prevent_initial_call=True,
)
def load_data(n_clicks):
    return html.Div(
        [
            dcc.Upload(
                id="upload-data",
                children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                # Allow multiple files to be uploaded
                multiple=True,
                className="panel-up-load",
            ),
        ],
    )


@callback(
    Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def update_output(list_of_contents, list_of_names, data):
    if list_of_contents is not None:
        msg = [
            parse_contents(c, n, data) for c, n in zip(list_of_contents, list_of_names)
        ]
        return create_msg(msg)
    else:
        raise PreventUpdate
