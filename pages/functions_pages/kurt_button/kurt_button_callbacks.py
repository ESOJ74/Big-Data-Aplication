import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from numpy import float64
from pandas import read_json

from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_html.my_div import my_div
from pages.functions_pages.kurt_button.kurt_button_css import *

id_page = "kurt"


create_callback_button_cover(id_page)


@callback(
        [
         Output(f"{id_page}_text", "className"),
         Output(f"{id_page}_graph", "className"),                 
         Output(f"{id_page}_text", "n_clicks"),
         Output(f"{id_page}_graph", "n_clicks")
        ],
        [
         Input(f"{id_page}_text", "n_clicks"),
         Input(f"{id_page}_graph", "n_clicks"),
        ],
        prevent_initial_call=True,)
def first_callback(n_clicks_text, n_click_graph):
    button_text = "btn btn-warning"
    button_graph = "btn btn-outline-warning"
    if n_click_graph:
        button_text = "btn btn-outline-warning"
        button_graph = "btn btn-warning"
    return [button_text, button_graph, 0, 0]


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True), 
        ],
        [
         Input("kurt_button", "n_clicks"),
         Input(f"{id_page}_text", "className"),
         Input(f"{id_page}_graph", "className"),
         Input(f"{id_page}_refresh", "n_clicks")
        ],
        [
         State("main_page_store", "data"),
         State(f"{id_page}_text", "className"),
         State(f"{id_page}_graph", "className"),
         
         State(f"{id_page}_axis", "value"),
         State(f"{id_page}_skipna", "value"),
         State(f"{id_page}_numeric_only", "value"),
        ],
        prevent_initial_call=True,)
def second_callback(n_clicks, n_clicks_text, n_click_graph, refresh, data,
                    state_text, state_graph, state_axis, state_skipna,
                    state_numeric_only):    
    
    try: 
       obj = ""   

       if type(state_axis) != int:
           state_axis = None

       if state_skipna == "True":
           state_skipna = True
       else:
           state_skipna = False

       if state_numeric_only == "True":
           state_numeric_only = True
       else:
           state_numeric_only = False

       kurt = read_json(data["df"]).kurt(state_axis, state_skipna, state_numeric_only)
       
       kurt_info = kurt
       if type(kurt_info) != float64:
           kurt_info = kurt_info.to_string()

       #if state_text == "btn btn-warning":          
           
       if state_axis not in (1, 0):
           kurt_info = f"Agregación en ambos ejes: {kurt_info}"
       obj = html.Pre(kurt_info, style=style_kurt_text)  
            
       if state_graph == "btn btn-warning":
          if state_axis == 0:
              fig = px.bar(x=kurt.index, y=kurt.values, labels={"x": "Columns", "y": "unbiased kurtosis"})
              obj = dcc.Graph(figure=fig, config={"displayModeBar": False, "responsive": True},
                              style={"width": "100%", "height": "100%"})
          else:
              obj = html.Pre("Gráfico disponible solo para axis=0", style=style_kurt_text) 
          
          
       return [        
              my_div(style_div_content, "",
                     [
                      my_div(style_div_title, "",
                             [
                              html.H5("DataFrame.kurt()",
                                      style=style_title),
                              html.A("Documentacion",
                                     href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html",
                                     target="_blank")
                             ],
                      ),
                      my_div(style_div_obj, "", obj)
                     ],
              ), ""]
    except (ValueError, TypeError) as msg:
        return [
                html.H6(msg.__str__(),
                        style=style_msg),
                ""]
