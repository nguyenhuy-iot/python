from PIL import ImageGrab,ImageOps
from numpy import *
import cv2
import pyautogui
import time


class target:
    def __init__(self,Point):
        self.Point = None


    while True:
        #input("chụp lấy tọa độ chuột")
        MouseXY=pyautogui.position()
        #print(MouseXY)
        Box=(MouseXY[0],MouseXY[1],MouseXY[0]+1,MouseXY[1]+1)
        #print("Box: ",Box)
        img_target=ImageGrab.grab(Box)
        #img_target.save("target.png")
        #print("grayscale")
        grayImage = ImageOps.grayscale(img_target)
        a= array(grayImage.getcolors())
        print(a.sum())
        time.sleep(0.1)
        #pyautogui.moveTo(XY_target)
        pass







