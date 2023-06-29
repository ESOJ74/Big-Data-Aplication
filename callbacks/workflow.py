import os
import shutil
from datetime import datetime

from pandas import read_json
from dash.exceptions import PreventUpdate
from dash import Input, Output, State, callback, dcc
from utils.utils_functions import create_msg
import pathlib

id_page = "workflow"

global file_path
file_path = ""



@callback(
    [
        Output(f"{id_page}_drop_file", "options"),
        Output(f"{id_page}_drop_file", "value"),
    ],
    Input("workflow", "n_clicks"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(refres, data):
    list_dir = os.listdir(f"""users/{data["user"]}/pipelines""")
    return [["Actual"] + list_dir, "Actual"]


@callback(
    Output(f"{id_page}_apply", "children"),
    Input(f"{id_page}_drop_file", "value"),
    prevent_initial_call=True,
)
def change_button_apply(drop_workflow):
    return "Save" if drop_workflow == "Actual" else "Apply"


@callback(
    [
        Output(f"{id_page}_div_code", "children"),
        Output("main_page_store", "data", allow_duplicate=True),
    ],
    Input(f"{id_page}_drop_file", "value"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def drop_file(drop_workflow, data):
    global file_path
    if drop_workflow == "Actual":
        pipe_file = f"""users/{data["user"]}/workflow.txt"""
    else:
        pipe_file = f"""users/{data["user"]}/pipelines/{drop_workflow}"""
    file_path = pipe_file
    codigo_python = pathlib.Path(pipe_file).read_text()
    data["pipeline"] = codigo_python
    obj = dcc.Markdown(
        "```python\n" + codigo_python + "```",
        className="code-workflow",
        highlight_config={"theme": "dark"},
    )
    return [obj, data]


@callback(
    [
        Output(f"{id_page}_apply", "children", allow_duplicate=True),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_div_code", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_apply", "n_clicks"),
    [
        State(f"{id_page}_apply", "children"),
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
def button_apply(n_clicks, name_button, data):
    if not n_clicks:
        raise PreventUpdate
    if name_button == "Save":
        date = str(datetime.now()).split(".")[0]
        path_file = f"""users/{data["user"]}/workflow.txt"""
        path_end = (
            f"""users/{data["user"]}/pipelines/{data['name_df']}-{date}.txt"""
        )
        shutil.copy2(path_file, path_end)
        msg = "Workflow guardado"
    else:
        import pandas as pd  # se utiliza en eval()  # noqa: F401

        df = read_json(data["df"])
        df_pipeline = data["pipeline"]

        for line in df_pipeline.split("\n")[3:]:
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
        create_msg(msg),
    ]


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
