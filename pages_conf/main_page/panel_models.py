from buttons_conf import (existing_models, models_deep, models_supervised,
                          models_test)
from dependencies.classes import button_bar, panel
from pages_conf.main_page.utils import create_button_drop, create_div_buttons

id_page = "main_page"

# button bar
models_button = button_bar.BarWithIconCreator(
    "Models", f"{id_page}_button_show_models", "btn-functionalities"
)

# supervised_button
supervised_button = create_button_drop(
    f"{id_page}_button_supervised", "Machine Learning"
)
supervised_buttons_div = create_div_buttons(
    f"{id_page}_div_supervised", models_supervised
)
# deep_learning_button
deep_learning_button = create_button_drop(
    f"{id_page}_button_deep_learning", "Deep Learning"
)
deep_learning_buttons_div = create_div_buttons(
    f"{id_page}_div_deep_learning", models_deep
)
# existing_models_button
existing_models_button = create_button_drop(
    f"{id_page}_button_existing_models", "Existing Models"
)
existing_models_buttons_div = create_div_buttons(
    f"{id_page}_div_existing_models", existing_models
)


list_of_models = [
    supervised_button,
    supervised_buttons_div,
    deep_learning_button,
    deep_learning_buttons_div,
    existing_models_button,
    existing_models_buttons_div,
]

models = panel.Panel(f"{id_page}_div_models")
models.update_panel(list_of_models, "")
models.update_hidden(True)

div_models = panel.Panel("")
div_models.update_panel(
    [models_button.create_bar_with_icon(), models.panel()], "panel-functions"
)

panel_models = div_models.panel()