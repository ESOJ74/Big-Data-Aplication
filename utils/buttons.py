from dash import html

from dependencies.classes.my_dash_table import MyDashTable

style_table = {
    "border": "1.5px solid rgba(36, 41, 46, 0.12)",
    "margin-top": "3%",
    "margin-left": "2%",
    "width": "96%",
    "height": "96%",
    "overflowX": "auto",
}

style_data = {
    "padding": "6px",
    "align-items": "center",
    "width": "8vmax",
    "min-width": "8vmax",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "font-size": "0.75vmax",
    "color": "black",
    "border-right": "1.5px solid rgba(36, 41, 46, 0.12)",
    "background": "linear-gradient(90deg, #d3dcdc 0%, #f8f8f8 40%, #d3dcdc 80%)",
}

style_header = {
    "padding": "6px",
    "color": "#143CB8",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "font-size": "0.9vmax",
    "border-bottom": "1.5px solid rgba(36, 41, 46, 0.12)",
    "border-right": "1.5px solid rgba(36, 41, 46, 0.12)",
    "background": "linear-gradient(0deg,#d9fefe 0%, #e4e9e9 80%)",
}

style_cell = {"textAlign": "center"}


def button_apply(df, msg, columns_grouped=0):
    if columns_grouped == 0:
        div = MyDashTable.my_dash_table(
            df.head(15),
            style_table,
            style_data,
            style_header,
            style_cell,
        )
    else:
        div = MyDashTable.my_dash_table_groupby(
            df.head(15),
            columns_grouped,
            style_table,
            style_data,
            style_header,
            style_cell,
        )

    content = [
        div,
        msg,
    ]
    return "Save Changes", content


def button_save(file, action):
    with open(file, "a") as file:
        file.write(action + "\n")
    return "Apply", html.H6(
        "Guardado", style={"color": "white", "font-size": "1vmax", "margin-left": "2%"}
    )
