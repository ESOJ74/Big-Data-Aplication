import os
import subprocess

from dash import callback, html
from dash.dependencies import Input, Output, State
from pandas import read_json

from .common_css import *

id_page = "show_pipeline"

@callback(Output(f"{id_page}_div_graph", "children"),
          Input("show_pipeline_button", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True,)
def add_data_to_fig(refres, data):  

    df = read_json(data["pipeline"])
   
    with open("output.txt", "w") as file:
        for x in df["codigo"]:
            file.write(x+"\n")        

    #subprocess.run(["black", "output.txt"], capture_output=True, text=True)

    obj = []
    with open("output.txt", "r") as file:        
        for line in file:      
            if len(line) > 5:                
                obj.append(html.P(line, style={"margin-bottom": "0%","white-space": "pre-wrap"}))
            
    os.remove("output.txt")
     
    return [html.H6(obj, style=style_msg)]