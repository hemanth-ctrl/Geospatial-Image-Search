from pymongo import MongoClient
import cv2

# -------------------------
# MongoDB Connection
# -------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["geo_images"]
collection = db["images"]

print("MongoDB connected")


# -------------------------
# Image Data
# -------------------------
images = [
    {
        "name": "beach.jpg",
        "path": "Data/beach.jpg",
        "coordinates": [72.8777, 19.0760]  # Mumbai
    },

    {
        "name": "Dino.jpg",
        "path": "Data/Dino.jpg",
        "coordinates": [80.2707, 13.0827]  # Chennai
    },

    {
        "name": "hawksbill_sea.jpg",
        "path": "Data/hawksbill_sea.jpg",
        "coordinates": [77.5946, 12.9716]  # Bangalore
    }
]


# -------------------------
# Process each image
# -------------------------
for image in images:

    img = cv2.imread(image["path"])

    if img is None:
        print(f"Could not load {image['Dino.jpg']}")
        continue

    # Resize image
    img = cv2.resize(img, (100, 100))

    # Feature extraction
    hist = cv2.calcHist(
        [img],
        [0, 1, 2],
        None,
        [8, 8, 8],
        [0, 256, 0, 256, 0, 256]
    )

    features = hist.flatten()

    # MongoDB document
    document = {
        "image_name": image["name"],

        "location": {
            "type": "Point",
            "coordinates": image["coordinates"]
        },

        "features": features.tolist()
    }

    collection.insert_one(document)

    print(f"{image['name']} inserted successfully")


print("All images inserted")