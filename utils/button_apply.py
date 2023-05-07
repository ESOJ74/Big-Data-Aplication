from assets.my_dash.my_html.my_div import my_div
from utils.create_agGrid import create_adgrid

style_div_table = {
    "widht": "100%",
    "height": "80%",
}

def button_apply(id_page, df, msg):   
    content = [my_div(style_div_table, "",
                      create_adgrid(f"{id_page}_ag-table", df.head(9))),
               msg]    
    return "Save Changes", content

def button_save(file, actions):
    with open(file, "a") as file:
        for action in actions:
            file.write(action+"\n") 
    return "Apply", "Guardado"