#wsgi example app

def wsgi_app(environ, start_responce):
        status = '200 OK'
        headers = ['Content-Type', 'text/plain']
        responce = environ['QUERY_STRING']
        return [ responce ]
pythonpath = '/home/box/web'
bind = '0.0.0.0:8080'
workers = 4
gunicorn -с /etc/gunicorn.d/hello.py hello
/usr/local/lib/python2.7/hello.py