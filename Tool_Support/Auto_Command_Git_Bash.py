import pyautogui
import time
import keyboard

def wait_key():
    delay=0.5
    while keyboard.is_pressed('enter') == False: pass
    time.sleep(delay)
def send_command(cmd):
    print(cmd)
    
print("-------**********---------")
print("cập nhật thư mục lên git hub")
print("Continue:[Enter]")
wait_key()

print("git add .")
pyautogui.write("git add .")
wait_key()

current_time = time.strftime("\"%d/%m/%Y, %H:%M:%S\"")
print("git commit -m ",current_time)
pyautogui.write("git commit -m ")
pyautogui.write(current_time)
wait_key()

print("git push origin master")
pyautogui.write("git push origin master")
wait_key()
print("Exit")
time.sleep(5)

'''
git add .
git commit -m "command"
git push origin master
'''