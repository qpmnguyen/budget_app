from shiny import App, ui 

app_ui = ui.page_fluid(
    ui.navset_tab(
        
    )
)



def server(input, output, session):
    return(None)




app = App(app_ui, server)