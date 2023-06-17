from buttons_conf import functions_info, functions_a_g, functions_h_p, functions_q_z
from dependencies.classes import button_bar, panel
from pages_conf.main_page.utils import create_button_drop, create_div_buttons

id_page = "main_page"


# button bar
functions_button = button_bar.BarWithIconCreator(
    "Functions", f"{id_page}_button_show_functions", "btn-functionalities"
)

# info_button
info_button = create_button_drop(f"{id_page}_button_info", "Info")
info_buttons_div = create_div_buttons(f"{id_page}_div_info", functions_info)
# A-G button
a_g_button = create_button_drop(f"{id_page}_button_a_g", "A-G")
a_g_buttons_div = create_div_buttons(f"{id_page}_div_a_g", functions_a_g)
# H-P button
h_p_button = create_button_drop(f"{id_page}_button_h_p", "H-P")
h_p_buttons_div = create_div_buttons(f"{id_page}_div_h_p", functions_h_p)
# Q-Z button
q_z_button = create_button_drop(f"{id_page}_button_q_z", "Q-Z")
q_z_buttons_div = create_div_buttons(f"{id_page}_div_q_z", functions_q_z)

list_of_functions = [
    info_button,
    info_buttons_div,
    a_g_button,
    a_g_buttons_div,
    h_p_button,
    h_p_buttons_div,
    q_z_button,
    q_z_buttons_div,
]

functions = panel.Panel(f"{id_page}_div_functions")
functions.update_panel(list_of_functions, "")
functions.update_hidden(True)

div_functions = panel.Panel("")
div_functions.update_panel(
    [functions_button.create_bar_with_icon(), functions.panel()], "panel-functions"
)

panel_functions = div_functions.panel()