from app import db
from app.models import Error
from app.models import Player

class Team(db.Document):
	name = db.StringField(max_length=20, required=True, unique=True)
	display_name = db.StringField(max_length=20, required=True, unique=True)
	players = db.ListField(db.EmbeddedDocumentField(Player))

	@classmethod
	def get_all(self):
		result = self.objects.exclude('id')
		success = True
		return result, success

	@classmethod
	def get(self, name):
		try:
			result = self.objects.exclude('id')
			result.get(name=name)
			success = True
		except db.DoesNotExist:
			result = Error().id('0003')
			success = False
		return result, success

	@classmethod
	def add(self, **kwargs):
		success = False
		try:
			result = self.objects.create(**kwargs)
			success = True
		except db.NotUniqueError: # When there's a team with the same name or display_name
			result = Error().id('0002')
		except db.ValidationError: # When there are missing keys in the post data
			result = Error().id('0004')
		except db.FieldDoesNotExist: # Wehn the key in the post data is incorrect
			result = Error().id('0001')
		return result, success

	@classmethod
	def update(self, name, data):
		success = False
		try:
			result = self.objects.get(name=name)
			result.modify(**data)
		except db.DoesNotExist:
			result = Error().id('0003')
		except db.InvalidQueryError: # If the keys of the request data are incorrect
			result = Error().id('0001')
		except db.NotUniqueError: # When there's an existing team using the new desired name/display_name
			result = Error().id('0002')
		return result, success

	@classmethod
	def delete(self, name):
		success = False
		result = self.objects(name=name).delete()
		if result == 0: # If the team does not exist
			result = Error().id('0003')
		else:
			result = None
			success = True
		return result, success

	@classmethod
	def add_players(self, name, data):
		success = False
		try:
			result = self.objects.get(name=name)
			result.modify(add_to_set__players=data)
			success = True
		except db.DoesNotExist: # When the team (name) does not exist
			result = Error().id('0003')
		except db.FieldDoesNotExist:
			result = Error().id('0001')
		return result, success

	@classmethod
	def delete_players(self, name, username):
		success = False
		result = self.objects(name=name, players__username=username).delete()
		if result == 0: # If the team does not exist
			#result = Error().id('0003')
			result = 'goshoo'
		else:
			result = None
			success = True
		return result, success
