from dash import dcc, html

from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div
from pages.functions_pages.info_pages.cov_button.cov_button_css import *

id_page = "describe"

def create_param_drop(id_param, options, value):
    return my_div(style_div_color, "", 
                  [
                   html.H6(id_param, style=style_params),
                   my_div(style_selector_color, "",
                          my_dropdown(f"{id_page}_{id_param}",
                                      {"background": "#b0d8d3"},
                                      options=options,
                                      value=value,
                          ),
                   )                                           
                  ]
           )


def create_utils(id_page):
    return my_div(style_div_utils, "",
                 [                   
                   html.H4("Params", style=style_div_params),        
                   my_div({"margin-left": "5%", "height" :"14%"}, "",
                          [
                           html.H6("percentiles", style=style_params),
                           dcc.Input(id=f"{id_page}_percentiles",
                                     style=style_input,
                                     value=None,
                           ),
                          ]
                   ),
                 
                   create_param_drop("include", ["", "all", 'number', "category", "object"], ""), 
                   create_param_drop("exclude", ["", 'number', "category", "object"], ""),                   
                   my_button(f"{id_page}_refresh", "Refresh", style_button_refresh,
                             className="btn btn-outline-warning", color="black"),            
                 ]
          )