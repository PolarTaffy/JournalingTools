import time
import cv2 as cv
import numpy as np
import os

def displayImage(albumArt, color_list):
    #Create Background Image
    image_height = 2000
    image_width = 1000
    background = np.full((image_height, image_width, 3), 255, np.uint8)
    border = int(image_height * .4) #Border between album art and swatches
    background = cv.line(background, (0 , border), (image_width, border), (0, 0, 0), 5) #separating line


    #Album Art Section (40%)
    background = cv.putText(background, 'Album Art', (100, 100), cv.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3, cv.LINE_AA)
    albumArtSize = int(border * .7)  #image should take up about 70% of the section
    
    albumArt = cv.resize(albumArt, (albumArtSize, albumArtSize))
    y_margin = int((border - albumArtSize) / 2) #TODO: Resize album art and swatch text based on the y-margin size
    x_margin = 100
    background[y_margin: y_margin + albumArt.shape[0], x_margin: x_margin + albumArt.shape[1]] = albumArt


    #Color Swatch Section (60%)
    background = cv.putText(background, 'Colors', (100, border + 100), cv.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3, cv.LINE_AA)

    #load image file & data
    swatch_alpha = cv.imread(os.path.dirname(os.path.abspath(__file__)) + '\\swatch.png', cv.IMREAD_UNCHANGED)
    swatch = cv.imread(os.path.dirname(os.path.abspath(__file__)) + '\\swatch.png')
    swatch_alpha = cv.resize(swatch_alpha, (200, 200))
    swatch = cv.resize(swatch, (200, 200))
    
    swatch_y = border + 150
    swatch_x = x_margin
    
    #load and display each swatch
    for color in color_list:
        for y in range(swatch.shape[0]):
            for x in range(swatch.shape[1]):
                if swatch_alpha[y, x, 3] == 0:
                    #swatch[y, x, :3] = (255, 255, 255)
                    swatch[y, x, :3] = background[swatch_y + y, swatch_x + x]
                else:
                    swatch[y, x, :3] = color
        background[swatch_y: swatch_y + swatch.shape[0], swatch_x : swatch_x + swatch.shape[1]] = swatch 
        swatch_x += 250

        #TODO: Add color RGB codes underneath each swatch

        #sort not enough image space
        if swatch_x + 200 > background.shape[1]:
            swatch_y += swatch.shape[0] + 50
            swatch_x = 100


    #display to user
    cv.namedWindow("Album Colors", cv.WINDOW_NORMAL)
    cv.imshow("Album Colors", background)
    cv.waitKey(0)
    cv.destroyAllWindows()

    #TODO: Export image to png