from dash import dcc, html

from my_dash.my_html.my_div import my_div

style_main_div = {"width": "99%", "height": "100%"}
style_div_content = {"float": "left", "margin-left": "4%", "margin-top": "3%", "width": "80%", "height": "90%"}
style_div_content_up = {"margin-top": "1%", "width": "95%", "height": "10%"}
style_div_content_middle = {"width": "100%", "height": "52%", "margin-top": "2%"}
style_div_content_down = {"width": "99.5%", "margin-top": "4%", "height": "38%"}
style_div_utils = {"float": "left", "margin-left": "1%", "width": "15%", "height": "100%"}

 
def create_models_layout(id_page, create_utils):
    return my_div(style_main_div, "",
                  [
                   my_div({"margin-top": "2%", "margin-left": "4%"}, "",
                         html.H5(f"{' '.join(id_page.split('_'))}"),),
                   my_div(style_div_content, "",
                          [
                           my_div(style_div_content_up, f"{id_page}_content_up"),
                           dcc.Loading(
                               id="loading-2",
                               children=[my_div({}, f"{id_page}_model_loading")],
                               type="default",
                               fullscreen=False,
                           ),
                           my_div(style_div_content_middle, f"{id_page}_content_middle"),
                           my_div(style_div_content_down, f"{id_page}_content_down"),
                          ]
                   ),
                   my_div(style_div_utils, f"{id_page}_utils", create_utils)
                  ])