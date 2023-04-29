from dash import callback
from dash.dependencies import Input, Output, State
from pandas import read_json
from assets.my_dash.my_html.my_div import my_div
from assets.my_dash.my_dcc.my_dropdown import my_dropdown
from assets.common_css import background_dropdown, background_in_dropdown

style_div_selectors = {
    "position": "relative",
    "top": "6%",
    "width": "70%",
    "height": "100%",
    "position": "relative",
    "top": "20%",
}
style_selector = {
    "float": "left",       
    "width": "12vmax",
    "height": "2.5em",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "color": "black",
    "background": background_dropdown,
}

style_selector2 = style_selector.copy()
style_selector2["margin-left"] = "2%"


def create_double_dropdown(id_page, style_selector=style_selector, style_selector2=style_selector2):
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
                                        {"background": background_in_dropdown},
                                        columns,
                                        placeholder="Seleccione columna"),
                    ),
                    my_div(style_selector2, "",
                            my_dropdown(f"{id_page}_drop_right",
                                        {"background": background_in_dropdown},
                                        columns,
                                        placeholder="Seleccione columna"),
                    ),
                    ]         
            )
    
def create_single_dropdown(id_page, id_output, style_selector=style_selector, multi=False):
    @callback(Output(id_output, "children"),
              Input(f"{id_page}_button", "n_clicks"),
              State('main_page_store', 'data'),
              prevent_initial_call=True)
    def display_page(n_clicks, data):
        return my_div(style_selector, "", 
                      my_dropdown(f"{id_page}_dropdown",
                                  {"background": background_in_dropdown},
                                  read_json(data["df"]).columns,
                                  placeholder="Seleccione columna",
                                  multi=multi
                      ),)