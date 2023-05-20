from dash import dcc, html


def my_dropdown(id, style, options=[], value="", placeholder="", multi=False, clearable=False, maxHeight=150):
    return dcc.Dropdown(
        style=style,
        id=id,
        options=[
            {
                "label": html.Span([option]),
                "value": option,
            }
            for option in options
        ],
        maxHeight=maxHeight,
        value=value,
        placeholder=placeholder,
        multi=multi,
        clearable=clearable,
    )
