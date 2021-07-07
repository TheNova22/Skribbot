import os
import pyautogui
from google_images_download import google_images_download
import numpy as np
from PIL import Image
from collections import defaultdict

# Required initialisation
# You can edit the whitePosX and whitePosY to your default white color box coordinates so that you dont have to take input every time.
whitePosX,whitePosY = (266,755)
# Set the time between each click as 0
pyautogui.PAUSE = 0
# Color palette from skribbl
colorsRow1 = [(254,255,255),(204,204,204),(244,44,4),(253,133,0),(254,230,0),(50,208,0),(41,192,255),(47,60,219),(180,45,198),(220,146,184),(177,101,58)]
colorsRow2 = [(0,0,0),(94,94,94),(136,22,3),(207,76,0),(237,176,0),(8,101,17),(5,107,174),(18,22,121),(105,24,124),(183,107,134),(119,63,13)]
pals = []
# Creating a dictionary that stores all the coordinates required to be visited for each color
coords = defaultdict(list)



# A function created to find the closest color
# Returns the coordinate of the color to be picked
def minColPicker(r,g,b):
    min1 = min2 = minv = row = index = 768
    for i in range(len(colorsRow1)):
        val1 = abs(r - colorsRow1[i][0]) + abs(g - colorsRow1[i][1]) + abs(b - colorsRow1[i][2])
        val2 = abs(r - colorsRow2[i][0]) + abs(g - colorsRow2[i][1]) + abs(b - colorsRow2[i][2])
        if minv > val1:
            minv = val1
            index = i
            row = 0
        if minv > val2:
            minv = val2
            index = i
            row = 1
    return whitePosX + (index * 24), whitePosY if row == 0 else whitePosY + 24



# Taking the coordinate of the white color
# Only white color is taken as every color box is 24px, so knowing the center of one block, we can reach any color.     
print("\nMove the mouse to the white color block's center and click on enter")
print('Type n to use default coordinates')
answer = input()
# You can set your default coordinates to quickly use it rather than moving to white color every single time
if answer != 'n' : whitePosX,whitePosY = pyautogui.position()
print(whitePosX,whitePosY)

# Now we will know where the canvas or the drawing shall start
print('\nMove the mouse to the top left corner of canvas and click on enter')
input()
currentX, currentY = pyautogui.position()

# Making the palette for the image
for col in colorsRow1:
    pals.append(col[0])
    pals.append(col[1])
    pals.append(col[2])
for col in colorsRow2:
    pals.append(col[0])
    pals.append(col[1])
    pals.append(col[2])

# You are required to have a list of length 768, hence we fill rest with 0's.
for v in range(768 - len(pals)):
    pals.append(0)

palette = Image.new("P",(16,16))
palette.putpalette(pals)


# Searching a clipart image in google and downloading the first result
response = google_images_download.googleimagesdownload()
print('\nEnter the title of the drawing')
word = input()
arguments = {"keywords": word, "limit":1, "print_urls":False, 'safe_search':True, 'exact_size':'200,200', 'type': 'clipart', 'format': 'jpg','no_directory' : True}
paths = response.download(arguments)
imageLoc = paths[0][word]









# Converting the image to the colors present in the palette
img = Image.open(imageLoc[0])
w = img.width
h = img.height
img = img.convert("RGB").quantize(palette=palette)
img = img.convert("RGB")

# This click is present as to shift the view to the browser rather than being focused on terminal
pyautogui.click()


# Getting the required data and appending it to the dictionary's value
# Dict format : Key = Coordinate of Color; Value = List of coordinates where that color will be used
for y in range(0,h,2):
    for x in range(0,w,2):
        r, g, b = img.getpixel((x, y))
        coords[minColPicker(r,g,b)].append((x,y))

# Sort the keys in such way so that color used the most is drawn first
for k in sorted(coords,key = lambda k : len(coords[k]), reverse=True):
    if len(coords[k]) == 0 : break
    if k == (whitePosX,whitePosY): continue
    pyautogui.click(x=k[0], y=k[1], button='left')
    for clic in coords[k]:
        # You can change the multiplicity here to 1 or 3 and so on to alter the size of the image drawn
       pyautogui.click(x=currentX + clic[0] * 2, y= currentY + clic[1] * 2, button='left')

# Move back to the initial position
pyautogui.moveTo(currentX,currentY)

# Delete the image
os.remove(imageLoc[0])