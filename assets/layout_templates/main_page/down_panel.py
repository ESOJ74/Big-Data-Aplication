from .main_page_css import *


def down_panel():
    return my_div(
        style_down_panel,
        "",
        [
            my_div(
                style_down_panel_html_A,
                "",
                html.A(
                    "GitHub",
                    href="https://github.com/ESOJ74/Big-Data-Aplication",
                    style={"color": color_boton_1},
                    target="_blank",
                ),
            ),
            my_div(
                style_down_panel_html_A,
                "",
                html.A(
                    "ChatGPT",
                    href="https://chat.openai.com/",
                    style={"color": color_boton_1},
                    target="_blank",
                ),
            ),
            my_div(
                style_down_panel_html_A,
                "",
                html.A(
                    "Phind",
                    href="https://www.phind.com/",
                    style={"color": color_boton_1},
                    target="_blank",
                ),
            ),
        ],
        className="alert-primary",
    )
