import pyautogui
import time

print("-------**********---------")
print("Hiển thị tọa độ hiện tại của chuột.")
input("[Enter]")
while True:
    Mouse_XY = pyautogui.position()
    print(Mouse_XY)
    time.sleep(0.1)