from dash import dcc, html


class SelectCreator:
    def __init__(
        self,
        id_dropdown,
        name_params,
        options=None,
        value="",
        multi=False,
        maxHeight=150,
    ):
        if options is None:
            options = []
        self.id_dropdown = id_dropdown
        self.name_params = name_params
        self.style_div = {
            "margin-left": "10%",
            "margin-top": "1%",
            "width": "90%",
            "height": "6%",
        }
        self.style_param = {
            "position": "relative",
            "top": "20%",
            "float": "left",
            "width": "52%",
            "font-size": "calc(0.1rem + 0.9vw)",
            "color": "white",
        }

        self.background = "transparent"
        self.options = options
        self.value = value
        self.multi = multi
        self.maxHeight = maxHeight

    def create_select(self):
        for name in self.name_params:
            return html.Div(
                [
                    html.Div(name, style=self.style_param),
                    dcc.Dropdown(
                        id=f"{self.id_dropdown}_{name}",
                        options=[
                            {
                                "label": html.Span([option]),
                                "value": option,
                            }
                            for option in self.options
                        ],
                        value=self.value,
                        multi=self.multi,
                        maxHeight=self.maxHeight,
                        className="selector-dropdown",
                    ),
                ],
                style=self.style_div,
            )
