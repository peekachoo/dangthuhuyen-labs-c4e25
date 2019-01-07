from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]

print("Total:",db.customers.estimated_document_count())

events = db.customers.count_documents(({"ref": "events"}))
print("Events:", events)

ads = db.customers.count_documents(({"ref": "ads"}))
print("Ads:", ads)

wom = db.customers.count_documents(({"ref": "wom"}))
print("WOM:", wom)

client.close()

from matplotlib import pyplot
ref_counts = [events, ads, wom]
ref_names = ["Events", "Ads", "WOM"]

pyplot.pie(ref_counts, labels=ref_names, autopct="%.1f%%", shadow=True)
pyplot.axis("equal")
pyplot.title("References")
pyplot.show()
