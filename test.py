import cv2
# Load an image from file
image = cv2.imread('test_gray.jpg')  # Replace 'test_image.jpg' with your image file path

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")
    image2 = cv2.resize(image, (600, 600))

    # Display the image in a window
    cv2.imshow('Test Image', image2)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
