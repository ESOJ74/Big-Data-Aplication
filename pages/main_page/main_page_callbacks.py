import os

from dash import callback
from dash.dependencies import Input, Output

from pages.main_page.main_page_functions import create_callback
from pages.main_page.main_page_lists import (buttons, functions, models,
                                             visualizations)

id_page = "main_page"

@callback(Output(f"{id_page}_store", "data"),
          Input(f"{id_page}_user", "value"))
def a(user_value):
    if user_value:
        if os.path.exists(f"users/{user_value}")==False:
            os.mkdir(f"users/{user_value}")
    return {"user": user_value}


create_callback(buttons, "i_o_pages")
create_callback(visualizations, "visualization_pages", "Visualización")
create_callback(functions, "functions_pages", "Función")
create_callback(models, "models_pages", "Modelo")