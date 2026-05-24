from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["geo_images"]
collection = db["images"]

for item in collection.find():
    print(item["image_name"])
    print(item["location"]["coordinates"])
    print("----------------")