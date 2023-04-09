from my_dash.my_html.my_div import my_div
from pages.functions_pages.groupby_button.groupby_button_callbacks import *

id_page = "groupby_function"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({},"dd"),
                  my_div({"margin-top": "0.5%"}, f"{id_page}_content")
                ])