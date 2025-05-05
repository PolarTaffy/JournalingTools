import cv2 as cv
import os
from colorDisplay import displayImage # type: ignore

#Load Image
image_dir = os.path.dirname(os.path.abspath(__file__))
imgPath = image_dir + '\\image.jpg'
image = cv.imread(imgPath) # #we are ASSUMING the input color is going to be an RGB image - generally inputs are in RGB.

if image is None:
    FileNotFoundError()
#TODO:  Implement tests for different images

#Parse Image for Colors
colorList = dict()
print("Started...")
for x in range(len(image)):
    for y in range(len(image[0])):
        #print(image[x][y].tolist())

        cur = tuple(image[x][y].tolist())
        #this would work BUT cur is a list. What data type can I use to store this data?

        #coords = (x,y)
        #use a hashmap! --> dictionary in python.
        #the x and y coords will be
        if cur not in colorList.keys():
            colorList.update({cur: 1})
        else:
            colorList[cur] = colorList[cur] + 1
print("Finished parsing!")

#Sort the color list 
sorted_items = sorted(colorList.items(), key=lambda kv: (kv[1], kv[0])) #type list
final_list:list[tuple] = sorted_items[-3:] #the top 3 colors in the album art
my_colors = [x[0] for x in final_list] #all the actual colors, first element in the list
print(my_colors)
#TODO: Customize # of exported colors with GUI


displayImage(image, my_colors)


# #TODO: Visibly display most popular colors on screen preview
# cv.namedWindow("Colors", cv.WINDOW_AUTOSIZE)
# outPath = image_dir + '\\template.png'
# outImg = cv.imread(outPath) 

# #put album art on outimg

# #
# cv.imshow('Colors', outImg)
# cv.waitKey(0) 

# cv.destroyAllWindows()

# #TODO: Export colors as png






#optional: export png of the most common ones

#make a separate file that takes an array of different colors, and then exports swatches of all the images