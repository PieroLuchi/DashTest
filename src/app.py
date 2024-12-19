import dash
from dash import dcc, html, Input, Output
import requests  # For making API requests
import dash_bootstrap_components as dbc

names_with_codes = {
    'HE': 'Hermada',
    'CE12': 'Checchi',
    'MDL4': 'Maestri del Lavoro',
    'CO87': 'Comasina',
    'ZA15': 'Zanoli',
    'GRA5': 'Grassini',
    'EMP1': 'Empoli'
}

edifici= {
    'Hermada': 'HE',
    'Checchi': 'CE12',
    'Maestri del Lavoro': 'MDL4',
    'Comasina': 'CO87',
    'Zanoli': 'ZA15',
    'Grassini': 'GRA5',
    'Empoli': 'EMP1'
}


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = dbc.Container([
    html.H1("API Request Interface", className="pad-row"),

    dbc.Row([
        dbc.Label("Select Edificio"),
        dbc.Select(
            id='edificio-select',
            options=[{'label': key, 'value': value} for key, value in edifici.items()],
            value='HE'  # Default value
        ),
    ]),
    
    dbc.Row([
        dbc.Col(dbc.Label("Select Option 1"), width=2,className="pad-row"),
        dbc.Col(dbc.Select(
            id='dropdown-1',
            options=[
                {'label': 'Option 1', 'value': 'option1'},
                {'label': 'Option 2', 'value': 'option2'},
                {'label': 'Option 3', 'value': 'option3'}
            ],
            value='option1',  # Default value
            ),width=2)
    ]),
    
    dbc.Row([
        dbc.Col(dbc.Label("Select Option 2"),width=2),
        dbc.Col(dbc.Select(
            id='dropdown-2',
            options=[
                {'label': 'Choice A', 'value': 'choiceA'},
                {'label': 'Choice B', 'value': 'choiceB'},
                {'label': 'Choice C', 'value': 'choiceC'}
            ],
            value='choiceA',  # Default value
        ),width=2)
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
    Input('dropdown-1', 'value'),
    Input('dropdown-2', 'value'),
        prevent_initial_call=True

)
def send_request(n_clicks, selected_value_1, selected_value_2):
    if n_clicks > 0:  # Ensure button has been clicked
        url = "https://api.example.com/endpoint"  # Replace with your API endpoint
        params = {
            'param1': selected_value_1,
            'param2': selected_value_2
        }
        
        # response = requests.get(url, params=params)  # Make the GET request
        
        # if response.status_code == 200:
        #     return f"Response: {response.json()}"  # Display response data
        # else:
        #     return f"Error: {response.status_code} - {response.text}"
        return "mandato"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
