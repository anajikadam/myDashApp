import dash
import dash_bootstrap_components as dbc

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

external_scripts = [
    
    {
        'src': 'assets/script.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    },
    
]

# external CSS stylesheets
external_stylesheets = [
    
    {
        'href': 'assets/style.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=[external_stylesheets,dbc.themes.BOOTSTRAP, FONT_AWESOME])


app.config.suppress_callback_exceptions = True
app.title = 'MyDash-App'

server = app.server
server.config['SECRET_KEY'] = 'k1LUZ1fZShowB6opoyUIEJkJvS8RBF6MMgmNcDGNmgGYr' 
# i know this should not be in version control.........
