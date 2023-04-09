from my_dash.my_html.my_div import my_div

style_main_div = {"width": "100%", "height": "100%"}
style_div_content = {"float": "left", "width": "85%", "height": "100%"}
style_div_content_up = {"width": "100%", "height": "10%"}
style_div_content_middle = {"width": "100%", "height": "50%"}
style_div_content_down = {"width": "100%", "height": "40%"}
style_div_utils = {"float": "left", "width": "15%", "height": "100%", "background": "#699B8F"}

def create_visualization_layout(id_page):
    return my_div(style_main_div, "",
                  [
                   my_div(style_div_content, "",
                          [
                           my_div(style_div_content_up, f"{id_page}_content_up"),
                           my_div(style_div_content_middle, f"{id_page}_content_middle"),
                           my_div(style_div_content_down, f"{id_page}_content_down"),
                          ]
                   ),
                   my_div(style_div_utils, f"{id_page}_utils")
                  ])