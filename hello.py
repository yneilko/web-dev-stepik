#wsgi example app

def wsgi_app(environ, start_responce):
        status = '200 OK'
        headers = ['Content-Type', 'text/plain']
        responce = environ['QUERY_STRING']
        return [ responce ]
