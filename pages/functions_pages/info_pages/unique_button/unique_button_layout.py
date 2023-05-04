from dash import Input, Output, State, callback, html
from pandas import read_json

from ..common_css import *
from assets.layout_templates.main_page.content_layout import \
    create_content_layout
from assets.my_dash.my_html.my_div import my_div

id_page = "unique"

layout = create_content_layout(id_page,
                               my_div(style_div_content_up, f"{id_page}_content_up"),
                               my_div(style_div_content_down, f"{id_page}_content_down"),
                               my_div(style_div_params, ""))


@callback(Output(f"{id_page}_content_up", "children"), 
          Input("unique_button", "n_clicks"), 
          prevent_initial_call=True,)
def second_callback(n_clicks):    
    return my_div(style_div_title, "",
                  [
                   html.H5("DataFrame.unique()",
                           style=style_title),
                   html.A("Documentacion",
                          href="https://pandas.pydata.org/docs/reference/api/pandas.unique.html",
                          target="_blank")
                  ])


@callback(
        [
         Output(f"{id_page}_content_down", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True),
        ],
        Input("unique_button", "n_clicks"),
        State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):   
    try:
        df = read_json(data["df"])
    except KeyError:
        return [html.H6("No ha cargado ningún fichero", style=style_msg), ""]  
    return [        
            my_div(style_div_content, "",
                    my_div(style_div_obj , "",
                           html.Pre(df.apply(lambda x: len(x.unique())).__str__(),
                             style=style_text),)
            ), ""]
    