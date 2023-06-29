from dependencies.classes import (button_drop, div_button_creator,
                                  panel)

def create_button_drop(id_buttom_bar, name):
    button = button_drop.ButtonDropCreator(name, id_buttom_bar, "btn-data")
    button.style_icon = {"float": "left", "width": "8%", "height": "5%"}
    panel_button = panel.Panel("")
    panel_button.update_panel(button.panel(), "panel-button-drop-functionalities")
    return panel_button.panel()


def create_div_buttons(id_div, list_of_buttons, hidden=True):
    buttons_div = div_button_creator.DivButtonCreator(
        "info_buttons_div_panel",
        list_of_buttons,
    )
    buttons_div.update_id_div(id_div)
    buttons_div.update_hidden(hidden)
    buttons_div.update_button_classname("info_buttons_panel")
    return buttons_div.panel()