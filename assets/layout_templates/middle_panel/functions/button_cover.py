from assets.layout_templates.imports import *

style_div_button_cover_right ={
    "position": "absolute",
    "left": "15.5%",
    "top": "5.4%",
}

style_button_cover_right = {
    "background": "#04212c",
    "border": "0px solid #2a9fd6",
    "border-radius": "80px",
    "color": color_boton_1,    
}

style_div_button_cover_left ={
    "position": "absolute",
    "left": "0.1%",
    "top": "5.4%",
}

style_button_cover_left = {
    "background": "#204765",
    "border": "0px solid #060606",
    "border-radius": "80px",
    "color": color_boton_1,
}

def button_cover(id_page):
    return my_div(style_div_button_cover_right,
                  f"{id_page}_div_button_cover",
                  my_button(f"{id_page}_button_cover",
                            DashIconify(
                                icon="ic:baseline-arrow-circle-left",
                                width=30
                            ),
                            style_button_cover_right,
                            className="btn btn-primary btn-sm",
                  ),
                  hidden=True)