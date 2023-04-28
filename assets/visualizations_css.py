from assets.common_css import background_dropdown

# create_visualizations
style_main_div = {   
    "width": "100%",
    "height": "100%",
}

style_div_title = {        
    "width": "20%",
    "height": "3%"
}

style_div_content = {
    "float": "left",
    "margin-left": "2%",
    "margin-top": "2vmax",
    "width": "82%",
    "height": "94%",
}

style_div_content_up = {
    "width": "90%",
    "height": "3.4vmax",
}

style_div_content_middle = {
    "margin-top": "1.5vmax",
    "width": "100%",
    "height": "69%",
}

style_div_content_down = {
    "width": "99.5%",
    "margin-top": "0.5%",
    "height": "18%",
    "color": "#060606",
}

style_div_utils = {
    "float": "left",
    "margin-left": "1%", 
    "margin-top": "1.4%",    
    "width": "15%",
    "height": "100%",
}

style_div_selectors = {
    "position": "relative",
    "top": "6%",
    "width": "70%",
    "height": "100%",
    "position": "relative",
    "top": "20%",
}

style_selector = {
    "float": "left",       
    "width": "12vmax",
    "height": "2.5em",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "color": "black",
    "background": background_dropdown,
}

style_selector2 = style_selector.copy()
style_selector2["margin-left"] = "2%"

style_selector_single = {
    "position": "relative",
    "top": "25%",
    "width": "12vmax",
    "height": "2.5em",
    "border-radius": "7px 7px 5px 5px",
    "padding": "2px 2px 0px 2px",
    "font-size": "1em",
    "color": "black",
    "background": background_dropdown,
}
