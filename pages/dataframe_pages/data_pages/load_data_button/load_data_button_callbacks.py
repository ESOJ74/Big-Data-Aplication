import os

from dash import Input, Output, State, callback, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_sql
from sqlalchemy import create_engine

from assets.layout_templates.main_page.common_css import *
from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div
from utils.create_callback_hidden_button_cover import create_callback_hidden_button_cover
from utils.parse_contents import parse_contents
from utils.read_data import read_data

from .load_data_button_css import *

id_page = "load_data"


create_callback_hidden_button_cover(f"{id_page}_content_down", True)


# botones
@callback(
    Output(f"{id_page}_content_down", "children"),
    Input(f"{id_page}_archivos", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def load_data(n_clicks, data):
    obj = html.H6(
        "No tiene archivos",
        style={"margin-left": "4%", "margin-top": "2%", "color": color_boton_1},
    )
    options = os.listdir(f"""users/{data["user"]}/data""")
    if len(options) > 0:
        obj = my_div(
            {"width": "100%", "height": "90%"},
            "",
            my_div(
                style_div_dropdown_archivos,
                f"{id_page}_div_archivos",
                [
                    my_div(
                        style_selector,
                        "",
                        my_dropdown(
                            f"{id_page}_drop_file",
                            {"background": background_in_dropdown},
                            options=options,
                            value=options[0],
                        ),
                    ),
                    my_button(
                        f"{id_page}_aceptar",
                        "Load",
                        style_boton_aceptar,
                        className="btn btn-outline-warning",
                        color="black",
                    ),
                ],
            ),
        )
    return obj


@callback(
    [
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"main_page_div_functions", "hidden"),
        Output(f"main_page_div_data", "hidden", allow_duplicate=True),
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
        html.H6(f"DataFrame {input_value.split('.')[0]} preparado", style=style_msg),
    ]


@callback(
    Output(f"{id_page}_content_down", "children", allow_duplicate=True),
    Input(f"{id_page}_database", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def load_data(click_db, data):
    return my_div(
        style_div_dropdown_db,
        f"{id_page}_div_db",
        [
            my_div(
                s_selector_db,
                "",
                [
                    html.H6("User", style=style_title_db),
                    dcc.Input(id=f"{id_page}_user", style=style_input),
                    html.H6("Password", style=style_title_db),
                    dcc.Input(id=f"{id_page}_password", style=style_input),
                    html.H6("Host", style=style_title_db),
                    dcc.Input(id=f"{id_page}_host", style=style_input),
                    html.H6("Port", style=style_title_db),
                    dcc.Input(id=f"{id_page}_port", style=style_input),
                    html.H6("DataBase", style=style_title_db),
                    dcc.Input(id=f"{id_page}_bd", style=style_input),
                    html.H6("Schema", style=style_title_db),
                    dcc.Input(id=f"{id_page}_schema", style=style_input),
                    html.H6("Table", style=style_title_db),
                    dcc.Input(id=f"{id_page}_table", style=style_input),
                ],
            ),
            my_button(
                f"{id_page}_aceptar_db",
                "Aceptar",
                style_boton_aceptar,
                className="btn btn-outline-warning",
                color="black",
            ),
        ],
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
            msg = my_div(
                {"margin-left": "22vmax"},
                "",
                html.H6(
                    f"Archivo guardado como {table}.csv", style={"color": color_boton_1}
                ),
            )
            engine.dispose()
            msg = html.H6(f"Archivo guardardo como {table}.csv", style=style_msg)
        except:
            msg = html.H6("Datos Erroneos", style=style_msg)
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
    return my_div(
        style_div_up_load,
        "",
        [
            dcc.Upload(
                id="upload-data",
                children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
                style=style_dcc_upload,
                # Allow multiple files to be uploaded
                multiple=True,
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
        return html.H6(msg, style=style_msg)
    else:
        raise PreventUpdate
