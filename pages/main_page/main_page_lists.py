from assets.layout_templates.main_page.common_css import *

style_button = {       
    "margin-top": "1%",
    "margin-left": "5%",
    "width": "100%",
    "font-size": "0.6vmax",
    "font-weight": "bold",
    "font-family": font_family,
    "border": "2px solid #b0d8d3",
    "color": color_boton_1,
}

buttons_data = list(map(lambda x: x + [style_button],                   [
    ["load_data_button", "Load"],
    ["save_data_button", "Save"]    
]))

buttons = list(map(lambda x: x + [style_button],
                   [
    
    ["view_data_button", "View"]
    
]))

functions_info = list(map(lambda x: x + [style_button],
                     [
    ["corr_button", "Corr"],
    ["cov_button", "Cov"],    
    ["describe_button", "Describe"],
    ["info_button", "Info"],
    ["kurt_button", "Kurt"],
    ["sem_button", "Sem"],
    ["t_button", "Transpose"],
    ["unique_button", "Unique"],
    ["var_button", "Var"],
]))

functions = list(map(lambda x: x + [style_button],
                     [   
    ["drop_button", "Drop"],
    ["groupby_button", "Groupby"],
    ["prueba_button", "Prueba"]
]))

visualizations_basic = list(map(lambda x: x + [style_button],
                          [
    ["area_button", "Area"],
    ["bar_button", "Bar"],
    ["funnel_button", "Funnel"],    
    ["line_button", "Line"],            
    ["scatter_button", "Scatter Plot"], 
    ["timeline_button", "Timeline"]
]))

visualizations_part_of_whole = list(map(lambda x: x + [style_button],
                          [  
    ["icicle_button", "Icicle"],
    ["pie_button", "Pie"],
    ["sunburst_button", "Sunburst"],
    ["treemap_button", "Treemap"],
]))



models_supervised = list(map(lambda x: x + [style_button],
                  [
    ["linear_regresion_button", "Linear Reg."],
    ["logistic_regresion_button", "Logistic Reg."],    
]))

models_deep = list(map(lambda x: x + [style_button],
                  [
    ["canny_button", "Canny"],
]))