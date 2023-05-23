from flask import Blueprint
from model import test_conn

routes = Blueprint('routes', __name__)


@routes.get('/')
def home():
    return "<h1>Home</h1>"


@routes.get('/test')
def test():
    return "Test."


@routes.get('/db')
def test_db_conn():
    return test_conn()
