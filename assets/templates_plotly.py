import plotly.graph_objects as go

from assets.layout_templates.main_page.common_css import *

template_visualizations = go.layout.Template()
template_visualizations.layout.plot_bgcolor = "#eff3f7"
template_visualizations.layout.paper_bgcolor = "#eff3f7"
template_visualizations.layout.xaxis.color = "black"
template_visualizations.layout.yaxis.color = "black"
template_visualizations.layout.xaxis.showgrid = True
template_visualizations.layout.yaxis.showgrid = True
template_visualizations.layout.xaxis.title.font.color = "black"
template_visualizations.layout.yaxis.title.font.color = "black"
template_visualizations.layout.legend.font.color = "black"
#template_visualizations.layout.margin = dict(t=40, l=25, r=25, b=35)
