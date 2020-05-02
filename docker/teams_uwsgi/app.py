from flask import Flask, request
from classes.db import initialize_db
from classes.team import Team
from classes.myresponse import MyResponse
from os import environ

# Init Flask
application = Flask('app')
application.config.from_object(environ['CONFIGURATION_SETUP'])
application.response_class = MyResponse
# Init DB
initialize_db(application)

@application.route('/', methods=['GET', 'POST'])
def default():
    return 'goshoooo\n'
# Get All Teams
@application.route('/teams', methods=['GET'])
def get_teams():
    result, success = Team.get_all()
    response = MyResponse(result=result, success=success)
    return response
# Add a new Team
@application.route('/teams', methods=['POST'])
def add_team():
    data = request.get_json()
    result, success = Team.add(**data)
    response = MyResponse(result=result, success=success)
    return response
# Get a Team by name
@application.route('/teams/<name>', methods=['GET'])
def get_team(name):
    result, success = Team.get(name)
    response = MyResponse(result=result, success=success)
    return response
# Update a Team
@application.route('/teams/<name>', methods=['PATCH'])
def update_team(name):
    data = request.get_json()
    result, success = Team.update(name, data)
    response = MyResponse(result=result, success=success)
    return response
# Delete a Team
@application.route('/teams/<name>', methods=['DELETE'])
def delete_team(name):
    result, success = Team.delete(name)
    response = MyResponse(result=result, success=success)
    return response
# Update Team players
@application.route('/teams/<name>/players', methods=['PATCH'])
def update_team_players(name):
    data = request.get_json()
    result, success = Team.update_players(name, data)
    response = MyResponse(result=result, success=success)
    return response
