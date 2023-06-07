from evdev import InputDevice, categorize, ecodes
import threading

class Code():
    # Type 3
    Xdpad = 16
    Ydpad = 17

    rightJoyX = 2
    rightJoyY = 5
    leftJoyX = 0
    leftJoyY = 1

    # Type 1
    a = 306
    b = 305
    x = 307
    y = 304

    start = 313
    back = 312

    rb = 309
    rt = 311
    lb = 308
    lt = 310

class Controller():
    def __init__(self, port):
        self.gamepad = InputDevice(port)
        
        self.rightJoyX = 128
        self.rightJoyY = 128
        self.leftJoyX = 128
        self.leftJoyY = 128
        
        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0
        
        
        self.a = 0
        self.b = 0
        self.x = 0
        self.y = 0

        self.start = 0
        self.back = 0

        self.rb = 0
        self.rt = 0
        self.lb = 0
        self.lt = 0
        
        a = threading.Thread(target = self.gamepadLoop, args = ())
        a.start()
        
    def gamepadLoop(self):
        for event in self.gamepad.async_read_loop():
            if(event.type == 1):
                if(event.code == Code.a):
                        self.a = event.value
                if(event.code == Code.b):
                        self.b = event.value
                if(event.code == Code.x):
                        self.x = event.value
                if(event.code == Code.y):
                        self.y = event.value
                if(event.code == Code.start):
                        self.start = event.value
                if(event.code == Code.back):
                        self.back = event.value
                if(event.code == Code.rb):
                        self.rb = event.value
                if(event.code == Code.rt):
                        self.rt = event.value
                if(event.code == Code.lb):
                        self.lb = event.value
                if(event.code == Code.lt):
                        self.lt = event.value
            if(event.type == 3):
                if(event.code == Code.rightJoyX):
                        self.rightJoyX = event.value
                if(event.code == Code.rightJoyY):
                        self.rightJoyY = event.value
                if(event.code == Code.leftJoyX):
                        self.leftJoyX = event.value
                if(event.code == Code.leftJoyY):
                        self.leftJoyY = event.value
                    
                if(event.code == Code.Xdpad):
                        if(event.value == 1):
                            self.right = 1
                        elif(event.value == -1):
                            self.left = 1
                        else:
                            self.right = 0
                            self.left = 0
                if(event.code == Code.Ydpad):
                        if(event.value == -1):
                            self.up = 1
                        elif(event.value == 1):
                            self.down = 1
                        else:
                            self.down = 0
                            self.up = 0


if(__name__ == "__main__"):
    
    import time
    c = Controller('/dev/input/event0')
    while(1):
        print(c.lt, c.rt, c.lb, c.rb)
        print(c.back, c.start)
        print(c.a, c.b, c.x, c.y)
        print(c.rightJoyX, c.rightJoyY, c.leftJoyX, c.leftJoyY)
        print(c.right, c.left, c.up, c.down)
        
        print()
        time.sleep(0.2)
    
