from dash import callback
from dash.dependencies import Input, Output, State
from pandas import read_json
from my_dash.my_html.my_div import my_div
from my_dash.my_dcc.my_dropdown import my_dropdown
from common_functions.common_functions_css import (style_div_selectors,
                                                   style_selector,
                                                   style_selector2)


def create_double_dropdown(id_page):
    # Panel content_up (dropdown)
    @callback(Output(f"{id_page}_content_up", "children"),
              Input(id_page, "n_clicks"),
              State('main_page_store', 'data'),
              prevent_initial_call=True)
    def display_page(n_clicks, data):   
        columns = read_json(data["df"]).columns  
        return my_div(style_div_selectors, "",
                    [
                    my_div(style_selector, "",
                            my_dropdown(f"{id_page}_drop_left",
                                        {},
                                        columns,
                                        placeholder="Seleccione columna"),
                    ),
                    my_div(style_selector2, "",
                            my_dropdown(f"{id_page}_drop_right",
                                        {"background": "#acf4ed"},
                                        columns,
                                        placeholder="Seleccione columna"),
                    ),
                    ]         
            )
    
def create_single_dropdown(id_page, id_output, style_selector, multi=False):
    @callback(Output(id_output, "children"),
              Input(f"{id_page}_button", "n_clicks"),
              State('main_page_store', 'data'),
              prevent_initial_call=True)
    def display_page(n_clicks, data):
        return my_div(style_selector, "", 
                      my_dropdown(f"{id_page}_dropdown",
                                  {"background": "#acf4ed"},
                                  read_json(data["df"]).columns,
                                  placeholder="Seleccione columna",
                                  multi=multi
                      ),)