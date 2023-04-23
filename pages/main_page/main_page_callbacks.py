from dash import callback, html
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
from pandas import read_csv

from pages.main_page.main_page_css import *
from pages.main_page.main_page_functions import create_callback
from pages.main_page.main_page_lists import (buttons, functions, models,
                                             visualizations)

id_page = "main_page"


@callback([
           Output(f"{id_page}_div_button_cover", "style"),
           Output(f"{id_page}_button_cover", "style"),
           Output(f"{id_page}_button_cover", "children"),
           Output(f"{id_page}_div_middle_left", "hidden", allow_duplicate=True),
           Output(f"{id_page}_page_content", "style")
          ],
          Input(f"{id_page}_button_cover", "n_clicks"),
          prevent_initial_call=True,)
def auth_display(n_clicks):
    if n_clicks % 2 !=0:
        return  [style_div_button_cover_left, style_button_cover_left,
                 DashIconify(
                             icon="ic:baseline-arrow-circle-right",   #2a9fd6
                             width=30
                ), True, style_div_content2]
    else:
        return  [style_div_button_cover_right, style_button_cover_right,
                 DashIconify(
                             icon="ic:baseline-arrow-circle-left",   #2a9fd6
                             width=30
                 ), False, style_div_content]


@callback([
           Output(f"{id_page}_div_middle_left", "hidden", allow_duplicate=True),
           Output(f"{id_page}_div_registry", "hidden"),
           Output(f"{id_page}_store", "data"),
           Output(f"{id_page}_panel_up_left", "children"),
           Output(f"{id_page}_panel_up_right", "children"),
           Output(f"{id_page}_reg_answer", "children")
          ],
          Input(f"{id_page}_reg_accept", "n_clicks"),
          [
            State(f"{id_page}_reg_user", "value"),
            State(f"{id_page}_reg_pass", "value") 
          ],
          prevent_initial_call=True,)
def auth_display(n_clicks, reg_user, reg_pass):
    left_hidden = True
    registry_hidden = False
    user_div = ""
    sesion_div = ""
    reg_answer = ""
    data = {}

    if n_clicks:
        df = read_csv("users.csv")        
        if reg_user in list(df["user"]):
            password = df[df["user"] == reg_user]["password"].iloc[0]
            if str(password) == str(reg_pass):
                left_hidden = False
                registry_hidden = True
                user_div = html.H6(f"User: {reg_user}", style={"font-weight": "bold", "color": "#acf4ed"})
                sesion_div = html.A("Cerrar Sesión", href="/", style={"color": "black"})
                data = {"user": reg_user}
            else:
                reg_answer = "Contraseña incorrecta"
        else:
            reg_answer =  "Usuario no registrado"
    return [left_hidden, registry_hidden, data, user_div, sesion_div, reg_answer] 


create_callback(buttons, "i_o_pages")
create_callback(visualizations, "visualization_pages", "Visualización")
create_callback(functions, "functions_pages", "Función")
create_callback(models, "models_pages", "Modelo")
