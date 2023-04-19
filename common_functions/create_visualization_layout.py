from dash import dcc, html

from my_dash.my_html.my_div import my_div

style_main_div = {"width": "99%", "height": "100%"}
style_div_content = {"float": "left", "margin-left": "4%", "width": "80%", "height": "97%"}
style_div_content_up = {"width": "95%", "height": "10%"}
style_div_content_middle = {"width": "100%", "height": "50%"}
style_div_content_down = {"width": "99.5%", "margin-top": "2%", "height": "38%", "color": "black"}
style_div_utils = {"float": "left", "margin-left": "1%", "width": "15%", "height": "100%"}


def create_visualization_layout(id_page):
    return my_div(style_main_div, "",
                  [
                   my_div({"margin-top": "2%", "margin-left": "4%"}, "",
                         html.H5(f"DataFrame {id_page.split('_')[0]}"),),
                   my_div(style_div_content, "",
                          [
                           my_div(style_div_content_up, f"{id_page}_content_up"),
                           dcc.Loading(
                               id="loading-2",
                               children=[my_div({}, f"{id_page}_visualizations_loading")],
                               type="default",
                               fullscreen=False,
                           ),
                           my_div(style_div_content_middle, f"{id_page}_content_middle"),
                           my_div(style_div_content_down, f"{id_page}_content_down"),
                          ]
                   ),
                   my_div(style_div_utils, f"{id_page}_utils")
                  ])