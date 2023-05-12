import os
import shutil
from datetime import datetime

from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_json

from utils.create_callback_hidden_button_cover import create_callback_hidden_button_cover

from .workflow_button_css import *

id_page = "workflow"
global file_path
file_path = ""

create_callback_hidden_button_cover(f"{id_page}_workflow", True)


@callback(
    [
        Output(f"{id_page}_workflow", "options"),
        Output(f"{id_page}_workflow", "value"),
    ],
    Input("workflow_button", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(refres, data):
    list_dir = os.listdir(f"""users/{data["user"]}/pipelines""")
    return [["Actual"] + list_dir, "Actual"]


@callback(
    Output(f"{id_page}_button_save1", "children"),
    Input(f"{id_page}_workflow", "value"),
    prevent_initial_call=True,
)
def add_data_to_fig(drop_workflow):
    if drop_workflow == "Actual":
        return "Save"
    return "Apply"


@callback(
    [
        Output(f"{id_page}_div_code", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
    ],
    Input(f"{id_page}_workflow", "value"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(drop_workflow, data):
    global file_path
    if drop_workflow == "Actual":
        pipe_file = f"""users/{data["user"]}/workflow.txt"""
        file_path = pipe_file
    else:
        pipe_file = f"""users/{data["user"]}/pipelines/{drop_workflow}"""
        file_path = pipe_file

    with open(pipe_file) as file:
        codigo_python = file.read()
    obj = dcc.Markdown(
        "```python\n" + codigo_python + "```",
        style=style_div_markdown,
        highlight_config={"theme": "dark"},
    )
    data["pipeline"] = codigo_python
    return [html.H6(obj), data]


@callback(
    [
        Output(f"{id_page}_button_save1", "children", allow_duplicate=True),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_div_code", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_button_save1", "n_clicks"),
    [
        State(f"{id_page}_button_save1", "children"),
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, name_button, data):
    if n_clicks:
        if name_button == "Save":
            date = str(datetime.now()).split(".")[0]
            path_file = f"""users/{data["user"]}/workflow.txt"""
            path_end = (
                f"""users/{data["user"]}/pipelines/{data['name_df']}-{date}.txt"""
            )
            shutil.copy2(path_file, path_end)
            msg = "Workflow guardado"
        else:
            import pandas as pd  # se utiliza en eval()

            df = read_json(data["df"])
            df_pipeline = data["pipeline"]

            for x, line in enumerate(df_pipeline.split("\n")[3:]):
                if len(line) > 1:
                    line = line.replace("df =", "")
                    df = eval(line)
            data["df"] = df.to_json(orient="columns")

            with open(f"""users/{data["user"]}/workflow.txt""", "w") as file:
                for line in df_pipeline.split("\n"):
                    file.write(line + "\n")
            msg = "Workflow Aplicado"
        return [
            name_button,
            data,
            html.H6(msg, style=style_msg),
        ]
    else:
        raise PreventUpdate


@callback(
    Output("download-text", "data"),
    Input("btn-download-txt", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def func(n_clicks, data):
    global file_path
    filename = (
        file_path.split(".")[0]
        .replace("_", "")
        .replace("users/", "")
        .replace("pipelines/", "")
        .replace(f"{data['user']}/", "")
    )
    filename = filename
    return dcc.send_file(file_path, filename=f"{filename}.py")
