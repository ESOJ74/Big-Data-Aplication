import plotly.graph_objects as go
from plotly.colors import sequential

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

list_of_squential = {
    "Plotly3": sequential.Plotly3,
    "Viridis": sequential.Viridis,
    "Cividis": sequential.Cividis,
    "Inferno": sequential.Inferno,
    "Magma": sequential.Magma,
    "Plasma": sequential.Plasma,
    "Turbo": sequential.Turbo,
    "Plotly3_r": sequential.Plotly3_r,
    "Viridis_r": sequential.Viridis_r,
    "Cividis_r": sequential.Cividis_r,
    "Inferno_r": sequential.Inferno_r,
    "Magma_r": sequential.Magma_r,
    "Plasma_r": sequential.Plasma_r,
    "Turbo_r": sequential.Turbo_r,
}