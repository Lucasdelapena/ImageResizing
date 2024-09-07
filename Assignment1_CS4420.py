import cv2
import sys
import numpy as np
import random
import os
import argparse
from pathlib import Path

# f5 to run
# python Assignment1_CS4420.py -rows 10 -cols 20 test.jpg
def main():

    parser = argparse.ArgumentParser(prog='browser')
    
    parser.add_argument('-rows', type=int) # add argument with equal
    parser.add_argument('-cols', type=int) 
    parser.add_argument('dir')
    args = parser.parse_args()
    rows = args.rows
    cols = args.cols

    dir = args.dir
    #dir_list = os.listdir(dir)
    #print(dir_list)
    picslist = []

    for dirpath, dirnames, filenames in os.walk(dir, topdown=False): # gets directory path, directory names, and file names
        for filename in filenames:
            picslist.append(os.path.join(dirpath, filename))
            
    #print(picslist)


    for pic in picslist:
        # Read the image
        image = cv2.imread(pic)

        # Check if the image was successfully loaded
        if image is None:
            raise Exception(f"Cannot open input image {pic}")
        
        # Image dimensions
        print (f"Image dimensions: {image.shape[1]} x {image.shape[0]}")

        # Read the same image as grayscale image
        img_gray = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)

        # Display grayscale image
        cv2.imshow('Grayscale Image', img_gray)
        cv2.waitKey(0)

        # Save a copy of grayscale image in a file on disk
        gray_pic_file = os.path.splitext(pic)[0] + "_gray" + os.path.splitext(pic)[1]
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


if __name__ == "__main__":
    main()
    
