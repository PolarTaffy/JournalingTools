import time
import cv2 as cv
import numpy as np
import os

def displayImage(albumArt, color_list):
    background = np.full((1000, 1000, 3), 255, np.uint8)

    #place album art
    albumArt = cv.resize(albumArt, (400, 400)) #resize art to fit
    h, w = albumArt.shape[:2] #
    h = 150
    w = 100
    background[h: h + 400, w: w + 400] = albumArt

    #place text
    background = cv.putText(background, 'Album Art', (100, 100), cv.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3, cv.LINE_AA)
    background = cv.putText(background, 'Colors', (100, 675), cv.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3, cv.LINE_AA)

    #get color swatches
    swatch_data = cv.imread(os.path.dirname(os.path.abspath(__file__)) + '\\swatch.png', cv.IMREAD_UNCHANGED)
    swatch = cv.imread(os.path.dirname(os.path.abspath(__file__)) + '\\swatch.png')
    swatch_data = cv.resize(swatch_data, (200, 200))
    swatch = cv.resize(swatch, (200, 200))
    
    
    #Display all color swatches to users!
    swatch_y = 700
    swatch_x = 100

    for color in color_list:
        for y in range(200):
            for x in range(200):
                if swatch_data[y, x, 3] == 0:
                    #swatch[y, x, :3] = (255, 255, 255)
                    swatch[y, x, :3] = background[swatch_y + y, swatch_x + x]
                else:
                    swatch[y, x, :3] = color
        background[swatch_y: swatch_y + swatch.shape[0], swatch_x : swatch_x + swatch.shape[1]] = swatch 
        swatch_x += 250


    #display to user
    cv.namedWindow("Album Colors", cv.WINDOW_NORMAL)
    cv.imshow("Album Colors", background)
    cv.waitKey(0)
    #cv.destroyAllWindows()
    pass