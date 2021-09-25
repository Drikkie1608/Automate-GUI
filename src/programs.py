import keyboard

from tk_steam import *
from tk_toggle import *
from tk_essentials import *
from f_autofish import autofish

def mining():
    """
    Small program: keep throwing tnt at mouse position
    """
    keyboard.wait('v')
    while True:
        sleep(0.5)
        click()

def idle():
    """
    Small program: Keep screen awake by switching between 2 positions
    """
    pos1 = mouse_pos('p')
    pos2 = mouse_pos('p')

    while True:
        sleep(20)
        pyautogui.moveTo(*pos1)
        sleep(20)
        pyautogui.moveTo(*pos2)

def fishing():
    power = int(input("Fishing power: "))
    sleep(5)
    while True:
        autofish(power)