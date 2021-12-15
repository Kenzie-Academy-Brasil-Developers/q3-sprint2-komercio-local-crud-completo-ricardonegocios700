from pytest import fixture, fail
from flask import Flask


@fixture
def app():
    try:
        return __import__("app").app
    except ModuleNotFoundError:
        fail('Verifique se o arquivo "app.py" existe na raiz do projeto')
    except AttributeError:
        fail('Verifique se a variável "app" existe dentro do arquivo "app.py"')


@fixture
def client(app: Flask):
    with app.test_client() as client:
        return client


@fixture
def app_routes(app: Flask):
    return app.url_map.bind("")
