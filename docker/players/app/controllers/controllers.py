from flask import request
from app.models import Player
from app.views import generate_view

# Default function
def index():
    return 'goshoooo\n'
# Get All Players
def get_players():
    result, success = Player.get_all()
    response = generate_view(result, success)
    return response
# Add a new Player
def add_player():
    data = request.get_json()
    result, success = Player.add(**data)
    response = generate_view(result, success)
    return response
# Get a Player by username
def get_player(username):
    result, success = Player.get(username)
    response = generate_view(result, success)
    return response
# Update a Player
def update_player(username):
    data = request.get_json()
    result, success = Player.update(username, data)
    response = generate_view(result, success)
    return response
# Delete a Player
def delete_player(username):
    result, success = Player.delete(username)
    response = generate_view(result, success)
    return response
