import dash
import dash_core_components as dcc
import dash_html_components as html

from server import app, server

from datetime import datetime
import time 

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    dcc.Link('Generat Report'
                    , href='/generat_report'),
    html.Br(),
    dcc.Link('PDF Generate'
                    , href='/generat_pdf'),
    html.Br(),
    dcc.Link('Report sent email'
                    , href='/Latest_Report_sent_email'),
    # content will be rendered in this element
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if ('sent_email' in pathname):
        print("flag0.0")
        from Email import sendEmail
        sendEmail()
        return html.Div([
            html.H3('You are on page of sending report through Email'),])

    if ('at_report' in pathname):
        print("flag0")
        from layout_1 import appMain_layout
        return appMain_layout

    if ('pdf' in pathname):
        print("flag1")
        x = datetime.now()
        file_name = str(x.date())+'_'+str(x.strftime("%X").replace(':','-'))
        filename = "assets/pdf/CovidReport_"+file_name+".pdf"
        from PDFgen import PDFgenerate
        mObj = PDFgenerate()
        mObj.create_pdf_report(filename)
        filename1 = "pdf/CovidReport_"+file_name+".pdf"
        dwn_filename = "CovidReport_"+file_name+".pdf"
        return html.Div([
            html.H3('You are on page PDF Generate {}'.format(filename)),
            html.A("PDF File",download=dwn_filename, href=app.get_asset_url("{}".format(filename1))),])
    if len(pathname)<9:
        return html.Div([html.H3('You are on page {}'.format(pathname)),   ])

if __name__ == '__main__':
    app.run_server(debug=True)

