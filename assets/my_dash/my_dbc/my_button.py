import dash_bootstrap_components as dbc


def my_button(
    id,
    children,
    style,
    color="secondary",
    className="btn btn-outline-primary",
    disabled=False,
    n_clicks=0,
):
    return dbc.Button(
        children=children,
        id=id,
        color=color,
        className=className,
        style=style,
        n_clicks=n_clicks,
        disabled=disabled,
    )
