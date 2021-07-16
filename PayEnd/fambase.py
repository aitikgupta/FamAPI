from pymongo import MongoClient, DESCENDING

client = MongoClient("mongo", 27017)
database = client.fambase
db = client.db

fam_collection = database.get_collection("fam_collection")

# index via description
fam_collection.create_index([
    ("title", DESCENDING),
    ("description", DESCENDING)
])
