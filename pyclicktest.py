# Code to check if left or right mouse buttons were pressed
import win32api
import time
import pynput

mouse = pynput.mouse.Controller()
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            print('Left Button Pressed')
            pos = mouse.position
            print('Mouse position: ', pos)
        else:
            print('Left Button Released')
            pos = mouse.position
            print('Mouse position: ', pos)

    if b != state_right:  # Button state changed
        state_right = b
        print(b)
        if b < 0:
            print('Right Button Pressed')
        else:
            print('Right Button Released')
    time.sleep(0.001)