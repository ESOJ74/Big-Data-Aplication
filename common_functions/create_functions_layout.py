
from dash import dcc
from my_dash.my_html.my_div import my_div

def create_functions_layout(id_page, style_div_content):
    return [
          dcc.Loading(
              id="loading-2",
              children=[my_div({"margin-top": "10%"}, f"{id_page}_loading")],
              type="default",
              fullscreen=False,
          ),
          my_div(style_div_content, f"{id_page}_content")
         ]