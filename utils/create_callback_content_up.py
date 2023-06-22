from dash import html

style_div_title = {
    "position": "relative",
    "left": "0%",
    "top": "0%",
    "width": "100%",
    "height": "100%",
}

style_title = {
    "float": "left",
    "position": "relative",
    "left": "2%",
    "top": "35%",
    "font-size": "calc(0.1rem + 1.7vw)",
    
    "font-weight": "bold",
    "font-style": "italic",
    "color": "white",
}

style_a = {
    "float": "left",
    "margin-left": "3%",
    "margin-top": "4.5vmin",
    
    "font-style": "italic",
    "font-size": "calc(0.1rem + .8vw)",
    "color": "white", 
}


def content_up_functions(name_button, is_dataFrame=True, name_button_with_=None):
    name_path = name_button
    if name_button_with_:
        name_path = name_button_with_
    href = f"https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.{name_path}.html"
    if not is_dataFrame:
        href = f"https://pandas.pydata.org/docs/reference/api/pandas.{name_path}.html"
    return html.Div(
        [
            html.Div(f"DataFrame.{name_button}()", style=style_title),
            html.A("Documentacion", href=href, target="_blank", style=style_a),
        ],
        style=style_div_title,
    )


def content_up_visualizations(name_button, path):
    href = f"https://plotly.com/python/{path}/"
    return html.Div(
        [
            html.Div(f"DataFrame.{name_button}()", style=style_title),
            html.A("Documentacion", href=href, target="_blank", style=style_a),
        ],
        style=style_div_title,
    )


def content_up_models(title, path):
    return html.Div(
        [
            html.Div(title, style=style_title),
            html.A("Documentacion", href=path, target="_blank", style=style_a),
        ],
        style=style_div_title,
    )


def content_up_existing_models(title, path, path2):
    return html.Div(
        [
            html.Div(title, style=style_title),
            html.A("Documentacion", href=path, target="_blank", style=style_a),
            html.A(
                "Git Hub",
                href=path2,
                target="_blank",
                style=style_a,
            ),
        ],
        style=style_div_title,
    )
