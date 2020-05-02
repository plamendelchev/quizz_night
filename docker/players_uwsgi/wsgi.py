from os import environ
from app import create_application

application = create_application(environ['CONFIGURATION_SETUP'])
