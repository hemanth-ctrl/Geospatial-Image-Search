from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["geo_images"]
collection = db["images"]

collection.delete_many({})

print("Database cleared successfully")