from navbar import create_navbar  
import webbrowser  
from threading import Timer  
from dash import Dash, html  
import dash  
 
# Cria uma instância do app Dash
app = Dash(__name__, use_pages=True)
#  * __name__ - refere-se ao nome do módulo Python atual
#  * use_pages=True - habilita suporte para uso de várias páginas

# Define o conteúdo da página HTML servida pelo app Dash. Bom para personalizar o layout da página. 
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Serra Rocketry</title>
        {%favicon%}
        <style>
            body {
                color: #cbcbe2;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Roboto;
                background-color: #2b2c40;
            }

            .button {
                background-color: #696cff;
                font-size: large;
                border: none;
                color: #cbcbe2;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                margin: 4px 2px;
                cursor: pointer;
                transition-duration: 0.4s;
                border: 0px;
                border-radius: 8px;
                padding: 10px 24px;
            }

            .button:hover {
                background-color: #4a4cc9;
            }

            header {
                font-size: 2vw;
                height: 90px;
                display: flex;
                padding-top: 10px;
                padding-bottom: 10px;
                align-items: center;
                justify-content: center;
            }

            .upload-data-div {
                display: flex;
                flex-direction: row;
                justify-content: center;
                margin-top: 10px;
            }

            #output-data-upload {
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 10px;
            }

            #doc-info {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 10px;
            }

            #info-intervalo {
                display: grid;
                grid-template-columns: 1fr 1.5fr;
                grid-gap: 5px;
            }

            #graph-analysis {
                display: grid;
                grid-template-columns: 2fr 1fr;
                grid-gap: 5px;
            }

            #graphv-analysis {
                display: grid;
                grid-template-columns: 2fr 1fr;
                grid-gap: 5px;
            }

            .card {
                background-color: #323249;
                border-radius: 14px;
                padding: 10px;
                margin: 10px;
                box-shadow: 0 0 0.375rem 0.25rem rgb(0 0 0 / 15%);
                border: 3px solid #232333;
            }

            h3 {
                font-size: x-large;
            }

            button h3 {
                margin: 5px;
            }

            h4 {
                margin: 5px;
                font-size: large;
            }

            h5 {
                margin: 5px;
                font-size: medium;
            }

            #graph {
                min-width: 300px;
                height: 600px;
                padding: 3px;
            }

            #graphv {
                min-width: 300px;
                height: 600px;
                padding: 3px;
            }

            #graph-live-update {
                min-width: 300px;
                height: 600px;
                padding: 3px;
            }

            #result {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 10px;
            }

            #result h4 {
                margin: 15px;
            }

            #result button {
                margin-top: 10px;
                width: 50%;
                text-align: center;
            }

            #notpass {
                margin-top: 1px;
                width: 50%;
                text-align: center;
            }

            #notpass h5 {
                color: #000000;
                border: 1px solid #D52C40;
                background-color: #CF6679;
                border-radius: 8px;
                padding: 10px 24px;
                cursor: not-allowed;
            }

            #notpassv {
                margin-top: 1px;
                width: 50%;
                text-align: center;
            }

            #notpassv h5 {
                color: #000000;
                border: 1px solid #D52C40;
                background-color: #CF6679;
                border-radius: 8px;
                padding: 10px 24px;
                cursor: not-allowed;
            }

            #name {
                margin-top: 10px;
                padding: 10px;
                width: 50%;
                border-radius: 8px;
                border: 0px;
            }

            a {
                font-size: medium;
                margin: 5px;
                color: #cbcbe2;
                outline-color: transparent;
                text-decoration: none;
                padding: 2px 1px 0;
            }

            a:hover {
                color: #e8e8f9;
            }

            a:link {
                color: #cbcbe2;
            }

            a:visited {
                color: #cbcbe2;
            }
        </style>
    </head>
    <body>
        

        {%app_entry%}

        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Cria o componente da barra de navegação
NAVBAR = create_navbar()

# Define o layout do aplicativo
app.layout = html.Div(
    [
        NAVBAR,  # Inclui o componente da barra de navegação no layout
        dash.page_container  # Adiciona o container de página para conteúdo dinâmico (proveniente das páginas extras)
    ]
)

# Função para abrir o navegador web automaticamente
def open_browser():
    webbrowser.open_new("http://localhost:8050/")

# Executa o aplicativo somente quando executado como o script principal
if __name__ == '__main__':
    # Agenda a abertura do navegador após 1 segundo usando Timer
    Timer(1, open_browser).start()

    # Executa o aplicativo Dash em modo de produção (debug=False)
    #  * debug=False - desativa o modo de depuração
    #  * debug=True - ativa o modo de depuração (útil para desenvolvimento)
    #  * port=8050 - define a porta para o aplicativo Dash
    #  * host='0.0.0.0' - permite conexões de qualquer máquina na rede
    app.run(debug=False, port=8050, host='0.0.0.0')
