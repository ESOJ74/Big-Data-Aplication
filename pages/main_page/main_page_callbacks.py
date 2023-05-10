from importlib import import_module

from dash import callback, html
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify
from pandas import read_csv

from assets.layout_templates.main_page.common_css import *
from assets.layout_templates.main_page.main_page_css import *
from pages.main_page.main_page_lists import *

id_page = "main_page"


def create_callback(buttons_list, module, button_name=""):
    @callback(
        [Output("main_page_page_content", "children",
                allow_duplicate=True)] +
        list(map(lambda x: Output(x[0], "n_clicks"),
                 buttons_list)),      
        list(map(lambda x: Input(x[0], "n_clicks"),
                 buttons_list)),
        prevent_initial_call=True)
    def display_page(*args):
        button = buttons_list[list(args).index(1)][0]
        cont = [
            import_module(
                f'pages.{module}.{button}.{button}_layout'
            ).layout]        
        return cont + [0 for x in buttons_list] 


create_callback(buttons, "dataframe_pages")
create_callback(buttons_data, "dataframe_pages.data_pages")
create_callback(visualizations_basic,
                "visualization_pages.basics")
create_callback(visualizations_part_of_whole,
                "visualization_pages.part_of_whole")
create_callback(visualizations_1d_distribution,
                "visualization_pages.oned_distribution")
create_callback(visualizations_2d_distribution,
                "visualization_pages.twod_distribution")
create_callback(visualizations_three_dimensional,
                "visualization_pages.three_dimensional")

create_callback(functions_info, "functions_pages.info_pages")
create_callback(functions_a_g, "functions_pages.a_g")
create_callback(functions_h_p, "functions_pages.h_p")
create_callback(functions_q_z, "functions_pages.q_z")

create_callback(models_supervised,
                "models_pages.machine_learning.supervised")
create_callback(models_deep, "models_pages.deep_learning")
create_callback(existing_models, "models_pages.existing_models")
create_callback(models_test, "models_pages")

create_callback(workflow, "workflow_pages")

@callback([
           Output(f"{id_page}_div_data", "hidden"),
           Output(f"{id_page}_div_buttons_info", "hidden"),
           Output(f"{id_page}_div_buttons_a_g", "hidden"),
           Output(f"{id_page}_div_buttons_h_p", "hidden"),
           Output(f"{id_page}_div_buttons_q_z", "hidden"),
           Output(f"{id_page}_div_buttons_basics", "hidden"), 
           Output(f"{id_page}_div_buttons_part_of_whole", "hidden"),       
           Output(f"{id_page}_div_buttons_machine", "hidden"), 
           Output(f"{id_page}_div_buttons_deep", "hidden"),
           Output(f"{id_page}_div_buttons_existing_models", "hidden"),
           Output(f"{id_page}_div_buttons_1d_distribution", "hidden"),
           Output(f"{id_page}_div_buttons_2d_distribution", "hidden"),
           Output(f"{id_page}_div_buttons_3d_dimensional", "hidden"),

           Output(f"{id_page}_button_data", "n_clicks"),
           Output(f"{id_page}_button_drop_info", "n_clicks"), 
           Output(f"{id_page}_button_a_g", "n_clicks"),
           Output(f"{id_page}_button_h_p", "n_clicks"),
           Output(f"{id_page}_button_q_z", "n_clicks"),
           Output(f"{id_page}_button_basics", "n_clicks"), 
           Output(f"{id_page}_button_part_of_whole", "n_clicks"),  
           Output(f"{id_page}_button_machine", "n_clicks"), 
           Output(f"{id_page}_button_deep", "n_clicks"),  
           Output(f"{id_page}_button_existing_models", "n_clicks"),
           Output(f"{id_page}_button_1d_distribution", "n_clicks"),
           Output(f"{id_page}_button_2d_distribution", "n_clicks"),
           Output(f"{id_page}_button_3d_dimensional", "n_clicks"),
          ],
          [
           Input(f"{id_page}_button_data", "n_clicks"),
           Input(f"{id_page}_button_drop_info", "n_clicks"),
           Input(f"{id_page}_button_a_g", "n_clicks"),
           Input(f"{id_page}_button_h_p", "n_clicks"),
           Input(f"{id_page}_button_q_z", "n_clicks"),
           Input(f"{id_page}_button_basics", "n_clicks"),
           Input(f"{id_page}_button_part_of_whole", "n_clicks"),
           Input(f"{id_page}_button_machine", "n_clicks"), 
           Input(f"{id_page}_button_deep", "n_clicks"), 
           Input(f"{id_page}_button_existing_models", "n_clicks"),
           Input(f"{id_page}_button_1d_distribution", "n_clicks"),
           Input(f"{id_page}_button_2d_distribution", "n_clicks"),
           Input(f"{id_page}_button_3d_dimensional", "n_clicks"),
          ],
          [
           State(f"{id_page}_div_data", "hidden"),
           State(f"{id_page}_div_buttons_info", "hidden"),
           State(f"{id_page}_div_buttons_a_g", "hidden"),
           State(f"{id_page}_div_buttons_h_p", "hidden"),
           State(f"{id_page}_div_buttons_q_z", "hidden"),
           State(f"{id_page}_div_buttons_basics", "hidden"),
           State(f"{id_page}_div_buttons_part_of_whole", "hidden"),
           State(f"{id_page}_div_buttons_machine", "hidden"), 
           State(f"{id_page}_div_buttons_deep", "hidden"),
           State(f"{id_page}_div_buttons_existing_models", "hidden"),
           State(f"{id_page}_div_buttons_1d_distribution", "hidden"),
           State(f"{id_page}_div_buttons_2d_distribution", "hidden"),
           State(f"{id_page}_div_buttons_3d_dimensional", "hidden"),
          ],
          prevent_initial_call=True,)
def auth_display(click_data, click_info, click_a_g, click_h_p, click_q_z,
                 click_basics, click_whole, 
                 click_machine, click_deep, click_existing_models,
                 click_1d_distribution, click_2d_distribution,
                 click_3d_dimensional,
                 state_hidden_data, state_hidden_info, state_hidden_a_g,
                 state_hidden_h_p, state_hidden_q_z, state_basics,
                 state_whole, state_machine, state_deep,
                 state_existing_models, state_1d_distribution,
                 state_2d_distribution, state_3d_dimensional):   

    if click_data:
        state_hidden_data = not state_hidden_data

    if click_info:
        state_hidden_info = not state_hidden_info

    if click_a_g:
        state_hidden_a_g = not state_hidden_a_g

    if click_h_p:
        state_hidden_h_p = not state_hidden_h_p

    if click_q_z:
        state_hidden_q_z = not state_hidden_q_z

    if click_basics:
        state_basics = not state_basics

    if click_whole:
        state_whole = not state_whole

    if click_1d_distribution:
        state_1d_distribution = not state_1d_distribution

    if click_2d_distribution:
        state_2d_distribution = not state_2d_distribution
    
    if click_3d_dimensional:
        state_3d_dimensional = not state_3d_dimensional

    if click_machine:
        state_machine = not state_machine

    if click_deep:
        state_deep = not state_deep

    if click_existing_models:
        state_existing_models = not state_existing_models

    return [state_hidden_data, state_hidden_info, state_hidden_a_g,
            state_hidden_h_p, state_hidden_q_z,
            state_basics, state_whole, state_machine,
            state_deep, state_existing_models, state_1d_distribution,
            state_2d_distribution, state_3d_dimensional,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


@callback([
           Output("panel_functions", "hidden", allow_duplicate=True),
           Output("panel_visualizations", "hidden", allow_duplicate=True),
           Output("panel_models", "hidden", allow_duplicate=True),
           Output("panel_workflow", "hidden", allow_duplicate=True),           

           Output("button_show_functions", "n_clicks"),
           Output("button_show_visualizations", "n_clicks"),
           Output("button_show_models", "n_clicks"),
           Output("button_show_workflow", "n_clicks"),
          ],
          [
          Input("button_show_functions", "n_clicks"),
          Input("button_show_visualizations", "n_clicks"),
          Input("button_show_models", "n_clicks"),
          Input("button_show_workflow", "n_clicks"),
          ],
          [
           State("panel_functions", "hidden"),
           State("panel_visualizations", "hidden"),
           State("panel_models", "hidden"),
           State("panel_workflow", "hidden")
          ],
          prevent_initial_call=True,)
def auth_display(button_functions, button_visualizations, button_models,
                 button_workflow,
                 state_panel_functions, state_panel_visualizations,
                 state_panel_models, state_panel_workflow):    
    
    if button_functions:
        state_panel_functions = not state_panel_functions
        
    if button_visualizations:
        state_panel_visualizations = not state_panel_visualizations
        
    if button_models:
        state_panel_models = not state_panel_models
        
    if button_workflow:
        state_panel_workflow = not state_panel_workflow       

    return [state_panel_functions, state_panel_visualizations,
            state_panel_models, state_panel_workflow, 0, 0, 0, 0]


@callback([
           Output(f"{id_page}_div_button_cover", "style"),
           Output(f"{id_page}_button_cover", "style"),
           Output(f"{id_page}_button_cover", "children"),
           Output(f"{id_page}_div_middle_left", "hidden",
                  allow_duplicate=True),
           Output(f"{id_page}_page_content", "style")
          ],
          Input(f"{id_page}_button_cover", "n_clicks"),
          prevent_initial_call=True,)
def auth_display(n_clicks):        
    if n_clicks % 2 !=0:
        return [style_div_button_cover_left,
                style_button_cover_left,
                DashIconify(
                    icon="ic:baseline-arrow-circle-right",
                    width=30
                ),
                True,
                style_div_content2]
    else:
        return [style_div_button_cover_right,
                style_button_cover_right,
                DashIconify(
                    icon="ic:baseline-arrow-circle-left",
                    width=30
                ),
                False,
                style_div_content]


@callback([
           Output(f"{id_page}_div_middle_left", "hidden",
                  allow_duplicate=True),
           Output(f"{id_page}_div_registry", "hidden"),
           Output(f"{id_page}_store", "data"),
           Output(f"{id_page}_panel_up_left", "children"),
           Output(f"{id_page}_panel_up_right", "children"),
           Output(f"{id_page}_reg_answer", "children")
          ],
          Input(f"{id_page}_reg_accept", "n_clicks"),
          [
            State(f"{id_page}_reg_user", "value"),
            State(f"{id_page}_reg_pass", "value") 
          ],
          prevent_initial_call=True,)
def auth_display(n_clicks, reg_user, reg_pass):
    left_hidden = True
    registry_hidden = False
    user_div = ""
    sesion_div = ""
    reg_answer = ""
    data = {}

    if n_clicks:
        df = read_csv("users.csv")        
        if reg_user in list(df["user"]):
            password = df[df["user"] == reg_user]["password"].iloc[0]
            if str(password) == str(reg_pass):
                left_hidden = False
                registry_hidden = True
                user_div = html.H6(f"User: {reg_user}",
                                   style={"font-weight": "bold",
                                          "color": color_boton_1})
                sesion_div = html.A("Cerrar Sesión", href="/",
                                    style={"color": "black"})
                data = {"user": reg_user}
            else:
                reg_answer = "Contraseña incorrecta"
        else:
            reg_answer =  "Usuario no registrado"
    return [left_hidden, registry_hidden, data,
            user_div, sesion_div, reg_answer] 