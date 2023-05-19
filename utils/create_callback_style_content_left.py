from dash import Input, Output, callback

from assets.layout_templates.main_page.common_css import (
    style_content_left,
    style_content_left2,
)


def create_callback_style_content_left(id_page):
    @callback(
        Output(f"{id_page}_content_left", "style", allow_duplicate=True),
        Input("main_page_button_cover", "n_clicks"),
        prevent_initial_call=True,
    )
    def auth_display(n_clicks):
        print(n_clicks)
        if n_clicks % 2 != 0:
            return style_content_left2
        return style_content_left
