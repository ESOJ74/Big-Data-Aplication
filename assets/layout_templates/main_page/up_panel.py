from .main_page_css import *


def up_panel(id_page):
    return my_div(
        style_up_panel,
        "",
        [
            my_div(
                style_div_user,
                "",
                my_div(style_user, f"{id_page}_panel_up_left"),
            ),
            my_div(style_div_app, "", html.H5("Big Data App", style=style_app)),
            my_div(
                style_div_sesion,
                "",
                my_div(style_sesion, f"{id_page}_panel_up_right"),
            ),
        ],
        className="alert-primary",
    )
