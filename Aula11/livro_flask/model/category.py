from flask_sqlalchemy import SQAlchemy 
from config import app_config, app_active

config = app_config[app_active]

db = SQAlchemy(config.APP)

class Category(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), unique=True, nullable=False)
    description=db.Column(db.Text(), nullable=False)
