from .db import db
from .error import Error

class Player(db.Document):
    username = db.StringField(max_length=20, required=True, unique=True)
    display_name = db.StringField(max_length=20, required=True, unique=True)

    @classmethod
    def get_all(self):
        result = self.objects.exclude('id')
        success = True
        return result, success

    @classmethod
    def get(self, username):
        try:
            result = self.objects.exclude('id').get(username=username)
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
        except db.NotUniqueError: # When there's a player with the same username or display_name
            result = Error().id('0002')
        except db.ValidationError: # When there are missing keys in the post data
            result = Error().id('0004')
        except db.FieldDoesNotExist: # Wehn the key in the post data is incorrect
            result = Error().id('0001')
        return result, success

    @classmethod
    def update(self, username, data):
        success = False
        try:
            result = self.objects(username=username).modify(new=True, **data)
            if result == None: # If player doesn't exist
                result = Error().id('0003')
            else:
                success = True
        except db.InvalidQueryError: # If the keys of the request data are incorrect
            result = Error().id('0001')
        except db.NotUniqueError: # When there's an existing player using the new desired username/display_name
            result = Error().id('0002')
        return result, success

    @classmethod
    def delete(self, username):
        result = self.objects(username=username).delete()
        if result == 0: # If the player does not exist
            result = Error().id('0003')
            success = False
        else:
            result = None
            success = True
        return result, success
