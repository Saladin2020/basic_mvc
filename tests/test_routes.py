import pytest
from flask import Flask
from App import Route

@pytest.fixture
def app():
    app = Flask(__name__, template_folder='App/views')
    app.config['SECRET_KEY'] = 'mykey'
    app.config['TESTING'] = True
    app = Route().map(app)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_home_parameter_injection(client):
    x = 'foobar'
    resp = client.get(f'/home/{x}')
    assert resp.status_code == 200
    assert f'test2 {x}' in resp.get_data(as_text=True)
