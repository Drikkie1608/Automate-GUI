from time import *

import keyboard
import pyautogui


def knopke(button):
    """
    Press a button on your keyboard with a slight delay
    """
    keyboard.press(button)
    sleep(0.12)
    keyboard.release(button)
    sleep(0.12)


def click(x=None, y=None):
    """
    Click the left mouse button on your keyboard with a slight delay
    """
    pyautogui.mouseDown(x, y)
    pyautogui.mouseUp(x, y)


def rightclick(x=None, y=None):
    """
    Click the right mouse button on your keyboard with a slight delay
    """
    pyautogui.mouseDown(x, y, button='right')
    pyautogui.mouseUp(x, y, button='right')


def moveItem(x, y, newx, newy):
    """
    Move an item from one location to another
    """
    pyautogui.mouseDown(x, y)
    pyautogui.moveTo(newx, newy)
    pyautogui.mouseUp(newx, newy)
