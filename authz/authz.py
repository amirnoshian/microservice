from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from authz.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
mg = Migrate()

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix='/api/v1')
apiv1 = Api(apiv1_bp)

from authz import resource 

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	mg.init_app(app, db)
	app.register_blueprint(apiv1_bp)
	return app
