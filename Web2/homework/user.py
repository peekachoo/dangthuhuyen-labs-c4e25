from mongoengine import Document, StringField, IntField

class User(Document):
    username = StringField(max_length=40)
    password = StringField()
