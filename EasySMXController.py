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
                match event.code:
                    case Code.a:
                        self.a = event.value
                    case Code.b:
                        self.b = event.value
                    case Code.x:
                        self.x = event.value
                    case Code.y:
                        self.y = event.value
                    case Code.start:
                        self.start = event.value
                    case Code.back:
                        self.back = event.value
                    case Code.rb:
                        self.rb = event.value
                    case Code.rt:
                        self.rt = event.value
                    case Code.lb:
                        self.lb = event.value
                    case Code.lt:
                        self.lt = event.value
            if(event.type == 3):
                match event.code:
                    case Code.rightJoyX:
                        self.rightJoyX = event.value
                    case Code.rightJoyY:
                        self.rightJoyY = event.value
                    case Code.leftJoyX:
                        self.leftJoyX = event.value
                    case Code.leftJoyY:
                        self.leftJoyY = event.value
                    
                    case Code.Xdpad:
                        if(event.value == 1):
                            self.right = 1
                        elif(event.value == -1):
                            self.left = 1
                        else:
                            self.right = 0
                            self.left = 0
                    case Code.Ydpad:
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
    
