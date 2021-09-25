import pyautogui
import keyboard

import toolkit as tk


def mouse_pos(trigger=None):
    """
    Returns mouse position after trigger or instantly if no trigger
    """
    if not trigger:
        return pyautogui.position()
    keyboard.wait(trigger)
    x, y = pyautogui.position()
    return x, y


def activate_screen(screen):
    """
    Only if 2 monitors, calibration?
    """
    pass


def manual_overwrite(possibilities):
    """
    Input window that returns a command via the command line, activate screen at the end?
    """
    command = input("Manual overwrite: ")
    if command in possibilities:
        return command

    print("Wrong command, try again")
    print("")
    return manual_overwrite(possibilities)



