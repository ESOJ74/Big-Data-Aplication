import os
from datetime import datetime
from dash import callback, html, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json
import shutil
from .workflow_button_css import *
from dash.exceptions import PreventUpdate

id_page = "workflow"


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
    Output(f"{id_page}_button_save", "children"),
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
     Output("main_page_store", "data", allow_duplicate=True)
    ],
    Input(f"{id_page}_workflow", "value"),
    State("main_page_store", "data"),
    prevent_initial_call=True,
)
def add_data_to_fig(drop_workflow, data):
    if drop_workflow == "Actual":  
        pipe_file = f"""users/{data["user"]}/workflow.txt"""
    else:
        pipe_file = f"""users/{data["user"]}/pipelines/{drop_workflow}"""   
    
    with open(pipe_file) as file:
            codigo_python = file.read()   
    obj = dcc.Markdown('```python\n' + codigo_python + '\n```', style={"width": "45%"})     
    data["pipeline"] = codigo_python  
    return [html.H6(obj), data]


@callback(
    [
        Output(f"{id_page}_button_save", "children", allow_duplicate=True),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_div_code", "children", allow_duplicate=True),
    ],
    Input(f"{id_page}_button_save", "n_clicks"),
    [
        State(f"{id_page}_button_save", "children"),
        State("main_page_store", "data"),
    ],
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks, name_button, data):    
    
    if n_clicks:
        if name_button == "Save":
            date = str(datetime.now()).split('.')[0]
            path_file = f"""users/{data["user"]}/workflow.txt"""
            path_end = f"""users/{data["user"]}/pipelines/{data['name_df']}_{date}.txt"""
            shutil.copy2(path_file, path_end)        
        else:     
            import pandas as pd #se utiliza en eval()

            df = read_json(data["df"])    
            df_pipeline = data["pipeline"]            
            
            for line in df_pipeline.split("\n"):
                if len(line) > 1:
                    if line[0] == "i" or line[:4] == "df =":
                        pass
                    else:
                        df = eval(line) 
               
            data["df"] = df.to_json(orient="columns") 
            with open(f"""users/{data["user"]}/workflow.txt""", "w") as file:
                for line in df_pipeline.split("\n"):
                    file.write(line + "\n")             
        return [name_button, data, "Aplicado"]
    else:
        raise PreventUpdate
