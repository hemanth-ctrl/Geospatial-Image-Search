from pymongo import MongoClient

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

db = client["geo_images"]
collection = db["images"]

# Create geo index
collection.create_index([("location", "2dsphere")])

print("Geo index created successfully")