from config import MONGODB_URI
from pymongo import MongoClient, DESCENDING

client = MongoClient(MONGODB_URI)
database = client.fambase

fam_collection = database.get_collection("fam_collection")

# index via description
fam_collection.create_index(
    [("title", DESCENDING), ("description", DESCENDING)]
)
