from dependencies.classes import panel
from pages_conf.main_page.panel_functions import panel_functions
from pages_conf.main_page.panel_models import panel_models
from pages_conf.main_page.panel_visualizations import panel_visualizations
from pages_conf.main_page.panel_workflow import panel_workflow

id_page = "main_page"

functionalities = panel.Panel(f"{id_page}_div_functionalities")
functionalities.update_panel(
    [
        panel_functions,
        panel_visualizations,
        panel_models,
        panel_workflow,
    ],
    "panel-functionalities",
)
functionalities.update_hidden(True)

panel_functionalities = functionalities.panel()
