from my_dash.my_html.my_div import my_div
from my_dash.my_dbc.my_button import my_button
from dash import dcc
from my_dash.my_dcc.my_dropdown import my_dropdown

id_page = "histogram_button"

s_utils = {
    "position": "relative",
    "top": "10%",
    "width": "100%",
    "height": "50%",
    "background": "#95D3DE",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

style_div_input = {
    "margin-left": "2%",
    "font-weight": "bold",
    "color": "#012A32"
}

style_input = {    
    "width": "10%"
}


def create_utils(id_page):
    return my_div(s_utils, "",
                 [
                   my_div(style_div_input, "", 
                          [my_div({}, "", "nbins"),
                           dcc.Input(id=f"{id_page}_nbins",
                                          style={"width": "15%", "background": "white", "color": "black"},
                                          value=20,
                           ),
                           my_div({}, "", "color"),
                           my_dropdown(f"{id_page}_color", {"width": "70%", "color": "black", "font-size": "80%"},),                           
                           my_button(f"{id_page}_refresh", "Refresh", {"margin-top": "2%"}, className="btn btn-outline-light", color="black")
                          ]
                   ),                   
                 ]
          )