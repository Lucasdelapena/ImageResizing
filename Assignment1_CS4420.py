import cv2
import sys
import numpy as np
import random
import os


def main(image_file):
    try:
        # Read the image
        image = cv2.imread(image_file)
        # Check if the image was successfully loaded
        if image is None:
            raise Exception(f"Cannot open input image {image_file}")
            
        # Image dimensions
        print (f"Image dimensions: {image.shape[1]} x {image.shape[0]}")

        # Read the same image as grayscale image
        img_gray = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

        # Display grayscale image
        cv2.imshow('Grayscale Image', img_gray)
        cv2.waitKey(0)

        # Save a copy of grayscale image in a file on disk
        gray_pic_file = os.path.splitext(image_file)[0] + "_gray" + os.path.splitext(image_file)[1]
        cv2.imwrite(gray_pic_file, img_gray)

        # Display value at a random pixel
        rows, cols, _ = image.shape
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        # Color pixel
        pxl_color = image[r, c]
        print(f"Color pixel at ({r},{c}) = ({int(pxl_color[0])}, {int(pxl_color[1])}, {int(pxl_color[2])})")

        # Grayscale pixel
        pxl_gray = img_gray[r, c]
        print(f"Grayscale pixel at ({r},{c}) = {int(pxl_gray)}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} image_file")
        sys.exit(1)
    
    main(sys.argv[1])
    
