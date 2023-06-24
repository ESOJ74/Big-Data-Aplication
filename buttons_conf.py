"""
This module contains lists of functions, visualizations, and models for data analysis
and visualization.

Functions:
- functions_info: Information about various data analysis functions, such as
  correlation, covariance, descriptive statistics, etc.
- functions_a_g: Functions starting with letters A to G, including data dropping,
  grouping, and creating dummy variables.
- functions_h_p: Currently empty, possibly a placeholder for functions starting with
  letters H to P.
- functions_q_z: Functions starting with letters Q to Z, including data replacement.

Visualizations:
- visualizations_basic: Basic visualizations like area plots, bar plots, line plots,
  scatter plots, etc.
- visualizations_part_of_whole: Visualizations representing part-of-whole relationships,
  such as pie charts, treemaps, etc.
- visualizations_1d_distribution: Visualizations representing one-dimensional
  distributions, such as histograms, box plots, violin plots, etc.
- visualizations_2d_distribution: Visualizations representing two-dimensional
  distributions, such as density heatmaps, density contours, etc.
- visualizations_three_dimensional: Visualizations representing three-dimensional data,
  such as 3D scatter plots, 3D line plots, etc.

Models:
- models_supervised: Supervised machine learning models, such as linear regression and
  logistic regression.
- models_deep: Currently contains a placeholder entry for a deep learning model.
- existing_models: Existing models, specifically the "Canny" model.
- models_test: Test models.

Other:
- l_workflow: Information about a workflow.

Buttons:
- buttons_for_functions: A list of function names that can be used as buttons in an
  interface.
- buttons_for_visualizations: A list of visualization names that can be used as buttons
  in an interface.
- buttons_for_models: A list of model names that can be used as buttons in an interface.
- list_of_buttons: A list containing different button groups, including general actions,
  function buttons, visualization buttons, and model buttons.

Note: The lists in this module are intended for creating interactive interfaces or
      menus, where users can select options from the defined functions, visualizations,
      and models. The "no_apply" list specifies functions that should not be applied
      automatically, indicating that some functions require additional user input before
      being executed.
"""

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
