from pymongo import MongoClient
import cv2
import numpy as np

# -------------------------
# MongoDB connection
# -------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["geo_images"]
collection = db["images"]

# -------------------------
# Query image
# -------------------------
query_path = "Data/beach.jpg"

img = cv2.imread(query_path)

# Extract features
hist = cv2.calcHist(
    [img],
    [0, 1, 2],
    None,
    [8, 8, 8],
    [0, 256, 0, 256, 0, 256]
)

query_features = hist.flatten()

print("Nearby + Similar Images\n")

# -------------------------
# Geo Query
# -------------------------
results = collection.find({
    "location": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": [72.8777, 19.0760]
            },
            "$maxDistance": 2000000
        }
    }
})

# -------------------------
# Similarity Check
# -------------------------
for item in results:

    db_features = np.array(item["features"])

    similarity = np.linalg.norm(
        query_features - db_features
    )

    print("Image:", item["image_name"])
    print("Similarity Score:", similarity)
    print("--------------------")
    