from my_dash.my_html.my_div import my_div

id_page = "histogram_button"

s_utils = {
    "width": "100%",
    "height": "100%",
}

def create_utils():
    return my_div(s_utils, "",
                  [
                   my_div({}, "", "hola"),
                   my_div({}, "", "f"),
                   my_div({}, "", "g"),
                   my_div({}, "", "e"),
                  ]
           )