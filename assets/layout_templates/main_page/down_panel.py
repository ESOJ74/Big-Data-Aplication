from .main_page_css import *


def down_panel():
    return my_div(
        style_down_panel,
        "",
        [
            my_div(
                {"float": "left", "margin-left": "2%"},
                "",
                html.A(
                    "GitHub",
                    href="https://github.com/ESOJ74/Big-Data-Aplication",
                    style={"color": "black"},
                    target="_blank",
                ),
            ),
            my_div(
                {"float": "left", "margin-left": "2%"},
                "",
                html.A(
                    "ChatGPT",
                    href="https://chat.openai.com/",
                    style={"color": "black"},
                    target="_blank",
                ),
            ),
            my_div(
                {"float": "left", "margin-left": "2%"},
                "",
                html.A(
                    "Phind",
                    href="https://www.phind.com/",
                    style={"color": "black"},
                    target="_blank",
                ),
            ),
        ],
        className="alert-primary",
    )
