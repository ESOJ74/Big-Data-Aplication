from dash import Input, Output, State, callback
from pandas import read_json


def selector_options(id_page, id_selector, value=True):
    @callback(
        Output(id_selector, "options"),
        Input("initial_layout_url", "pathname"),
        State("main_page_store", "data"),
    )
    def display_page(n_clicks, data):
        if value:
            return [" "] + list(read_json(data["df"]).columns)
        else:
            return list(read_json(data["df"]).columns)
