import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from numpy import float64
from pandas import read_json

from assets.templates import template_visualizations
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from common_functions.panel_params.create_callbacks_text_graph import \
    create_callback_text_graph
from my_dash.my_html.my_div import my_div
from pages.functions_pages.info_pages.common_css import *

id_page = "sem"


create_callback_button_cover(id_page)
create_callback_text_graph(id_page)


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True), 
        ],
        [
         Input("sem_button", "n_clicks"),
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
         State(f"{id_page}_ddof", "value"),
         State(f"{id_page}_numeric_only", "value"),
        ],
        prevent_initial_call=True,)
def second_callback(n_clicks, n_clicks_text, n_click_graph, refresh, data,
                    state_text, state_graph, state_axis, state_skipna,
                    state_ddof, state_numeric_only):    
    
    try: 
       obj = ""   
       state_ddof = int(state_ddof)

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

       sem = read_json(data["df"]).sem(state_axis,
                                       state_skipna,
                                       state_ddof,
                                       state_numeric_only)
       
       sem_info = sem
       if type(sem_info) != float64:
           sem_info = sem_info.to_string()      
       
       obj = html.Pre(sem_info, style=style_text)  
            
       if state_graph == "btn btn-warning":
          if state_axis == 0:
              fig = px.bar(x=sem.index, y=sem.values, labels={"x": "Columns", "y": "unbiased standard error of the mean"},
                           template=template_visualizations)
              obj = dcc.Graph(figure=fig, config={"displayModeBar": False, "responsive": True},
                              style=style_graph)
          else:
              obj = html.Pre("Gráfico disponible solo para axis=0", style=style_text)           
          
       return [        
              my_div(style_div_content, "",
                     [
                      my_div(style_div_title, "",
                             [
                              html.H5("DataFrame.sem()",
                                      style=style_title),
                              html.A("Documentacion",
                                     href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html",
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
