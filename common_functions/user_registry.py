from dash import dcc, html

from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div

style_div_regystry = {
    "position": "absolute",
    "top": "25%",
    "left": "35%",
    "width": "30%",
    "height": "10%"
}

style_div_input = {    
    "margin-top": "6%",
    "margin-left": "5%",
    "width": "40%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
}

style_input = {
    
     
}

style_button = {    
    "margin-top": "1%",
    "margin-left": "12%",
    "width": "22%",
    "height": "35%",
    "font-size": "90%",
    "font-family": "Roboto, Helvetica, Arial, sans-serif",
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

style_div_register = {"margin-left": "5%",
                      "margin-top": "3%",
                      "width": "100%"
}


def insert_user(id_page):
    return my_div(style_div_input, "",
                         [
                          my_div({}, "",
                                 dcc.Input(id=f"{id_page}_reg_user",
                                           placeholder="Usuario",
                                 )
                          ),
                          my_div({}, "",
                                 dcc.Input(id=f"{id_page}_reg_pass",
                                           placeholder="Contraseña",
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
                          my_div({"float": "left", "width": "31%"}, "",
                                 html.Label('Nuevo en Big Data App?'),),
                          my_div({"float": "left", "width": "65%"}, "",
                                 html.A('Register', href='/registro'),),
                         ]
                  ),                    
                 ]
           )


def user_registry(id_page):
    return my_div(style_div_regystry, f"{id_page}_div_registry",
                 [
                  my_div({"margin-left": "4%"}, "", html.H2('Sign In'),),                  
                  insert_user(id_page),
                  my_button(f"{id_page}_reg_accept", "Sing in", style_button),                  
                  my_div(style_div_reg_answer, f"{id_page}_reg_answer"),   
                  my_div(style_div_register, "", 
                         [
                          my_div({"float": "left", "width": "23%"}, "",
                                 html.Label('Ir a Big Data App?'),),
                          my_div({"float": "left", "width": "70%"}, "",
                                 html.A('Login', href='/'),),
                         ]
                  ),         
                 ]
           )
