from dash import Input, Output, State, callback, html
from pandas import read_json

from common_functions.create_functions_layout import create_functions_layout
from my_dash.my_html.my_div import my_div

style_div_content = {
    "position": "relative",
    "top": "1%",
    "left": "30%",
    "width": "25%",
    "font-size": "1.2em",
    "font-weight": "bold",
    "background": "#C5F4FD",
    "color": "#03353E",    
}

id_page = "kurt"

layout = create_functions_layout(id_page, style_div_content)


@callback(
        [
         Output(f"{id_page}_content", "children"),
         Output(f"{id_page}_loading", "children", allow_duplicate=True),
        ],
        Input("kurt_button", "n_clicks"),
        State("main_page_store", "data"),
    prevent_initial_call=True,)
def add_data_to_fig(n_clicks, data):     
    try:
       return [
              my_div({"text-align": "center"}, "",
                     [
                     my_div({"background": "radial-gradient(circle farthest-side at bottom left, #347eb7 0%, #204765 30%, #04212c 95%)"}, "",
                            [
                                   html.H5("DataFrame.kurt()",
                                          style={"font-weight": "bold", "color": "#acf4ed"}),
                                   html.A("Documentacion",  href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html",
                                          target="_blank")
                            ],
                     ),
                     my_div({}, "",
                            html.Pre(read_json(data["df"]).kurt().__str__())
                     ),
                     ],
              ), ""]
    except TypeError as msg:
        return [
                html.H6(msg.__str__(),
                        style={"background": "#060606", "color": "#acf4ed"}),
                ""]