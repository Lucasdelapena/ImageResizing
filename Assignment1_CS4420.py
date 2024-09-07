# Lucas de la Pena
# CS4420/5420
# Assignment 1
# 09/9/2024

import cv2
import sys
import numpy as np
import random
import os
import argparse
from screeninfo import get_monitors

# sample execution: python Assignment1_CS4420.py -rows 300 -cols 400 pictures 

def main():

    parser = argparse.ArgumentParser(prog='browser') # -h should be automatically added because of argparse
    parser.add_argument('-rows', type=int) # add argument with equal
    parser.add_argument('-cols', type=int) 
    parser.add_argument('dir')
    args = parser.parse_args()
    rows = args.rows
    cols = args.cols

    # Get monitor information
    for m in get_monitors(): #note: this gets takes the last monitor
        maxWidth = m.width
        maxHeight = m.height

    # Check if rows and cols are greater than the monitor size
    if rows > maxWidth:
        rows = maxWidth
    if cols > maxHeight:
        cols = maxHeight

    cv2.namedWindow('Image Window', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image Window', rows, cols)

    dir = args.dir
    picslist = []
    filenameList = []

    # gets directory path, directory names, and file names
    for dirpath, dirnames, filenames in os.walk(dir, topdown=False): 
        for filename in filenames:
            picslist.append(os.path.join(dirpath, filename))
            filenameList.append(filename)
                      
    imageNumber = 0 # counter for loop
    while True:
        pic = picslist[imageNumber]
        # Read the image
        image = cv2.imread(pic)

        # Check if the image was successfully loaded
        if image is None:
            filenameList.pop(imageNumber) # removing non-image files from the list
            picslist.pop(imageNumber)
            continue
        
        # File name
        print(f"File name: {filenameList[imageNumber]}")

        # File path
        print(f"File path: {os.path.dirname(pic)}")
        
        # Image dimensions
        print (f"Image dimensions: {image.shape[1]} x {image.shape[0]}")

        # Image amount of pixels
        print (f"Amount of pixels: {image.size}")

        #file size
        fileSize = os.path.getsize(pic)
        print(f"File size: {fileSize} bytes")

        #file type
        fileType = os.path.splitext(pic)[1] 
        print(f"File type: {fileType}")

        # Displayimage
        cv2.imshow('Image Window', image)

        # Display value at a random pixel
        rows, cols, _ = image.shape
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)

        # Color pixel
        pxl_color = image[r, c]
        print(f"Color pixel at ({r},{c}) = ({int(pxl_color[0])}, {int(pxl_color[1])}, {int(pxl_color[2])})")

    
        # User actions
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
    
