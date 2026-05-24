import streamlit as st
from pymongo import MongoClient
import cv2
import numpy as np

st.title("Geospatial Image Search")

client = MongoClient("mongodb://localhost:27017/")
db = client["geospatial"]
collection = db["images"]

# Upload image button
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Convert uploaded image
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    query_img = cv2.imdecode(file_bytes, 1)

    # Show image
    st.image(query_img, caption="Uploaded Image")
    st.success("Image uploaded successfully!")

    # Extract histogram features
    hist = cv2.calcHist(
        [query_img],
        [0, 1, 2],
        None,
        [8, 8, 8],
        [0, 256, 0, 256, 0, 256]
    )

    query_features = hist.flatten()

    st.subheader("Similar Images")

    for item in collection.find():
        db_features = np.array(item["features"])
        similarity = np.linalg.norm(query_features - db_features)

        st.write("Image:", item["image_name"])
        st.write("Similarity Score:", round(similarity, 2))
        st.write("-------------------")