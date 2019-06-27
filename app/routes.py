from app import app
@app.route('/')
@app.route('/index')
def index():
    user={"username":'rajat'}
    return'''
    <html>
    <head>
<title>My Application</title>
    </head>
    <body bgcolor='cyan'>
<h1>Hello,'''+ user['username']+'''!</h1>
    </body>
    </html>'''
