from dash import Input, Output, callback, html

from assets.common_css import *
from assets.my_dash.my_html.my_div import my_div

style_div_title = {
    "text-align": "center",
    "width": "100%",
    "height": "100%",
    "background": background_dark,
}

style_title = {
    "font-weight": "bold",
    "color": color_boton_1,
}


def create_callback_content_up(name_button, is_dataFrame=True):
    @callback(
        Output(f"{name_button}_content_up", "children"),
        Input(f"{name_button}_button", "n_clicks"),
        prevent_initial_call=True,
    )
    def second_callback(n_clicks):
        href = f"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.{name_button}.html"
        if not is_dataFrame:
            href = f"https://pandas.pydata.org/docs/reference/api/pandas.{name_button}.html"
        return my_div(
            style_div_title,
            "",
            [
                html.H5(f"DataFrame.{name_button}()", style=style_title),
                html.A(
                    "Documentacion",
                    href=href,
                    target="_blank",
                ),
            ],
        )


def create_callback_content_up_plotly(name_button, path):
    @callback(
        Output(f"{name_button}_content_up", "children"),
        Input(f"{name_button}_button", "n_clicks"),
        prevent_initial_call=True,
    )
    def second_callback(n_clicks):
        href = f"https://plotly.com/python/{path}/"
        return my_div(
            style_div_title,
            "",
            [
                html.H5(f"DataFrame.{name_button}()", style=style_title),
                html.A(
                    "Documentacion",
                    href=href,
                    target="_blank",
                ),
            ],
        )
