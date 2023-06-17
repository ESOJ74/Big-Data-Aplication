import os

from dash import callback
from dash.dependencies import Input, Output, State
from pandas import read_csv

from dependencies.classes.my_login import UserLogin

id_page = "users_registry"

user_login = UserLogin(id_page, "panel-login")
user_login.set_title("Sign In")
user_login.set_pathname("login", "")
layout = user_login.user_login()


@callback(
    Output(f"{id_page}_reg_answer", "children"),
    Input(f"{id_page}_reg_accept", "n_clicks"),
    [State(f"{id_page}_reg_user", "value"), State(f"{id_page}_reg_pass", "value")],
    prevent_initial_call=True,
)
def auth_display(n_clicks, reg_user, reg_pass):
    if not reg_user or not reg_pass:
        return "Faltan Datos"

    df = read_csv("users.csv")
    if reg_user in df["user"].values:
        return "El Usuario ya existe"

    user_dir = f"users/{reg_user}"
    os.makedirs(user_dir, exist_ok=True)
    subdirectories = ["data", "models", "fotos", "pipelines"]
    for subdirectory in subdirectories:
        os.makedirs(os.path.join(user_dir, subdirectory))

    df.loc[df.shape[0]] = [reg_user, reg_pass]
    df.to_csv("users.csv", index=False)

    return "Registro completado"
