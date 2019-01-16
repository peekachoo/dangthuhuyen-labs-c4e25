from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds131546.mlab.com:31546/c4e25"

# Connect to mlab server:
client = MongoClient(uri)

# Get a database:
db = client.get_database()

# Get a collection:
    # collection = db.get_collection
post_collection = db["posts"] # dictionary style

# Create a document:
new_post = {
    "title": "Hom nay troi mua", # field
    "content": "Toi ra duong code",
}
    # import datetime
    # post = {"author": "Mike",
    #         "text": "My first blog post!",
    #         "tags": ["mongodb", "python", "pymongo"],
    #         "date": datetime.datetime.utcnow()}

# Insert document:
# post_collection.insert_one(new_post)
    # posts = db.posts
    # post_1 = posts.insert_one(post).inserted_id
    # post_1

# Query for mote than one doc:
# for post in post_collection.find():
#     print(post)

# Lazy loading:
post_list = post_collection.find() # cursor
first_post = post_list[0]
print(first_post)

# for post in post_collection.fing();
# print(post)

# Exit:
client.close()