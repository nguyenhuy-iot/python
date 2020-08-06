'''
Auto Click
lưu tọa độ chuột
click vị trí đã lưu

'''
import array
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 1
button = Button.left
start_stop_key = KeyCode(char='9')
exit_key = KeyCode(char='0')
#chuc nang
save_key = KeyCode(char='1')
click_key = KeyCode(char='2')
#######
class AutoClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(AutoClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True 

    def start_running(self):
        print("start_running")
        self.running = True

    def stop_running(self):
        print("stop_running")
        self.running = False
    def exit(self):
        print("exit")
        self.running = False
        self.program_running = False
        pass
    def run(self):
        global Posi_list
        print("program_running...")
        while self.program_running:
            #print("run...")
            while self.running:
                print("............Auto click Running...........",delay) 
                for index in Posi_list:
                    mouse.position = (index)
                    mouse.click(AutoClick.button)
                    time.sleep(self.delay)
                    pass                            
                pass
            time.sleep(0.01)
            pass

mouse = Controller()
#AutoClick = AutoClickMouse(delay, button)
#AutoClick.start()

#trinh xu ly keyboard
def on_press(key):
      
    if key == start_stop_key:
        if AutoClick.running:
            AutoClick.stop_running()
            pass
        else:
            AutoClick.start_running()
            pass
        
        pass
    elif key == exit_key:
        AutoClick.exit()
        listener.stop()
        pass
    elif key == save_key:
        global Posi_list        
        print("mouse.position: ", len(Posi_list), mouse.position)
        Posi_list = Posi_list + [mouse.position]
        

        pass
    elif key == click_key:
        global count
        print("click ", count, Posi_list[count])
        mouse.position = (Posi_list[count])
        mouse.click(AutoClick.button)
        count +=1
        if count >= len(Posi_list):
            count =0
            pass        
        pass
    
#----------main-----------
Posi_list = []
count = 0

print("hướng dẫn sử dụng")
print("1.lưu tọa độ click")
print("2.click")
print("9.Auto Click")
print("0.thoat")
print("-----------------------")


try:
    delay = float(input("set delay để tiếp tục, delay="))
except ValueError:
    print("delay = 1")
print("delay=",delay)
input("are you redy!")
AutoClick = AutoClickMouse(delay, button)
AutoClick.start()
#kich hoat kiem tra keyboard
with Listener(on_press=on_press) as listener: 
    listener.join()
pass 
input("")   
      
       		

    



