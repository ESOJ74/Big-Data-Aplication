from my_dash.my_html.my_div import my_div
from pages.functions_pages.groupby_button.groupby_button_callbacks import *

id_page = "groupby"

layout = my_div({"height": "100%"}, "", 
                [
                  my_div({},f"{id_page}_div_dropdown"),
                  my_div(style_div_content, f"{id_page}_content")
                ])