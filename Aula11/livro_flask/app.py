from flask import Flask
from config import app_config, app_active
config = app_config[app_active]
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, template_folder ='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('Config.py')
    app.config['SQALCHEMY_DATABASE_URI'] = config.SQALCHEMY_DATABASE_URI
    app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route("/")
    def index():
        return 'Hello World!'
    
    return app