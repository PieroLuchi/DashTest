import dash
from dash import dcc, html, Input, Output
import requests  # For making API requests
import dash_bootstrap_components as dbc
import json

edifici= {
    'Hermada': 'HE',
    'Checchi': 'CE12',
    'Maestri del Lavoro': 'MDL4',
    'Comasina': 'CO87',
    'Zanoli': 'ZA15',
    'Grassini': 'GRA5',
    'Empoli': 'EMP1',
    'Test':'TES0'
}


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
n_clicks_old=0
server = app.server

app.layout = dbc.Container([
    html.H1("AiEcO Manager", className="pad-row"),

    dbc.Row([
        dbc.Col(dbc.Label("Seleziona Edificio"),width=2, className="pad-row"),
        dbc.Col(dbc.Select(
            id='edificio-select',
            options=[{'label': key, 'value': value} for key, value in edifici.items()],
            value='Test'  # Default value
        ),width=2, className="pad-row"),
    ]),
    
    dbc.Row([
        dbc.Col(dbc.Label("Attivazione"), width=2,className="pad-row"),
        dbc.Col(dbc.Select(
            id='dropdown-attivazione',
            options=[
                {'label': 'Attiva!', 'value': "True"},
                {'label': 'Disattiva!', 'value': "False"}
            ],
            value="True",  # Default value
            ),width=2, className="pad-row")
    ]),
    
    dbc.Row([
        dbc.Col(dbc.Label("Versione Algoritmo"),width=2, className="pad-row"),
        dbc.Col(dbc.Select(
            id='dropdown-versione',
            options=[
                {'label': 'Lite', 'value': 'lite'},
                {'label': 'Standard', 'value': 'standard'}
            ],
            value='lite',  # Default value
        ),width=2, className="pad-row")
    ]),

    dbc.Row([
        dbc.Col(dbc.Label("Temperatura di Attenuazione"),width=2, className="pad-row"),
        dbc.Col(dbc.Input(
                id='input-temperatura',
                type='text',  # Specify the type of input (text, number, etc.)
                placeholder='Inserisci temperatura',  # Placeholder text
                value=50,  # Default value
                ), width=2, className="pad-row")
    ]),

    dbc.Row([
    # dbc.Button('Send', id='send-button', color='primary'),
    dbc.Col(dbc.Button('Send', id='send-button', color='primary'), width=2, class_name='me-1'),
    dbc.Col(html.Div(id='response-output'), width=2, class_name='me-1') # To display API response
    ])
    
])

@app.callback(
    Output('response-output', 'children'),
    Input('send-button', 'n_clicks'),
    Input('edificio-select','value'),
    Input('dropdown-attivazione', 'value'),
    Input('dropdown-versione', 'value'),
    Input('input-temperatura', 'value'),
        prevent_initial_call=True
)
def send_request(n_clicks, nome_edificio,stato_attivazione, versione,temp_attivazione):
    global n_clicks_old
    if n_clicks!=None:
        if n_clicks>n_clicks_old:  # Ensure button has been clicked

            n_clicks_old=n_clicks

            params = {
                'nome_edificio': nome_edificio,
                'stato_attivazione': stato_attivazione,
                'versione':versione,
                'temp_attivazione':temp_attivazione
            }

            url='https://abitarefunctionapp.azurewebsites.net/api/AiEcoStateSelector?'
            
            response = requests.get(url, params=params)  # Make the GET request
            # if response.status_code == 200:
            #     return f"Response: {json.dumps(params)}"  # Display response data
            # else:
            #     return f"Error: {response.status_code}"
            return json.dumps(params)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
