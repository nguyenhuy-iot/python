from pynput.keyboard import KeyCode
from pynput import keyboard
from PIL import ImageGrab,ImageOps
from numpy import *
import cv2
import pyautogui
import threading
import time


Click_One = False
start_stop_key = KeyCode(char='9')
exit_key = KeyCode(char='0')
Running = False
Program_Running = True 

class Monitoring_pixel(threading.Thread):
    def __init__(self,name,point):
        super(Monitoring_pixel, self).__init__()
        self.name = name
        self.point = point        
        self.mold = self.img_sum()
        print("Monitoring_pixel",self.point) 
        print(self.mold) 

    def img_sum(self):
        Box=(self.point[0],self.point[1],self.point[0]+1,self.point[1]+1) 
        img_Box=ImageGrab.grab(Box)
        grayImage = ImageOps.grayscale(img_Box)
        img_array= array(grayImage.getcolors())
        return img_array.sum()

    def run(self):
        global Click_One
        global Running
        global Program_Running
        print("Running...",self.point)
        while Program_Running: 
            time.sleep(0.4)            
            while Running:
                #print(self.name,self.img_sum())
                if self.img_sum()< self.mold:
                
                    if Click_One:
                        pass
                    else:
                        Click_One = True                    
                        pyautogui.click(self.point)
                        print("click",self.name)
                        time.sleep(0.01)
                        Click_One = False
                        pass
                    
                   
                                                 


#trinh xu ly keyboard
def on_press(key):
    global Running
    global Program_Running
    if key == start_stop_key:
        if Running:
            Running = False 
            print("Stop")          
        else:
            Running = True 
            print("start")              
    elif key == exit_key:
        Running  =False
        Program_Running = False  
        print("Exit")      
        listener.stop()        
#kich hoat kiem tra keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

#-----------main-------------

print("hướng dẫn sử dụng")
print("9.Auto Click")
print("0.thoat")
print("-----------------------")

input("toa do 1: [enter]")
Point_1 = pyautogui.position()
print(pyautogui.position())
Pixel_1 = Monitoring_pixel("Pixel_1",Point_1)
#+++++++++++++++++
input("toa do 2: [enter]")
Point_2 = pyautogui.position()
print(pyautogui.position())
Pixel_2 = Monitoring_pixel("Pixel_2",Point_2)
#+++++++++++++++++
input("toa do 3: [enter]")
Point_3 = pyautogui.position()
print(pyautogui.position())
Pixel_3 = Monitoring_pixel("Pixel_3",Point_3)
#+++++++++++++++++
input("toa do 4: [enter]")
Point_4 = pyautogui.position()
print(pyautogui.position())
Pixel_4 = Monitoring_pixel("Pixel_4",Point_4)
#____________________
input("are you redy!")
Pixel_1.start()
Pixel_2.start()
Pixel_3.start()
Pixel_4.start()




