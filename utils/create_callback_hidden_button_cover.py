from dash import Input, Output, callback


def create_callback_hidden_button_cover(input, state_hidden=False):
    @callback(
        Output("main_page_div_button_cover", "hidden", allow_duplicate=True),
        Input(input, "children"),
        prevent_initial_call=True,
    )
    def display_page(values):
        return state_hidden
