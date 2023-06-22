from dash import dcc, html
from pandas import set_option, DataFrame
from dependencies.classes.my_dash_table import MyDashTable


def create_obj(df, fig, state_button, axis=0):
    set_option("display.max_columns", 500)
    set_option("display.width", 1000)
    style_table = {
        "margin-left": "3%",
        "margin-top": "3.5%",
        "width": "95%",
        "max-height": "500px",
        "text-align": "left",
        "overflow": "auto",
    }
    style_data = {
        "padding": "-5px",
        "text-align": "left",
        "height": "0.5vmin",

        "font-size": "0.7vmax",
        "border": "transparent",
        "color": "#535353",
        "background": "#E8F6FF",
        "border-radius": "10px",
    }
    style_cell = {
        "min-width": "2%",
        "max-width": "2%",
        "padding": "-5px",
    }
    style_header = {        
        "color": "white",

        "font-size": "0.8vmax",
        "font-weight": "bold",
        "text-align": "left",
        "border": "transparent",
        "background": "#08397E",
    }
    style_data_conditional = [
        {
            "if": {"row_index": "odd"},
            "color": "white",
            "backgroundColor": "#9EC7FC",
            "border": "transparent",
            "borderRadius": "35px",
        },
        {
            "if": {"column_id": "-"},
            "width": "20%",
            "font-size": "0.8vmax",
            "font-weight": "bold",
        },
    ]
    df = df.round(decimals=5)
    try:
        df.insert(0, "-", df.columns)
    except Exception:
        try:
            df = DataFrame({"Class": df.index, "Values": df.values})
            style_table = {
                "margin-left": "30%",
                "margin-top": "5%",
                "width": "35%",
                "max-height": "500px",
                "text-align": "left",
                "overflow-x": "auto",
                "overflow-y": "auto"
            }
        except Exception:
            df.insert(0, "-", df.index)
    obj = MyDashTable.my_dash_table(
        df,
        style_table,
        style_data,
        style_header,
        style_cell,
        style_data_conditional,
    )
    if state_button == "btn-on":
        if axis == 0:
            obj = dcc.Graph(
                figure=fig,
                style={
                    "margin-left": "2%",
                    "width": "98%",
                    "height": "100%"},
            )
        else:
            obj = html.H6(
                "Gráfico disponible solo para axis=0",
                style={
                    "color": "white",
                    "font-size": "1vmax",
                    "margin-left": "2%",
                },
            )
    return obj


def create_msg(msg):
    return html.Div(
        msg.__str__(),
        style={
            "position": "relative",
            "top": "4%",
            "left": "5%",
            "color": "white",
            "font-family": "inherit",
            "font-size": "1vmax",
            "font-weight": "bold",
        },
    )
