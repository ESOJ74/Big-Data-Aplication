from dependencies.classes import panel

from pages_conf.main_page.panel_data import panel_data
from pages_conf.main_page.panel_functionalities import panel_functionalities

id_page = "main_page"

panel_middle_left = panel.Panel(f"{id_page}_panel_middle_left")
panel_middle_left.update_panel([panel_data, panel_functionalities], "panel-middle-left")


panel_middle_right = panel.Panel(f"{id_page}_panel_middle_right")
panel_middle_right.update_panel([], "panel-middle-right")


middle = panel.Panel()
middle.update_panel(
    [panel_middle_left.panel(), panel_middle_right.panel()],
    "panel-middle",
)

middle_panel = middle.panel()
