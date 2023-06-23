from buttons_conf import l_workflow
from dependencies.classes import button_bar, panel
from pages_conf.main_page.utils import create_div_buttons

id_page = "main_page"

# button bar
workFlow_button = button_bar.BarWithIconCreator(
    "WorkFlow", f"{id_page}_button_show_workflow", "btn-functionalities"
)
# workflow_button
workflow_buttons_div = create_div_buttons(f"{id_page}_div_workflow", l_workflow, False)

workflow = panel.Panel(f"{id_page}_div_workFlow")
workflow.update_panel(workflow_buttons_div, "")
workflow.update_hidden(True)

div_workflow = panel.Panel("")
div_workflow.update_panel(
    [workFlow_button.create_bar_with_icon(), workflow.panel()], "panel-functions"
)

panel_workflow = div_workflow.panel()
