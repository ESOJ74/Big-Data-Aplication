from buttons_conf import (
    visualizations_basic,
    visualizations_part_of_whole,
    visualizations_1d_distribution,
    visualizations_2d_distribution,
    visualizations_three_dimensional,
)
from dependencies.classes import button_bar, panel
from pages_conf.main_page.utils import create_button_drop, create_div_buttons

id_page = "main_page"

# button bar
visualizations_button = button_bar.BarWithIconCreator(
    "Visualizations", f"{id_page}_button_show_visualizations", "btn-functionalities"
)

# basics_button
basic_button = create_button_drop(f"{id_page}_button_basic", "Basics")
basic_buttons_div = create_div_buttons(f"{id_page}_div_basic", visualizations_basic)
# part_of_whole button
part_of_whole_button = create_button_drop(
    f"{id_page}_button_part_of_whole", "Part Of Whole"
)
part_of_whole_buttons_div = create_div_buttons(
    f"{id_page}_div_part_of_whole", visualizations_part_of_whole
)
# 1d_distribution button
one_d_button = create_button_drop(f"{id_page}_button_one_d", "1d Distribution")
one_d_buttons_div = create_div_buttons(
    f"{id_page}_div_one_d", visualizations_1d_distribution
)
# 2d_distribution
two_d_button = create_button_drop(f"{id_page}_button_two_d", "2d Distribution")
two_d_buttons_div = create_div_buttons(
    f"{id_page}_div_two_d", visualizations_2d_distribution
)
# three_dimensional
three_d_button = create_button_drop(f"{id_page}_button_three_d", "3D")
three_d_buttons_div = create_div_buttons(
    f"{id_page}_div_three_d", visualizations_three_dimensional
)

list_of_visualizations = [
    basic_button,
    basic_buttons_div,
    part_of_whole_button,
    part_of_whole_buttons_div,
    one_d_button,
    one_d_buttons_div,
    two_d_button,
    two_d_buttons_div,
    three_d_button,
    three_d_buttons_div,
]

visualizations = panel.Panel(f"{id_page}_div_visualizations")
visualizations.update_panel(list_of_visualizations, "")
visualizations.update_hidden(True)

div_visualizations = panel.Panel("")
div_visualizations.update_panel(
    [visualizations_button.create_bar_with_icon(), visualizations.panel()],
    "panel-functions",
)

panel_visualizations = div_visualizations.panel()