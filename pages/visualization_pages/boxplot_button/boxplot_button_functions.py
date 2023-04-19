from my_dash.my_dbc.my_button import my_button
from my_dash.my_dcc.my_dropdown import my_dropdown
from my_dash.my_html.my_div import my_div

id_page = "boxplot_button"

s_utils = {
    "position": "relative",
    "top": "15.5%",
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


def create_utils(id_page):
    return my_div(s_utils, "",
                 [
                   my_div(style_div_input, "", 
                          [
                           my_div({}, "", "points"),
                           my_dropdown(f"{id_page}_points", {"width": "70%", "color": "black", "font-size": "80%"},
                                       options=["all", "outliers", "false"], value="outliers"),   
                           my_div({}, "", "color"),
                           my_dropdown(f"{id_page}_color", {"width": "70%", "color": "black", "font-size": "80%"},),      
                           my_div({}, "", "quartile method"),
                           my_dropdown(f"{id_page}_quartilemethod", {"width": "70%", "color": "black", "font-size": "80%"},
                                       options=["linear", "inclusive", "exclusive"], value="linear"),    
                           my_div({}, "", "notched"),
                           my_dropdown(f"{id_page}_notched", {"width": "70%", "color": "black", "font-size": "80%"},
                                       options=["true", "false"], value="false"),
                           my_div({}, "", "hover_data"),
                           my_dropdown(f"{id_page}_hover_data", {"width": "70%", "color": "black", "font-size": "80%"},),              
                           my_button(f"{id_page}_refresh", "Refresh", {"margin-top": "2%"}, className="btn btn-outline-light", color="black")
                          ]
                   ),                   
                 ]
          )