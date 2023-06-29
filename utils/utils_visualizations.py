from dash import dcc, html

from utils.in_out import save_panel

style_msg = {
    "color": "white",
    "font-size": "1vmax",
    "margin-left": "2%",
}


def panel_guardado():
    return html.H6(
        "Panel Guardado",
        style=style_msg,
    )


def error(msg):
    return html.H6(
        str(msg).__str__(),
        style=style_msg,
    )


def create_graph(fig):
    return dcc.Graph(
        figure=fig,
        style={"height": "100%", "background": "white"},
    )


def create_result(name_button, fig, name_fig):
    if name_button == "Apply":
        name_button = "Save Panel"
        content = create_graph(fig)
    else:
        save_panel(fig, name_fig)
        content = panel_guardado()
        name_button = "Apply"
    return name_button, content
