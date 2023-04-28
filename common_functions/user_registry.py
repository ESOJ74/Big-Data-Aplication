from dash import dcc, html

from assets.common_css import background_dark, background_light
from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div

style_div_regystry = {
    "position": "absolute",
    "top": "25%",
    "left": "35%",
    "width": "30%",
    "height": "10%",
}

style_div_regystry2 = {
    
    "margin-top": "13%",
    "margin-left": "35%",
    "width": "30%",
    "height": "10%",
}

style_div_input = {    
    "margin-top": "6%",
    "margin-left": "5%",
    "width": "40%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

style_button = {    
    "margin-top": "1%",
    "margin-left": "12%",
    "width": "6em",
    "height": "35%",
    "font-size": "0.8vmax",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "color": "#b0d8d3",
    "border": "1.5px solid"
}

style_div_reg_answer = {  
    "margin-top": "2%",
    "margin-left": "5%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",    
}

style_accept = {
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
    "width": "100%"
}

style_div_register = {
    "margin-left": "5%",
    "margin-top": "3%",
    "width": "100%"
}

style_div_answer = {
    "float": "left",
    "width": "35%",
    "font-size":"0.9vmax",
    "color": "#b0d8d3",
}

style_div_login = {
    "float": "left",
    "width": "60%",
    "font-size": "0.9vmax"
}

style_input = {
    "width": "10em",
    "font-size": "1vmax",
    "background": background_light,
    "border": "1px solid #020d11",
    "color": "black"
}

def insert_user(id_page):
    return my_div(style_div_input, "",
                         [
                          my_div({"width": "10em"}, "",
                                 dcc.Input(id=f"{id_page}_reg_user",
                                           placeholder="Usuario",
                                           style=style_input,
                                 )
                          ),
                          my_div({"width": "10em"}, "",
                                 dcc.Input(id=f"{id_page}_reg_pass",
                                           placeholder="Contraseña",
                                           style=style_input,
                                 )
                          ),
                         ]
                  )


def user_login(id_page):
    return my_div(style_div_regystry, f"{id_page}_div_registry",
                 [
                  my_div({"margin-left": "4%"}, "", html.H2('Login'),),                  
                  insert_user(id_page),
                  my_button(f"{id_page}_reg_accept", "Login", style_button),
                  my_div(style_div_reg_answer, f"{id_page}_reg_answer"),      
                  my_div(style_div_register, "", 
                         [
                          my_div(style_div_answer, "",
                                 html.Label('Nuevo en Big Data App?'),),
                          my_div(style_div_login, "",
                                 html.A('Register', href='/registro'),),
                         ]
                  ),                    
                 ]
           )


def user_registry(id_page):
    return my_div({"position": "absolute", "top": "0%", "left": "0%", "width": "100%", "height": "100%",
                   "background": background_dark}, "",
                   my_div(style_div_regystry2, f"{id_page}_div_registry",
                          [
                           my_div({"margin-left": "4%"}, "", html.H2('Sign In'),),                  
                           insert_user(id_page),
                           my_button(f"{id_page}_reg_accept", "Sing in", style_button),                  
                           my_div(style_div_reg_answer, f"{id_page}_reg_answer"),   
                           my_div(style_div_register, "", 
                                  [
                                   my_div(style_div_answer, "",
                                          html.Label('Ir a Big Data App?'),),
                                   my_div(style_div_login, "",
                                          html.A('Login', href='/'),),
                                  ]
                           ),         
                          ]
                    )
        )
