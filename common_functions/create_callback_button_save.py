from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate
from pandas import read_json


def create_callback_button_save(id_page):
    @callback(
        [
        Output(f"{id_page}_dropdown", "options", allow_duplicate=True),
        Output(f"{id_page}_dropdown", "value", allow_duplicate=True),
        Output("main_page_store", "data", allow_duplicate=True),
        Output(f"{id_page}_save", "n_clicks"),
        ],
        Input(f"{id_page}_save", "n_clicks"),
        State("main_page_store", "data"),
        prevent_initial_call=True,)
    def save_button(save, data):
        if save:
            df = read_json(data["prov_df"])
            data["df"] = df.to_json(orient="columns")
            columns = list(df.columns)
        else:
            raise PreventUpdate
        return [columns, columns[0], data, 0]