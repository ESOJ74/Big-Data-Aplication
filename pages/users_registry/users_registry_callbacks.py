import os

from dash import callback, html
from dash.dependencies import Input, Output, State
from pandas import read_csv

from assets.common_css import *

id_page = "users_registry"


@callback(
    Output(f"{id_page}_reg_answer", "children"),
    Input(f"{id_page}_reg_accept", "n_clicks"),
    [State(f"{id_page}_reg_user", "value"), State(f"{id_page}_reg_pass", "value")],
    prevent_initial_call=True,
)
def auth_display(n_clicks, reg_user, reg_pass):
    if reg_user is None or reg_pass is None:
        reg_answer = html.H6("Faltan Datos", style={"color": color_boton_1})
    elif len(reg_user) < 1 or len(reg_pass) < 1:
        reg_answer = html.H6("Faltan Datos", style={"color": color_boton_1})
    else:
        df = read_csv("users.csv")
        if reg_user in list(df["user"]):
            reg_answer = html.H6("El Usuario ya existe", style={"color": color_boton_1})
        else:
            os.mkdir(f"users/{reg_user}")
            os.mkdir(f"users/{reg_user}/data")
            os.mkdir(f"users/{reg_user}/models")
            os.mkdir(f"users/{reg_user}/fotos")
            os.mkdir(f"users/{reg_user}/pipelines")
            df.loc[df.shape[0]] = [reg_user, reg_pass]
            df.to_csv("users.csv", index=False)
            reg_answer = html.H6("Registro completado", style={"color": color_boton_1})
    return reg_answer
