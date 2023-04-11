import os

from dash import callback
from dash.dependencies import Input, Output, State
from pandas import read_csv

id_page = "users_registry"

@callback(Output(f"{id_page}_reg_answer", "children"),
          Input(f"{id_page}_reg_accept", "n_clicks"),
          [
            State(f"{id_page}_reg_user", "value"),
            State(f"{id_page}_reg_pass", "value") 
          ])
def auth_display(n_clicks, reg_user, reg_pass):
    reg_answer = ""
    if n_clicks:
        df = read_csv("users.csv")        
        if reg_user in list(df["user"]):
            reg_answer = "El Usuario ya existe"
        else:
            os.mkdir(f"users/{reg_user}")
            df.loc[df.shape[0]] = [reg_user, reg_pass]
            df.to_csv("users.csv", index=False)
            reg_answer =  "Registro completado"
    return [reg_answer] 