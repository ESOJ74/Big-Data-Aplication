functions_info = [
    ["corr", "Corr"],
    ["cov", "Cov"],
    ["describe", "Describe"],
    ["info", "Info"],
    ["kurt", "Kurt"],
    ["sem", "Sem"],
    ["t", "Transpose"],
    ["unique", "Unique"],
    ["var", "Var"],
]

functions_a_g = [
    ["drop", "Drop"],
    ["groupby", "Groupby"],
    ["getdummies", "Get Dummies"],
]

functions_h_p = [
    ["-----", "---------"],
]

functions_q_z = [["replace", "Replace"]]


visualizations_basic = [
    ["area", "Area"],
    ["bar", "Bar"],
    ["funnel", "Funnel"],
    ["line", "Line"],
    ["scatter", "Scatter Plot"],
    ["timeline", "Timeline"],
]

visualizations_part_of_whole = [
    ["icicle", "Icicle"],
    ["pie", "Pie"],
    ["sunburst", "Sunburst"],
    ["treemap", "Treemap"],
]

visualizations_1d_distribution = [
    ["histogram", "Histogram"],
    ["box", "Box"],
    ["violin", "Violin"],
    ["strip", "Strip"],
    ["ecdf", "Ecdf"],
]

visualizations_2d_distribution = [
    ["densityheatmap", "Density Heatmap"],
    ["densitycontour", "Density Contour"],
]

visualizations_three_dimensional = [
    ["scatter3d", "Scatter 3D"],
    ["line3d", "Line 3D"],
]

models_supervised = [
    ["linearregresion", "Linear Reg."],
    ["logisticregresion", "Logistic Reg."],
]

models_deep = [["prueba", "-----"]]

existing_models = [
    ["canny", "Canny"],
]

models_test = [
    ["testmodels", "Test Models"],
]

l_workflow = [
    ["workflow", "Workflow"],
]


buttons_for_functions = [
    x[0] for x in (functions_info + functions_a_g + functions_h_p + functions_q_z)
]


buttons_for_visualizations = [
    x[0]
    for x in (
        visualizations_basic
        + visualizations_part_of_whole
        + visualizations_1d_distribution
        + visualizations_2d_distribution
        + visualizations_three_dimensional
    )
]

buttons_for_models = [
    x[0] for x in (models_supervised + models_deep + existing_models + models_test)
]

list_of_buttons = [
    ["load_data", "view_data", "save_data", "workflow"],
    buttons_for_functions,
    buttons_for_visualizations,
    buttons_for_models,
]

no_apply = [
    "load_data",
    "save_data",
    "view_data",
    "workflow",
    "testmodels",
    "info",
    "t",
    "unique",
    "linearregresion",
    "logisticregresion",
]
