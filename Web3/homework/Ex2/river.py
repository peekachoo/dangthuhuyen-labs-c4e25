from mongoengine import Document, StringField, IntField
import mlab

mlab.connect()

class river(Document):
    name = StringField()
    continent = StringField()
    length = StringField()

rivers = river.objects()
african_river = []
american_river = []
for r in rivers:
    if r.continent == 'Africa':
        african_river.append(r.name)
        
    if (r.continent == 'S. America' and r.length < 1000):
        american_river.append(r.name)

print("* Rivers in Africa:")
for i in african_river:
    print(i)

print("\n* Rivers in America (<1000km): ")
for i in american_river:
    print(i)