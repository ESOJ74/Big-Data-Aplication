from dash import callback, html
from dash.dependencies import Input, Output, State
from pandas import read_json
import subprocess
from assets.my_dash.my_html.my_div import my_div
id_page = "show_pipeline"
import os

id_page = "drop_file"
@callback(
    [
      Output(f"{id_page}_result", "children"),
    ],
    Input("drop_file_button", "n_clicks"),
    [ 
      State("main_page_store", "data"),
    ],
    prevent_initial_call=True,)
def add_data_to_fig(refres, data):  
    df = read_json(data["pipeline"])
    try:
      with open("pipeline.py", "w") as file:
          for x in df["codigo"]:
              file.write(x+"\n")     

      subprocess.run(["black", "pipeline.py"], capture_output=True, text=True)
   
      obj = "Archivo descargado"
    except:
        obj = "No se ha pdido descargar el archivo"
     
    return [my_div({"margin-left": "3%", "margin-top": "10%"}, "", obj)]