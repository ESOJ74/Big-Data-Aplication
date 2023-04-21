from dash import callback, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pandas import read_csv

from pages.main_page.main_page_css import *
from pages.main_page.main_page_functions import create_callback
from pages.main_page.main_page_lists import (buttons, functions, models,
                                             visualizations)

id_page = "main_page"


@callback([
           Output(f"{id_page}_div_button_left", "hidden", allow_duplicate=True),
           Output(f"{id_page}_div_button_right", "hidden", allow_duplicate=True),
           Output(f"{id_page}_left", "hidden", allow_duplicate=True),
           Output(f"{id_page}_page_content", "style", allow_duplicate=True),
           Output(f"{id_page}_button_left", "n_clicks"),
          ],
          Input(f"{id_page}_button_left", "n_clicks"),
          prevent_initial_call=True,)
def auth_display(n_clicks):
    if n_clicks:
        return  [True, False, False, style_div_content, 0]
    else:
        raise PreventUpdate


@callback([
           Output(f"{id_page}_div_button_left", "hidden", allow_duplicate=True),
           Output(f"{id_page}_div_button_right", "hidden", allow_duplicate=True),
           Output(f"{id_page}_left", "hidden", allow_duplicate=True),
           Output(f"{id_page}_page_content", "style", allow_duplicate=True),
           Output(f"{id_page}_button_right", "n_clicks"),
          ],
          Input(f"{id_page}_button_right", "n_clicks"),
          prevent_initial_call=True,)
def auth_display(n_clicks):
    if n_clicks:
        return  [False, True, True, style_div_content2, 0]
    else:
        raise PreventUpdate

@callback([
           Output(f"{id_page}_left", "hidden"),
           Output(f"{id_page}_div_registry", "hidden"),
           Output(f"{id_page}_store", "data"),
           Output(f"{id_page}_panel_up_left", "children"),
           Output(f"{id_page}_panel_up_right", "children"),
           Output(f"{id_page}_reg_answer", "children"),
           Output(f"{id_page}_div_button_right", "hidden")
          ],
          Input(f"{id_page}_reg_accept", "n_clicks"),
          [
            State(f"{id_page}_reg_user", "value"),
            State(f"{id_page}_reg_pass", "value") 
          ])
def auth_display(n_clicks, reg_user, reg_pass):
    left_hidden = True
    registry_hidden = False
    user_div = ""
    sesion_div = ""
    reg_answer = ""
    data = {}
    button_left_hidden = True
    if n_clicks:
        df = read_csv("users.csv")        
        if reg_user in list(df["user"]):
            password = df[df["user"] == reg_user]["password"].iloc[0]
            if str(password) == str(reg_pass):
                left_hidden = False
                registry_hidden = True
                user_div = html.H6(f"User: {reg_user}", style={"font-weight": "bold", "color": "black"})
                sesion_div = html.A("Cerrar Sesión", href="/", style={"color": "black"})
                data = {"user": reg_user}
                button_left_hidden = False
            else:
                reg_answer = "Contraseña incorrecta"
        else:
            reg_answer =  "Usuario no registrado"
    return [left_hidden, registry_hidden, data, user_div, sesion_div, reg_answer, button_left_hidden] 


create_callback(buttons, "i_o_pages")
create_callback(visualizations, "visualization_pages", "Visualización")
create_callback(functions, "functions_pages", "Función")
create_callback(models, "models_pages", "Modelo")
