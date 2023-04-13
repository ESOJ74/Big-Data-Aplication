from dash import dcc

from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div

style_div_regystry = {
    "position": "absolute",
    "top": "5%",
    "left": "1%",
    "width": "10%",
    "height": "10%"
}

style_div_input = {    
    "margin-top": "1%",
    "margin-left": "5%",
    "width": "85%"
}

style_input = {
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "width": "100%"
}

style_button = {    
    "margin-top": "2%",
    "margin-left": "5%",
    "width": "85%",
    "height": "30%",
    "font-size": "90%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

style_div_reg_answer = {    
    "margin-top": "1%",
    "margin-left": "5%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

style_accept = {
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "width": "100%"
}

def user_registry(id_page):
    return my_div(style_div_regystry, f"{id_page}_div_registry",
                 [
                  my_div(style_div_input, "",
                                dcc.Input(id=f"{id_page}_reg_user",
                                          placeholder="Usuario",
                                          style=style_input,
                                          debounce=True
                                )
                  ),
                  my_div(style_div_input, "",
                                dcc.Input(id=f"{id_page}_reg_pass",
                                          placeholder="Contraseña",
                                          style=style_input,
                                          debounce=True
                                )
                  ),
                  my_button(f"{id_page}_reg_accept", "Aceptar", style_button),
                  my_div(style_div_reg_answer, f"{id_page}_reg_answer"),        
                 ]
    )