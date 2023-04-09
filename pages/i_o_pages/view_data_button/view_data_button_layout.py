from my_dash.my_html.my_button import my_button
from my_dash.my_html.my_div import my_div
from pages.i_o_pages.view_data_button.view_data_button_callbacks import *

layout = my_div({"margin-top": "2%", "margin-left": "2%", "height": "100%"}, "", 
                [
                  my_button("add-data-rows", 
                            "View full DataFrame",
                             {}, 
                             disabled=True),
                  my_div({"width": "90%"}, "view_data_content")
                ])
