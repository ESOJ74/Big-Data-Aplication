import os

from dash import callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div

from ..common_css import *

id_page = "pipe"


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("pipe_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("DataFrame.pipe()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html",
                          target="_blank")
                  ])


@callback([
           Output(f"{id_page}_pipe", "options"),
           Output(f"{id_page}_pipe", "value"),
          ],
          Input("pipe_button", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True,)
def add_data_to_fig(refres, data):  
    pipe = ""   
    list_dir = os.listdir(f"""users/{data["user"]}/pipelines""")
    if len(list_dir) > 0:
        pipe = list_dir[0]   
    return [list_dir, pipe]


@callback(Output(f"{id_page}_div_result", "children", allow_duplicate=True),
          Input(f"{id_page}_pipe", "value"),
          State("main_page_store", "data"),
          prevent_initial_call=True,)
def add_data_to_fig(file_name, data):  
    
    pipe_file = f"""users/{data["user"]}/pipelines/{file_name}"""
    
    with open(pipe_file) as file:
        file = file.readlines()

    obj = [html.P(line, style={"margin-bottom": "0%",
                               "white-space": "pre-wrap"
                               }) for line in file[2:]]    
    return my_div({}, "", obj)


@callback([
           Output("main_page_store", "data", allow_duplicate=True),
           Output(f"{id_page}_button_apply_pipe", "n_clicks"),
          ],
          Input(f"{id_page}_button_apply_pipe", "n_clicks"),
          [
           State(f"{id_page}_pipe", "value"),
           State("main_page_store", "data")
           
          ],
          prevent_initial_call=True,)
def add_data_to_fig(n_clicks, file_name, data):      
    if n_clicks:
        pipe_file = f"""users/{data["user"]}/pipelines/{file_name}"""
        df = read_json(data["df"])
        
        with open(pipe_file, 'r') as file:
            for i, linea in enumerate(file):
                if i > 2:
                    df = eval(linea)    
    
        data["df"] = df.to_json(orient="columns")  
        return [data, 0]
    else:
        raise PreventUpdate
