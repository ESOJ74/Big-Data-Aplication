import subprocess
from datetime import datetime

from dash import callback
from dash.dependencies import Input, Output, State
from pandas import read_json

from assets.my_dash.my_html.my_div import my_div

id_page = "drop_file"

@callback(Output(f"{id_page}_result", "children"),
          Input("drop_file_button", "n_clicks"),
          State("main_page_store", "data"),
          prevent_initial_call=True,)
def add_data_to_fig(refres, data):  
    df = read_json(data["pipeline"])
    try:     
      date = str(datetime.now()).split(".")[0]
      
      with open(f"""pipeline{date}.py""", "w") as file:
          for x in df["codigo"]:
              file.write(x+"\n")     

      subprocess.run(["black", f"""pipeline{date}.py"""], capture_output=True, text=True)      
    except:
        return "No se ha podido descargar el archivo"
     
    return my_div({"margin-left": "3%", "margin-top": "5%"}, "",
                  "Archivo descargado")
