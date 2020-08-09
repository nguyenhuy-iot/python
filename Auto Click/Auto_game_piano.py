import pyautogui
import keyboard
import time
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

Points=[]
print("-------*******------")
print("Auto game piano click")
input("Continue [Enter]")
print("chọn vị trí click")
for i in range(4):
    print("chọn vị trí(%d): "%(i+1),end='')
    keyboard.wait('enter')
    Points  += [pyautogui.position()]
    print(Points[i])
print("Are you ready!")
keyboard.wait('enter')
print("START...")
running = True
while keyboard.is_pressed('esc') == False:    
    if running :
        for i in range(4):
            X,Y=Points[i]
            #RGB(24,20,70)
            if pyautogui.pixel(X,Y)[2] < 80:
                click(X,Y)
                #print("click ",i)
        
    if keyboard.is_pressed('0'):          
        running = not(running)
        print(running)
        time.sleep(0.1)
    pass
