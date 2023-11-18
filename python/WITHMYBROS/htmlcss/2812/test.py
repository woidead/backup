import pyautogui
import os
import time 
import random
pyautogui.FAILSAFE = True

print('ctrl + c')
try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        print(position_str)
        print('\b' * len(position_str), end='', flush=True)

except:
    os.system('clear')
    print('Finish')