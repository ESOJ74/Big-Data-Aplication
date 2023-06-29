from dash import html, dcc

class ParamInputCreator:
    def __init__(self, id_page, id_param, value=1):
        self.id_page = id_page
        self.id_param = id_param
        self.style_div_input = {
            "margin-left": "10%",
            "margin-top": "2%",
            "height": "3%",
            "width": "90%",
        }
        self.s_param = {
            "position": "relative",
            "top": "0%",
            "float": "left",
            "width": "52%",
            "font-size": "calc(0.1rem + 1vw)",
            
            "color": "white",
        }
        self.style_input = {"float": "left",
                            "width": "44%",
                            "color": "black",
                            "border": "0.5px solid var(--bs-azul-odd)",
                            "border-bottom": "2px solid var(--bs-azul-odd)",
                            "border-right": "2px solid var(--bs-azul-odd)",
                            "border-radius": "5px"}
        self.value = value

    def create_input(self):
        return html.Div(
            [
                html.Div(self.id_param, style=self.s_param),
                dcc.Input(
                    id=f"{self.id_page}_{self.id_param}",
                    style=self.style_input,
                    value=self.value,
                ),
            ],
            style=self.style_div_input,
        )