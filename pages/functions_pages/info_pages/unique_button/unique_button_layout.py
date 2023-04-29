from dash import Input, Output, State, callback, html
from pandas import read_json

from assets.common_css import background_dark, background_light
from common_functions.create_layout.create_functions_layout import \
    create_functions_layout
from assets.my_dash.my_html.my_div import my_div

id_page = "unique"

layout = create_functions_layout(id_page)

style_div_content ={    
    "text-align": "center",
    "height": "100%",
}

style_div_title = {
    "background": background_dark
}

style_title = {
      "font-weight": "bold",
      "color": "#acf4ed"
}

style_div_text = {
    "height": "90%",
    "overflow": "auto",
    "background": background_light
}

@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True),
        ],
        Input("unique_button", "n_clicks"),
        State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):     
    return [        
            my_div(style_div_content, "",
                   [
                    my_div(style_div_title , "",
                           [
                            html.H5("DataFrame.unique()",
                                    style=style_title),
                            html.A("Documentacion",
                                   href="https://pandas.pydata.org/docs/reference/api/pandas.unique.html",
                                   target="_blank")
                           ],
                    ),
                    html.Pre(read_json(data["df"]).apply(lambda x: len(x.unique())).__str__(),
                             style=style_div_text),                     
                   ],
           ), ""]
    