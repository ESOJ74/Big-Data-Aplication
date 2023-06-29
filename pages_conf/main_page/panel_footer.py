from dash import html

from dependencies.classes import panel

id_page = "main_page"

panel_git = panel.Panel()
panel_git.update_panel(
    html.A(
        "GitHub",
        href="https://github.com/ESOJ74/Big-Data-Aplication",
        className="panel-a-footer",
        target="_blank",
    ),
    className="container-a-footer"
)
panel_chat = panel.Panel()
panel_chat.update_panel(
    html.A(
        "ChatGPT",
        href="https://chat.openai.com/",
        className="panel-a-footer",
        target="_blank",
    ),
    className="container-a-footer"
)
panel_phind = panel.Panel()
panel_phind.update_panel(
    html.A(
        "Phind",
        href="https://www.phind.com/",
        className="panel-a-footer",
        target="_blank",
    ),
    className="container-a-footer"
)

footer = panel.Panel()
footer.update_panel(
    [
        panel_git.panel(),
        panel_chat.panel(),
        panel_phind.panel(),
    ],
    "panel-footer",
)

panel_footer = footer.panel()
