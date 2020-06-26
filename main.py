from app import app
from app import config
from flup.server.fcgi import WSGIServer

if __name__ == '__main__':
    if (config.DEBUG):
        app.run(host='127.0.0.1', port=config.S_PORT, debug=config.DEBUG)
    else:
        WSGIServer(app, bindAddress=('127.0.0.1', config.S_PORT)).run()
