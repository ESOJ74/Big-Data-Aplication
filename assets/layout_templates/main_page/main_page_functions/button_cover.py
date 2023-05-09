from ..main_page_css import *


def button_cover(id_page):
    return my_div(
        style_div_button_cover_right,
        f"{id_page}_div_button_cover",
        my_button(
            f"{id_page}_button_cover",
            DashIconify(icon="ic:baseline-arrow-circle-left", width=30),
            style_button_cover_right,
            className="btn btn-primary btn-sm",
        ),
        hidden=True,
    )
