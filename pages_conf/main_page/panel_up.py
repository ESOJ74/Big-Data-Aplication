from dependencies.classes import panel

id_page = "main_page"

panel_user = panel.Panel(f"{id_page}_panel_up_left")
panel_user.update_panel(className="panel-user")
panel_title = panel.Panel()
panel_title.update_panel("Big Data App", "panel-title")
panel_sesion = panel.Panel(f"{id_page}_panel_up_right")
panel_sesion.update_panel(className="panel-close-sesion")  

up = panel.Panel()
up.update_panel(
    [
        panel_user.panel(),
        panel_title.panel(),
        panel_sesion.panel(),
    ],
    "panel-up",
)

panel_up = up.panel()
