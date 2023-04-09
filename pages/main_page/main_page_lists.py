from pages.main_page.main_page_css import style_button

buttons = list(map(lambda x: x + [style_button],
                   [
    ["load_data_button", "Load DataFrame"],
    ["view_data_button", "View DataFrame"],
    ["save_data_button", "Save DataFrame"]
]))

functions = list(map(lambda x: x + [style_button],
                     [
    ["info_button", "DataFrame Info"],
    ["describe_button", "DataFrame Describe"],
    ["drop_columns_button", "Drop Columns"],
    ["groupby_button", "Groupby"],
    ["funcion_3", "Funcion 3"],
    ["funcion_4", "Funcion 4"],
    ["Funcion_5", "Funcion 5"],
    ["Funcion_6", "Funcion 6"],
    ["Funcion_7", "Funcion 7"],
    ["Funcion_8", "Funcion 8"],
    ["Funcion_9", "Funcion 9"],
    ["Funcion_10", "Funcion 10"],
    ["Funcion_11", "Funcion 11"],
    ["Funcion_12", "Funcion 12"],
    # [<id button>, <name button>]
]))

visualizations = list(map(lambda x: x + [style_button],
                          [
    ["histogram_button", "Histogram"],
    ["bar_button", "Bar"],
    ["scatter_button", "Scatter"],    
    ["bloxpot_button", "Bloxpot"],
    ["heatmap_button", "Heatmap"],
    ["line_button", "Line"],
    ["area_button", "Area"],
    ["pie_button", "Pie"],
    # [<id button>, <name button>]
]))

models = list(map(lambda x: x + [style_button],
                  [
    ["linear_regresion_button", "Linear Regresion"],
    ["logistic_regresion_button", "Logistic Regresion"],
    ["model_3", "Model 3"],
    ["model_4", "Model 4"],
    ["model_5", "Model 5"],
    # [<id button>, <name button>]
]))
