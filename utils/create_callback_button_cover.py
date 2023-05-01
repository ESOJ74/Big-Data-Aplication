from dash import Input, Output, callback


def create_callback_button_cover(id_page, input = ""):

    id_input = f"{id_page}_content"
    if len(input) > 0:
        id_input = input
    @callback(Output("main_page_div_button_cover", "hidden",
                     allow_duplicate=True),
              Input(id_input, "children"),
              prevent_initial_call=True)
    def display_page(values):
        return False
