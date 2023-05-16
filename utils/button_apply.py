from dash import html

from assets.common_css import color_boton_1
from assets.my_dash.my_html.my_div import my_div
from utils.create_agGrid import create_adgrid


def button_apply(id_page, df, msg):
    content = [
        my_div({}, "", create_adgrid(f"{id_page}_ag-table", df.head(9))),
        msg,
    ]
    return "Save Changes", content


def button_save(file, action):
    with open(file, "a") as file:
        file.write(action + "\n")
    return "Apply", html.H6("Guardado", style={"color": color_boton_1})
