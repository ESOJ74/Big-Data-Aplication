from dash import dcc

from assets.my_dash.my_html.my_div import my_div

from .common_css import *


def create_content_layout(id_page, content_left_up, content_left_down, content_right):
    return my_div(
        style_div_main,
        f"{id_page}_content_layout",
        [
            my_div(
                style_content_left,
                f"{id_page}_content_left",
                [
                    my_div(
                        style_content_left_up,
                        f"{id_page}_content_left_up",
                        content_left_up,
                    ),
                    dcc.Loading(
                        id="loading-2",
                        children=my_div({}, f"{id_page}_loading"),
                        type="default",
                        fullscreen=False,
                    ),
                    my_div(
                        style_content_left_down,
                        f"{id_page}_content_left_down",
                        content_left_down,
                    ),
                ],
            ),
            my_div(style_content_right, f"{id_page}_content_right", content_right),
        ],
    )
