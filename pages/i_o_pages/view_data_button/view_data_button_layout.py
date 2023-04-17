from my_dash.my_dbc.my_button import my_button
from my_dash.my_html.my_div import my_div
from pages.i_o_pages.view_data_button.view_data_button_callbacks import *

layout = my_div({"position": "relative", "margin-top": "8%", "margin-left": "7%", "height": "60%"}, "", 
                [
                  my_button("add-data-rows", 
                            "View full DataFrame",
                             {"font-size": "85%",
                              "font-family": "Roboto, Helvetica, Arial, sans-serif",}, 
                             color="black",
                             disabled=True),
                  my_div({"margin-top": "1%", "width": "90%"}, "view_data_content")
                ])
