from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_application(config):
    application = initialize_flask(config)
    initialize_db(application)
    register_blueprints(application)
    return application

def initialize_flask(config):
    application = Flask('app')
    application.config.from_object(config)
    return application

def initialize_db(application):
    db.init_app(application)

def register_blueprints(application):
    from app.controllers import blueprints
    application.register_blueprint(blueprints)

