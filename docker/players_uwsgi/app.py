from flask import Flask, request
from classes.db import initialize_db
from classes.player import Player
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
# Get All Players
@application.route('/players', methods=['GET'])
def get_players():
    result, success = Player.get_all()
    response = MyResponse(result=result, success=success)
    return response
# Add a new Player
@application.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()
    result, success = Player.add(**data)
    response = MyResponse(result=result, success=success)
    return response
# Get a Player by username
@application.route('/players/<username>', methods=['GET'])
def get_player(username):
    result, success = Player.get(username)
    response = MyResponse(result=result, success=success)
    return response
# Update a Player
@application.route('/players/<username>', methods=['PATCH'])
def update_player(username):
    data = request.get_json()
    result, success = Player.update(username, data)
    response = MyResponse(result=result, success=success)
    return response
# Delete a Player
@application.route('/players/<username>', methods=['DELETE'])
def delete_player(username):
    result, success = Player.delete(username)
    response = MyResponse(result=result, success=success)
    return response
