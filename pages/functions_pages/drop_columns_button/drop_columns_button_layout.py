from my_dash.my_html.my_div import my_div
from pages.functions_pages.drop_columns_button.drop_columns_button_callbacks import *

id_page = "drop_columns_function"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({},f"{id_page}_div_dropdown"),
                  my_div({"margin-top": "0.5%"}, f"{id_page}_content")
                ])