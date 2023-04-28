from my_dash.my_html.my_div import my_div
from pages.dataframe_pages.view_data_button.view_data_button_callbacks import *

layout = my_div({"position": "relative", "margin-top": "8%", "margin-left": "2%", "height": "60%"}, "", 
                [
                 my_div({"width": "50%"}, "add-data-rows"),
                 my_div({"margin-top": "1%", "width": "97%"}, "view_data_content")]
                )
