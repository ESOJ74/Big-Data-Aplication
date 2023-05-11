from assets.layout_templates.main_page.content_layout import create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .view_data_button_callbacks import *

id_page = "view_data"
style_div_result = {
    "position": "relative",
    "top": "2%",
    "width": "100%",
    "height": "88%"
}
content_down = my_div(
    style_div_content_down,
    f"{id_page}_content_down",
    my_div(style_div_result, f"{id_page}_div_graph"),
)
#content_down = my_div(style_div_content_down, f"{id_page}_content_down")

layout = create_content_layout(
    id_page,
    my_div(style_div_content_up, f"{id_page}_content_up"),
    content_down,
    my_div(style_div_params, "", ""),
)
