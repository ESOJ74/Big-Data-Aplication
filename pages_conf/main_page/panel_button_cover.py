import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from dependencies.classes import panel

id_page = "main_page"

button_cover = panel.Panel(f"{id_page}_div_button_cover")
button_cover.update_panel(
    dbc.Button(
        id=f"{id_page}_button_cover",
        children=DashIconify(
            icon="ic:baseline-arrow-circle-left", className="icon-cover"
        ),
        class_name="btn-cover",
        style={"border": "transparent"},
    ),
    "panel-button-cover",
)

panel_button_cover = button_cover.panel()
