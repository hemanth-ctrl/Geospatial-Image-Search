from pymongo import MongoClient
import cv2

# -------------------------
# Connect MongoDB
# -------------------------
client = MongoClient("mongodb://localhost:27017/")

db = client["geo_images"]
collection = db["images"]

print("MongoDB connected")


# -------------------------
# Load image
# -------------------------
image_path = "Data/beach.jpg"

img = cv2.imread(r"C:\Users\authi\OneDrive\Pictures\Camera Roll\peakpx.jpg")  # Update with your image path

if img is None:
    print("Image not found")

else:
    print("Image loaded successfully")

    # Resize image
    img = cv2.resize(img, (100, 100))

    # Extract features
    hist = cv2.calcHist(
        [img],
        [0, 1, 2],
        None,
        [8, 8, 8],
        [0, 256, 0, 256, 0, 256]
    )

    features = hist.flatten()

    # -------------------------
    # Create document
    # -------------------------
    document = {
        "image_name": "beach.jpg",

        "location": {
            "type": "Point",
            "coordinates": [72.8777, 19.0760]
        },

        "features": features.tolist()
    }

    # -------------------------
    # Insert into MongoDB
    # -------------------------
    collection.insert_one(document)

    print("Data inserted successfully")