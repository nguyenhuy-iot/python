import pyautogui
import time
import keyboard

print("-------**********---------")
print("Hiển thị tọa độ hiện tại của chuột:\n")
print("Point(x, y)(R, G, B)\n")
input("Continue:[Enter] ; Exit:[Esc]")
while keyboard.is_pressed('esc') == False:
    Mouse_XY = pyautogui.position()
    print(Mouse_XY,end='')
    pixel_RGB = pyautogui.pixel(Mouse_XY[0],Mouse_XY[1])
    print(pixel_RGB)
    time.sleep(0.1)