from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate
from pandas import read_json


def create_callback_button_save(id_page):
    @callback(
        [         
         Output("main_page_store", "data", allow_duplicate=True),
         Output(f"{id_page}_save", "n_clicks"),
         Output(f"{id_page}_save", "disabled", allow_duplicate=True),
        ],
        Input(f"{id_page}_save", "n_clicks"),
        State("main_page_store", "data"),
        prevent_initial_call=True,)
    def save_button(save, data):
        if save:
            df = read_json(data["prov_df"])
            data["df"] = df.to_json(orient="columns")
            data["pipeline"] = data["prov_cod"]
        else:
            raise PreventUpdate
        return [data, 0, True]
    

def create_callback_updates_button_save(id_page, id_drop):
    @callback(
        [
         Output(f"{id_page}_{id_drop}", "options", allow_duplicate=True),
         Output(f"{id_page}_{id_drop}", "value", allow_duplicate=True),         
        ],
        Input(f"{id_page}_save", "n_clicks"),
        State("main_page_store", "data"),
        prevent_initial_call=True,)
    def save_button(save, data):
        df = read_json(data["prov_df"])
        data["df"] = df.to_json(orient="columns")
        columns = list(df.columns)        
        return [columns, columns[0]]   