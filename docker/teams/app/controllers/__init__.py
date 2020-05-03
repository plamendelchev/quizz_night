from flask import Blueprint
from .controllers import *

blueprints = Blueprint('players', __name__)

blueprints.add_url_rule('/', view_func=index, methods=['GET'])
blueprints.add_url_rule('/players', view_func=get_players, methods=['GET'])
blueprints.add_url_rule('/players', view_func=add_player, methods=['POST'])
blueprints.add_url_rule('/players/<username>', view_func=get_player, methods=['GET'])
blueprints.add_url_rule('/players/<username>', view_func=update_player, methods=['PATCH'])
blueprints.add_url_rule('/players/<username>', view_func=delete_player, methods=['DELETE'])
