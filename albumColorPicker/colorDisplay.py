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
    background = cv.putText(background, 'Colors', (100, 750), cv.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3, cv.LINE_AA)

    #get color swatches
    swatch_data = cv.imread(os.path.dirname(os.path.abspath(__file__)) + '\\swatch.png', cv.IMREAD_UNCHANGED)
    swatch = cv.imread(os.path.dirname(os.path.abspath(__file__)) + '\\swatch.png')
    swatch_data = cv.resize(swatch_data, (200, 200))
    swatch = cv.resize(swatch, (200, 200))
    

    # swatch_y = 650
    # swatch_x = 150
    # for y in range(200):
    #     for x in range(200):
    #         overlay_color = swatch[y, x, :3] #this selects the r, g, and b [:3 selects the first three elements in the color information]
    #         overlay_alpha = swatch[y, x, 3] #this selects the alpha channel [alpha info is stored in channel three]

    #         #get color from background image
    #         background_color = background[swatch_y + y, swatch_x + x]
    #         composite_color = background_color * (1 - overlay_alpha) + overlay_color * overlay_alpha

    #         background[swatch_y + y, swatch_x + x] = composite_color
    

    #new approach, let's just make all pixels that have an empty alpha into white!

    swatch_y = 750
    swatch_x = 100
    for y in range(200):
        for x in range(200):
            if swatch_data[y, x, 3] == 0:
                #swatch[y, x, :3] = (255, 255, 255)
                swatch[y, x, :3] = background[swatch_y + y, swatch_x + x]

    background[swatch_y: swatch_y + swatch.shape[0], swatch_x : swatch_x + swatch.shape[1]] = swatch


    #display to user
    cv.namedWindow("Album Colors", cv.WINDOW_NORMAL)
    cv.imshow("Album Colors", background)
    cv.waitKey(0)
    #cv.destroyAllWindows()
    pass