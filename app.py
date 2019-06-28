import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html


from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server=app.server

df = pd.read_csv('alldrgs_DILI_label_summary.csv')

data=df.to_dict("records")

PAGE_SIZE = 10

colors = {
    'text': '#4682B4'
}

app.layout = html.Div([

    html.H1(children='LIVER-SAVER', style={
            'color': colors['text']}),

    html.H4("On demand Drug Induced Liver Injury (DILI) risk labels for FDA approved drugs",style={
            'color': colors['text']} ),

    html.H5("Select drug name (active ingredient) from drop-down below"),



    dcc.Dropdown(
    id="drop-down",

    options=[
        {"label": i, "value": i} for i in df['Drug_Name'].values],
    value='troglitazone'
),

    dash_table.DataTable(

    id='table-filtering',
    columns=[{"name": i, "id": i} for i in df.columns],

    style_as_list_view=False,

    style_cell_conditional=[



        {
                "if": {"row_index": 0},
                     "backgroundColor": "white",
                    'color': '404040'
        },


        {
            'if': {
                'column_id': 'DILI-Concern Label',
                'filter': '{DILI-Concern Label} eq "Most-DILI-Concern"'
            },
            'backgroundColor': '#ff9999',
            'color': '404040',
        },

        {
            'if': {
                'column_id': 'DILI-Risk Level',
                'filter': '{DILI-Risk Level} eq "High"'
            },
            'backgroundColor': '#ff9999',
            'color': '404040',
        },
            
        
    ],

        style_header={
        'backgroundColor': '#E0E0E0'
    },
        style_cell={'textAlign': 'left',
                'font_size': '20px'},
        
    pagination_settings={
        'current_page': 0,
        'page_size': PAGE_SIZE
    },


),

html.H4(children="For drugs labeled with Most-DILI-Concern, consider alternatives with lower DILI-Risk Level OR monitor liver function of patient",
    style={
            'color': colors['text']}),

    ])



@app.callback(
    Output('table-filtering', "data"),
    [Input('drop-down', "value")])
def update_table( value):
    
    dff=df
    dff=dff.loc[dff["Drug_Name"]==value]
    return dff.to_dict("records")

 
if __name__ == '__main__':
    app.run_server(debug=True)