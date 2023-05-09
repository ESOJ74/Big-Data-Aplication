from dash import html


def my_div(style, id="", children="", hidden=False, className=""):
    return html.Div(
        style=style, children=children, id=id, hidden=hidden, className=className
    )
