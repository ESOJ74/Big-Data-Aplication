from dash import callback
from dash.dependencies import Input, Output, State
from pandas import read_json


def refresh_button(id_page):
    @callback(Output(f"{id_page}_drop_left", "value"),           
              Input(f"{id_page}_refresh", "n_clicks"),  
              State(f"{id_page}_drop_left", "value"),
              prevent_initial_call=True)
    def display_page(n_clicks, drop_left_state):
        return drop_left_state
    

def selector_options(id_page, id_selector, value=True):
    @callback(Output(id_selector, 'options'),
              Input(f"{id_page}_content_up", "children"),
              State('main_page_store', 'data'),
              prevent_initial_call=True)
    def display_page(n_clicks, data):   
        if value:       
            return [" "] +  list(read_json(data["df"]).columns)  
        else:
            return list(read_json(data["df"]).columns)
