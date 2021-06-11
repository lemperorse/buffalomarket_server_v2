from waitress import serve

from buffalo_market.wsgi import application

if __name__ == '__main__':
    serve(application, port='4949')