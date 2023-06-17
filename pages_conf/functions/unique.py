from utils.create_callback_content_up import content_up_functions
from callbacks.functions.unique import *

id_page = "unique"

content_up = content_up_functions(id_page, False)
content_down = ""
params = [html.Div(className="no-params")]