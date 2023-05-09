from numpy import arange

from assets.layout_templates.main_page.content_layout import create_content_layout
from assets.layout_templates.panel_params.create_panel_params import *

from .scatter_3d_button_callbacks import *

id_page = "scatter_3d"

params_utils = [
    create_select(id_page, "X"),
    create_select(id_page, "Y"),
    create_select(id_page, "Z"),
    html.H4("Params", style=style_title_params),
    create_param_drop(id_page, "color"),
    create_param_drop(id_page, "symbol"),
    create_param_drop(id_page, "size"),
    create_param_drop(id_page, "opacity", options=list(arange(0.1, 1.1, 0.1)), value=1),
    create_buttom_refresh(id_page),
]

content_down = my_div(
    style_div_content_down,
    f"{id_page}_content_down",
    my_div(style_div_result, f"{id_page}_div_graph"),
)

layout = create_content_layout(
    id_page,
    my_div(style_div_content_up, f"{id_page}_content_up"),
    content_down,
    my_div(style_div_params, "", params_utils),
)
