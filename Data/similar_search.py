from pymongo import MongoClient
import cv2
import numpy as np

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["geo_images"]
collection = db["images"]

# Query image path
query_path = "Data/beach.jpg"

# Read image
img = cv2.imread(query_path)

# Feature extraction
hist = cv2.calcHist(
    [img],
    [0, 1, 2],
    None,
    [8, 8, 8],
    [0, 256, 0, 256, 0, 256]
)

query_features = hist.flatten()

print("Searching visually similar images...\n")

# Compare with DB
for item in collection.find():

    db_features = np.array(item["features"])

    similarity = np.linalg.norm(query_features - db_features)

    print(item["image_name"])
    print("Similarity score:", similarity)
    print("--------------------")
    