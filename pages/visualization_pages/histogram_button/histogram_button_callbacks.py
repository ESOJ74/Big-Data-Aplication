import plotly.express as px
from dash import callback, dcc
from dash.dependencies import Input, Output, State
from pandas import read_json

from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.visualization_pages.histogram_button.histogram_button_css import *
from pages.visualization_pages.histogram_button.histogram_button_functions import \
    create_utils

id_page = "histogram_button"


# Panel utils
@callback(Output(f"{id_page}_utils", "children"),          
          Input("histogram_button", "n_clicks"),
          prevent_initial_call=True)
def display_page(n_clicks):  
    return create_utils(id_page)


# Panel content_up (dropdown)
@callback(Output(f"{id_page}_content_up", "children"),
          Input("histogram_button", "n_clicks"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):     
    return my_div(s_selector, "",
                  my_dropdown(f"{id_page}_dropdown",
                              {},
                              read_json(data["df"]).columns,
                              placeholder="Seleccione columna"),)
    

# color options 
@callback(Output(f"{id_page}_color", 'options'),
          Input(f"{id_page}_content_up", "children"),
          State('main_page_store', 'data'),
          prevent_initial_call=True)
def display_page(n_clicks, data):      
    return [" "] +  list(read_json(data["df"]).columns)  


# Panel content_middle
@callback(Output(f"{id_page}_content_middle", "children"),           
          Input(f"{id_page}_dropdown", "value"),  
          [
           State('main_page_store', 'data'),
           State(f"{id_page}_nbins", 'value'),
           State(f"{id_page}_color", 'value'),
          ],
          prevent_initial_call=True)
def display_page(
    dropdown_value,
    data,
    nbins_state,
    color_state):     

    if color_state is not None and len(color_state) < 1 or color_state == " ":
        color_state = None     
     
    obj = ["", ""]
    if dropdown_value:
        # content_middle
        df = read_json(data["df"])
        fig = px.histogram(
            df,
            x=dropdown_value,
            color=color_state,
            nbins=int(nbins_state))
        obj = [dcc.Graph(figure=fig)]               
    return obj


# refresh button
@callback(Output(f"{id_page}_dropdown", "value"),           
          Input(f"{id_page}_refresh", "n_clicks"),  
          State(f"{id_page}_dropdown", "value"),
          prevent_initial_call=True)
def display_page(n_clicks, dropdown_state):
    return dropdown_state
