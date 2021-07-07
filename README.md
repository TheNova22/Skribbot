# Skribbot
Skribbot is a drawing bot created using python for games played on skribbl.

## Examples

### Gifs
![Donald Duck](https://github.com/TheNova22/Skribbot/blob/master/screenshots/donaldDuck.gif)   ![Cave](https://github.com/TheNova22/Skribbot/blob/master/screenshots/cave.gif)

### Images
#### Dragon
![Dragon](https://github.com/TheNova22/Skribbot/blob/master/screenshots/dragon.png)
#### Tree
![Tree](https://github.com/TheNova22/Skribbot/blob/master/screenshots/tree.png)

## Installation
- After cloning the repo, make sure you install google_image_download and pyautogui by running the following:</br>
```pip install google_images_download```</br>
```pip install pyautogui```

## Running
- Call the python program from terminal at the turn you are supposed to draw on skribbl.</br>
- Move your mouse on top of the white color block's center and click on enter so that it records where the color palette is present in your screen. You can set the values of ```whitePosX``` and ```whitePosY``` (<em>Line 10</em> in the py file) so that you can quickly proceed with the program rather than moving the cursor to white block every time. </br>
- Move your mouse to the top left corner of canvas so that it will be used as a start point to draw the image. </br>
- Input the word assigned to you. </br>
- Wait and let Skribbot do its magic


### Note
- The program automatically deletes the images downloaded after drawing them. You can disable it by removing the last line in the py file i.e. <em>Line 120</em>.
- This program doesn't intend to use copyrighted materials/images via downloading the images from google, but rather is intended to be educational and a medium for users to have fun in playing skribbl and using python.
