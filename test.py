import cv2

# Load image
image_path = "Data/beach.jpg"
img = cv2.imread(r"C:\Users\authi\OneDrive\Pictures\Camera Roll\peakpx.jpg")

if img is None:
    print("Image not found")

else:
    print("Image loaded successfully")

    # Resize image
    img = cv2.resize(img, (100, 100))

    # Extract color histogram features
    hist = cv2.calcHist(
        [img],
        [0, 1, 2],
        None,
        [8, 8, 8],
        [0, 256, 0, 256, 0, 256]
    )

    # Convert to one-dimensional array
    features = hist.flatten()

    print("Feature extraction successful")
    print(features[:10])  