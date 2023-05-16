from dash import dcc, html

from assets.my_dash.my_dbc.my_button import my_button
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.my_dash.my_html.my_div import my_div

from .create_panel_params_css import *


def create_select(
    id_page,
    id_param,
    options=[],
    value="",
    multi=False,
    s_div_selector=style_div_selector2,
    s_selector=style_selector2,
    s_params=style_params2,
):
    return my_div(
        s_div_selector,
        "",
        [
            html.H6(id_param, style=s_params),
            my_div(
                s_selector,
                "",
                my_dropdown(
                    f"{id_page}_{id_param}",
                    {"background": background_light},
                    options=options,
                    value=value,
                    multi=multi,
                ),
            ),
        ],
    )


def create_param_drop(id_page, id_param, options=[], value="", multi=False):
    return create_select(
        id_page,
        id_param,
        options,
        value,
        multi,
        style_div_selector,
        style_selector,
        style_params,
    )


def create_param_input(id_page, id_param, value=1):
    return my_div(
        style_div_input,
        "",
        [
            html.A(id_param, style=style_params),
            dcc.Input(
                id=f"{id_page}_{id_param}",
                style=style_input,
                value=value,
            ),
        ],
    )


def create_param_buttons_text_graph(id_page):
    return my_div(
        style_div_buttons,
        "",
        [
            my_button(
                f"{id_page}_text",
                "Text",
                style_button,
                className="btn btn-warning",
                color="black",
                n_clicks=1,
            ),
            my_button(
                f"{id_page}_graph",
                "Graph",
                style_button,
                className="btn btn-outline-warning",
                color="black",
            ),
        ],
    )


def create_buttom_refresh(id_page):
    return my_button(
        f"{id_page}_refresh",
        "Apply",
        style_button_refresh,
        className="btn btn-outline-primary",
        color=color_boton_1,
    )
