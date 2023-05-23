from flask import Blueprint, jsonify, request, make_response
from model import test_conn
import jwt

routes = Blueprint('routes', __name__)


@routes.get('/')
def home():
    return "<h1>Home</h1>"

# TEST DB CONNECTION


@routes.get('/db')
def test_db_conn():
    return test_conn()


@routes.get('/protected')
def protected():
    return ''


@routes.get('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password123':
        return ''
    return make_response('Could not verifiy !', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@routes.get('/unprotected')
def unprotected():
    return ''
