from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["geo_images"]
collection = db["images"]

print("Searching nearby images...\n")

results = collection.find({
    "location": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [72.8777, 19.0760]  # Mumbai
            },
            "$maxDistance": 2000000
        }
    }
})

count = 0

for item in results:
    print(item["image_name"])
    print(item["location"]["coordinates"])
    print("-----------")
    count += 1

print("Total images found:", count) 