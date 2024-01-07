from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from project.app.db import mongo

from project.blueprints.Customer import bp as Customer
from project.blueprints.Supplier import bp as Supplier
from project.blueprints.Category import bp as Category
from project.blueprints.Product import bp as Product
from project.blueprints.Department import bp as Department
from project.blueprints.Store import bp as Store
from project.blueprints.Employee import bp as Employee
from project import config
import os


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"
    app.config[
        "MONGO_URI"
    ] = f"mongodb://{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "mysql+pymysql://root:kashif@localhost:3306/sms"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    mongo.init_app(app)
    app.config[
        "JWT_SECRET_KEY"
    ] = "60b8b427938bc9f2fbe65d98640e831b4a8522f56150b97f141677d02570819b"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
    UPLOAD_FOLDER = "uploads"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    jwt = JWTManager(app)

    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    # with app.app_context():
    #     db.create_all()
    app.register_blueprint(Customer)
    app.register_blueprint(Supplier)
    app.register_blueprint(Category)
    app.register_blueprint(Product)
    app.register_blueprint(Department)
    app.register_blueprint(Store)
    app.register_blueprint(Employee)
    return app
