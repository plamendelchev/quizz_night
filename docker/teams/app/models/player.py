from app import db

class Player(db.EmbeddedDocument):
    username = db.StringField(max_length=20, required=True, unique=True)
    display_name = db.StringField(max_length=20, required=True, unique=True)
