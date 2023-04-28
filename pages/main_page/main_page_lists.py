from pages.main_page.main_page_css import style_button

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
    # [<id button>, <name button>]
]))

functions = list(map(lambda x: x + [style_button],
                     [   
    ["drop_button", "Drop"],
    ["groupby_button", "Groupby"],
    ["funcion", "funcion"]
]))

visualizations = list(map(lambda x: x + [style_button],
                          [
    ["area_button", "Area"],
    ["bar_button", "Bar"],
    ["boxplot_button", "Box Plot"],
    ["heatmap_button", "Heatmap"],
    ["histogram_button", "Histogram"],
    ["line_button", "Line"],    
    ["pie_button", "Pie"],    
    ["scatter_button", "Scatter Plot"],       
    # [<id button>, <name button>]
]))

models = list(map(lambda x: x + [style_button],
                  [
    ["linear_regresion_button", "Linear Reg."],
    ["logistic_regresion_button", "Logistic Reg."],
    ["canny_button", "Canny"],
    ["model_4", "Model 4"],
    ["model_5", "Model 5"],
    # [<id button>, <name button>]
]))
