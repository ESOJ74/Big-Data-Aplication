from dependencies.classes.main_page import MainPage
from pages_conf.main_page.panel_footer import panel_footer
from pages_conf.main_page.panel_middle import middle_panel
from pages_conf.main_page.panel_up import panel_up
from callbacks.main_page import *  # noqa: F403

id_page = "main_page"

main = MainPage(id_page, "panel-content-main_page")
main.update_panel_up(panel_up)
main.update_panel_footer(panel_footer)
main.update_middle_panel(middle_panel)

layout = main.main_page()


