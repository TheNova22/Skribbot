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
- Make sure to set ```whitePosX``` and ```whitePosY``` as the constraints of the white color box in skribbl as the position of it might vary with display screen size. (<em>Line 7</em> in the py file)

## Running
Call the python program from terminal and let the program draw on skribbl's canvas.

### Note
- The program automatically deletes the images downloaded after drawing them. You can disable it by removing the last line in the py file i.e. <em>Line 91</em>.
- This program doesn't intend to use copyrighted materials/images via downloading the images from google, but rather is intended to be educational and a medium for users to have fun in playing skribbl and using python.
