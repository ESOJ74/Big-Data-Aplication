from dash import html

from assets.common_css import color_boton_1
from assets.my_dash.my_dash_table.my_dash_table import (
    my_dash_table,
    my_dash_table_groupby,
)
from assets.my_dash.my_html.my_div import my_div


def button_apply(id_page, df, msg, columns_grouped=0):
    if columns_grouped == 0:
        div = my_div({}, "", my_dash_table(df.head(15)))
    else:
        div = my_div({}, "", my_dash_table_groupby(df.head(15), columns_grouped))

    content = [
        div,
        msg,
    ]
    return "Save Changes", content


def button_save(file, action):
    with open(file, "a") as file:
        file.write(action + "\n")
    return "Apply", html.H6("Guardado", style={"color": color_boton_1})
