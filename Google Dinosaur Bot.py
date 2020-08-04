from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *
class Cordinates():
    replayBtn = (340,390)
    dinasaur = (147,375)
def restartGame():
    pyautogui.click(Cordinates.replayBtn)
def pressSapce():
    pyautogui.keyDown('space')  
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
def imageGrab():
    box = (Cordinates.dinasaur[0]+50,Cordinates.dinasaur[1],Cordinates.dinasaur[0]+80,Cordinates.dinasaur[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a= array(grayImage.getcolors())
    print(a.sum())
    return a.sum()
def main():
    restartGame()
    while True:
        if(imageGrab() != 1147):
            pressSapce()
            time.sleep(0.1)

main()


