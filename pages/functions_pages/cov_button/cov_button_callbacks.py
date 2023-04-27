import plotly.express as px
from dash import Input, Output, State, callback, dcc, html
from pandas import read_json, set_option

from assets.templates import template_visualizations
from common_functions.create_callback_button_cover import \
    create_callback_button_cover
from my_dash.my_html.my_div import my_div
from pages.functions_pages.cov_button.cov_button_css import *

id_page = "cov"


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
         Input("cov_button", "n_clicks"),
         Input(f"{id_page}_text", "className"),
         Input(f"{id_page}_graph", "className"),
         Input(f"{id_page}_refresh", "n_clicks")
        ],
        [
         State("main_page_store", "data"),
         State(f"{id_page}_text", "className"),
         State(f"{id_page}_graph", "className"),
         
         State(f"{id_page}_ddof", "value"),
         State(f"{id_page}_numeric_only", "value"),
         State(f"{id_page}_min_periods", "value"),
        ],
        prevent_initial_call=True,)
def second_callback(n_clicks, n_clicks_text, n_click_graph, refresh, data,
                    state_text, state_graph, state_ddof, state_numeric_only,
                    state_min_periods):    
    
    try: 
       obj = ""     
       if state_min_periods: 
           state_min_periods = int(state_min_periods)

       if state_numeric_only == "True":
           state_numeric_only = True
       else:
           state_numeric_only = False

       cov = read_json(data["df"]).cov(state_min_periods, state_ddof, state_numeric_only)

       if state_text == "btn btn-warning":
           set_option('display.max_columns', 500)
           set_option('display.width', 1000)
           obj = html.Pre(cov.__str__(), style=style_cov_text)
              
       if state_graph == "btn btn-warning":
          fig = px.imshow(cov, template=template_visualizations,
                          color_continuous_scale="earth", aspect="auto")
          obj = dcc.Graph(figure=fig, config={'displayModeBar': False, 'responsive': True},
                          style={'width': '100%', 'height': '100%'})
          
       return [        
              my_div(style_div_content, "",
                     [
                      my_div(style_div_title, "",
                             [
                              html.H5("DataFrame.cov()",
                                      style=style_title),
                              html.A("Documentacion",
                                     href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html",
                                     target="_blank")
                             ],
                      ),
                      my_div(style_div_obj, "", obj)
                     ],
              ), ""]
    except ValueError as msg:
        return [
                html.H6(msg.__str__(),
                        style=style_msg),
                ""]
