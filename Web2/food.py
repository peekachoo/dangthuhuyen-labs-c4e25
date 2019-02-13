from mongoengine import Document, StringField, IntField

class Food(Document):
    title = StringField(max_length=40)
    link = StringField()

    