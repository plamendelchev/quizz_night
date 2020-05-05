from flask import Blueprint
from .controllers import *

blueprints = Blueprint('teams', __name__)

blueprints.add_url_rule('/', view_func=index, methods=['GET'])
blueprints.add_url_rule('/teams', view_func=get_teams, methods=['GET'])
blueprints.add_url_rule('/teams', view_func=add_team, methods=['POST'])
blueprints.add_url_rule('/teams/<name>', view_func=get_team, methods=['GET'])
blueprints.add_url_rule('/teams/<name>', view_func=update_team, methods=['PATCH'])
blueprints.add_url_rule('/teams/<name>', view_func=delete_team, methods=['DELETE'])
blueprints.add_url_rule('/teams/<name>/players', view_func=add_players, methods=['PATCH'])
blueprints.add_url_rule('/teams/<name>/players/<username>', view_func=delete_players, methods=['DELETE'])
