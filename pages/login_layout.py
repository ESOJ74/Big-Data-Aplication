import csv

from dash import callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from dependencies.classes.my_login import UserLogin

id_page = "login"

user_login = UserLogin(id_page, "panel-login")
user_login.set_title("Login")
user_login.set_pathname("registro", "registro")
layout = user_login.user_login()


@callback(
    Output("initial_layout_url", "pathname"),
    Input(f"{id_page}_reg_answer", "children"),
)
def change_url(content_children):
    if content_children == "ok":
        return "/app"
    raise PreventUpdate


@callback(
    Output(f"{id_page}_reg_answer", "children"),
    Input(f"{id_page}_reg_accept", "n_clicks"),
    [State(f"{id_page}_reg_user", "value"), State(f"{id_page}_reg_pass", "value")],
    prevent_initial_call=True,
)
def auth_display(n_clicks, reg_user, reg_pass):
    if not reg_user or not reg_pass:
        return "Faltan Datos"

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["user"] == reg_user:
                if row["password"] == reg_pass:
                    with open("user.txt", "w") as user_file:
                        user_file.write(reg_user)
                    return "ok"
                else:
                    return "Contraseña incorrecta"

    return f"El Usuario {reg_user} no está registrado"
