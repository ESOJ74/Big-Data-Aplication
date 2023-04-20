import plotly.express as px
from dash import callback, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json

from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.visualization_pages.scatter_button.scatter_button_css import *
from pages.visualization_pages.scatter_button.scatter_button_functions import \
    create_utils

id_page = "scatter_button"


# Panel utils
@callback(Output(f"{id_page}_utils", "children"),          
          Input("scatter_button", "n_clicks"),
          prevent_initial_call=True)
def display_page(n_clicks):  
    return create_utils(id_page)


# Panel content_up (dropdown)
@callback(Output(f"{id_page}_content_up", "children"),
          Input("scatter_button", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):   
    columns = read_json(data["df"]).columns  
    return my_div({"width": "35%", "height": "50%", "position": "relative", "top": "20%"}, "",
                  [
                   my_div(s_selector, "",
                          my_dropdown(f"{id_page}_drop_left",
                                      {},
                                      columns,
                                      placeholder="Seleccione columna"),
                   ),
                   my_div(s_selector, "",
                          my_dropdown(f"{id_page}_drop_right",
                                      {},
                                      columns,
                                      placeholder="Seleccione columna"),
                   ),
                  ]         
           )


# Panel content_middle
@callback([
           Output(f"{id_page}_content_middle", "children"),
           Output(f"{id_page}_visualizations_loading", "children", allow_duplicate=True),
          ],
          [
           Input(f"{id_page}_drop_left", "value"),         
           Input(f"{id_page}_drop_right", "value"),
          ],
          [
           State('main_page_store', 'data'),
           State(f"{id_page}_drop_left", "value"),
           State(f"{id_page}_drop_right", "value"),
           State(f"{id_page}_color", 'value'),
          ],
          prevent_initial_call=True)
def display_page(
    drop_left_value,
    drop_left_right,
    data,
    drop_left_state,
    drop_right_state,
    color_state
    ):     

    if color_state is not None and len(color_state) < 1 or color_state == " ":
        color_state = None    
     
    obj = ["", ""]
    if drop_left_state and drop_right_state:
        # content_middle
        df = read_json(data["df"])
        fig = px.scatter(
            df,
            template='plotly_dark',
            x=drop_left_state,
            y=drop_right_state,
            color=color_state,
        )
        obj = [dcc.Graph(figure=fig)]               
    return [obj, ""]
                  

# color options 
@callback(Output(f"{id_page}_color", 'options'),
          Input(f"{id_page}_content_up", "children"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):          
    return [" "] +  list(read_json(data["df"]).columns)  


# refresh button
@callback(Output(f"{id_page}_drop_left", "value"),           
          Input(f"{id_page}_refresh", "n_clicks"),  
          State(f"{id_page}_drop_left", "value"),
          prevent_initial_call=True)
def display_page(n_clicks, drop_left_state):
    return drop_left_state