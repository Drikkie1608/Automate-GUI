import pyautogui
import keyboard
import time

import toolkit as tk
import terraria as te

def mining():
    """
    Small program: keep throwing tnt at mouse position
    """
    keyboard.wait('v')
    while True:
        time.sleep(0.5)
        tk.click()

def idle():
    """
    Small program: Keep screen awake by switching between 2 positions
    """
    pos1 = tk.mouse_pos('p')
    pos2 = tk.mouse_pos('p')

    while True:
        time.sleep(20)
        pyautogui.moveTo(*pos1)
        tk.sleep(20)
        pyautogui.moveTo(*pos2)

def fishing():
    power = int(input("Fishing power: "))
    time.sleep(5)
    while True:
        te.autofish(power)