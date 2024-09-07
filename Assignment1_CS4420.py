import cv2
import sys
import numpy as np
import random
import os
import argparse

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
    picslist = []

    for dirpath, dirnames, filenames in os.walk(dir, topdown=False): # gets directory path, directory names, and file names
        for filename in filenames:
            picslist.append(os.path.join(dirpath, filename))
            
    #print(picslist)
    imageNumber = 0
    while True:
        pic = picslist[imageNumber]
        # Read the image
        image = cv2.imread(pic)

        # Check if the image was successfully loaded
        if image is None:
            raise Exception(f"Cannot open input image {pic}")
        
        # Image dimensions
        print (f"Image dimensions: {image.shape[1]} x {image.shape[0]}")

        # Displayimage
        cv2.imshow('Image', image)

        # Display value at a random pixel
        rows, cols, _ = image.shape
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        # Color pixel
        pxl_color = image[r, c]
        print(f"Color pixel at ({r},{c}) = ({int(pxl_color[0])}, {int(pxl_color[1])}, {int(pxl_color[2])})")

        useraction = cv2.waitKey(0) & 0xFF

        if useraction == ord('n'):
            if imageNumber < len(picslist) - 1:
                imageNumber += 1
        
        if useraction == ord('p'):
            if imageNumber > 0:
                imageNumber -= 1

        if useraction == ord('q'):
            break



if __name__ == "__main__":
    main()
    
