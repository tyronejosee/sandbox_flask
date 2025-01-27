from flask import Flask
from flask_migrate import Migrate

from app.config import config_by_name
from app.extensions import db, jwt, ma
from app.categories.routes import category_bp
from app.products.routes import product_bp

migrate = Migrate()


def create_app(config_name="development") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Extensions
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    return app
