import cv2 as cv
import os
from colorDisplay import displayImage

#Load Image
image_dir = os.path.dirname(os.path.abspath(__file__))
imgPath = image_dir + '\\image.jpg'
image = cv.imread(imgPath) # Is a non-RGB image a concern?

if image is None:
    FileNotFoundError()
#TODO:  Implement tests for different images

#Parse Image for Colors
colorList = dict()
print("Started...")
for x in range(len(image)):
    for y in range(len(image[0])):
        cur = tuple(image[x][y].tolist())
        if cur not in colorList.keys(): #TODO: Filter out colors that are too similar
            colorList.update({cur: 1})
        else:
            colorList[cur] = colorList[cur] + 1
print("Finished parsing!")

#Sort the color list 
num_colors = 10
sorted_items = sorted(colorList.items(), key=lambda kv: (kv[1], kv[0])) #type list
final_list:list[tuple] = sorted_items[-num_colors:] #the top X colors in the album art
my_colors = [x[0] for x in final_list] #all the actual colors, first element in the list
print(my_colors)
#TODO: Customize # of exported colors with GUI


displayImage(image, my_colors) #TODO: Add different exported image size options?


# TODO: Export each color separately