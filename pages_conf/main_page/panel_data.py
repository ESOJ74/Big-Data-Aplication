import dash_bootstrap_components as dbc
from dash import html

from dependencies.classes import div_button_creator, panel, button_drop

# from utils.buttons.button_drop import button_drop

id_page = "main_page"

# title
title_panel = panel.Panel()
title_panel.update_panel(html.P("DataFrame"), "panel-title-data")

# button data
button_data = button_drop.ButtonDropCreator(
    "Data", f"{id_page}_button_data", "btn-data"
)
data_panel = panel.Panel()
data_panel.update_panel(button_data.panel(), "panel-button-data")

# button view
view_panel = panel.Panel()
view_panel.update_panel(
    dbc.Button("View", "view_data", className="btn-data", n_clicks=0),
    "panel-button-data",
)

# panel buttons data-view
panel_data_view = panel.Panel()
panel_data_view.update_panel(
    [data_panel.panel(), view_panel.panel()], "panel_data_view"
)

# panel load-save
panel_load_save = div_button_creator.DivButtonCreator(
    "panel_load_save",
    [("load_data", "Load"), ("save_data", "Save")],
)
panel_load_save.update_div_button_classname("panel-load")
panel_load_save.update_button_classname("btn-load")
panel_load_save.update_id_div(f"{id_page}_panel_load_save")

# panel dataFrame
data = panel.Panel()
data.update_panel(
    [title_panel.panel(), panel_data_view.panel(), panel_load_save.panel()],
    "panel-dataframe",
)

panel_data = data.panel()
