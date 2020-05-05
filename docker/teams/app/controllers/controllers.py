from flask import request
from app.models import Team
from app.views import generate_view

# Default function
def index():
    return 'goshoooo\n'
# Get All Teams
def get_teams():
    result, success = Team.get_all()
    response = generate_view(result, success)
    return response
# Add a new Team
def add_team():
    data = request.get_json()
    result, success = Team.add(**data)
    response = generate_view(result, success)
    return response
# Get a Team by name
def get_team(name):
    result, success = Team.get(name)
    response = generate_view(result, success)
    return response
# Update a Team
def update_team(name):
    data = request.get_json()
    result, success = Team.update(name, data)
    response = generate_view(result, success)
    return response
# Delete a Team
def delete_team(name):
    result, success = Team.delete(name)
    response = generate_view(result, success)
    return response
# Add players to a Team
def add_players(name):
	data = request.get_json()
	result, success = Team.add_players(name, data)
	response = generate_view(result, success)
	return response
# Delete players from a team
def delete_players(name, username):
	result, success = Team.delete_players(name, username)
	response = generate_view(result, success)
	return response
