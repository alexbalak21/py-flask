from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)
from routes import routes  # noqa
load_dotenv()

app.config.from_envvar('APPLICATION_SETTINGS')

app.register_blueprint(routes, url_prefix='/')
