import plotly.graph_objects as go

from assets.layout_templates.main_page.common_css import *

template_visualizations = go.layout.Template()
template_visualizations.layout.plot_bgcolor = "#22576a"
template_visualizations.layout.paper_bgcolor = "#2f6b81"
template_visualizations.layout.xaxis.color = color_boton_1
template_visualizations.layout.yaxis.color = color_boton_1
template_visualizations.layout.xaxis.title.font.color = color_boton_1
template_visualizations.layout.yaxis.title.font.color = color_boton_1