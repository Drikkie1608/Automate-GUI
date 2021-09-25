import pyautogui

from tk_calibration import *
from tk_essentials import *

def dayskip(c):
    """
    Skip one day
    """
    knopke('esc')
    click(*c["power_menu"])
    reset_power_menu(c)
    click(*c["time_menu"])
    click(*c["dusk"])
    click(*c["dawn"])
    click(*c["day"])
    knopke('esc')


def get_dup_item(c, item):
    """
    Puts item from duplication menu in inventory
    """
    knopke('esc')

    reset_power_menu(c)
    click(*c["dup_menu"])

    reset_dup_menu(c)
    click(*c["dup_search"])
    keyboard.write(item)
    keyboard.press('shift')
    click(*c["dup_first_item"])
    keyboard.release('shift')
    click(*c["dup_x"])
    knopke('esc')


def research(c, slot_x, slot_y):
    """
    Research item at coördinate
    """

    knopke('esc')
    knopke('esc')

    click(*c["power_menu"])
    click(*c["dup_menu"])
    click(*c["research_menu"])
    pyautogui.moveTo(slot_x, slot_y, *c["research_window"])
    click(*c["research_button"])

    knopke('esc')
    knopke('esc')

    pyautogui.moveTo(slot_x, slot_y)


def reset_dup_menu(c):
    click(*c["dup_weapons"])
    click(*c["dup_armor"])
    click(*c["dup_armor"])
    click(*c["dup_x"])


def reset_power_menu(c):
    click(*c["dup_menu"])
    click(*c["research_menu"])
    click(*c["research_menu"])


def calibrate_journey(screen, trigger):
    # Power menu
    calibrate(screen, ["power_menu"], trigger)

    # Duplication menu
    calibrate_grid(screen, ["dup_menu", "research_menu", "time_menu", "weather_menu", "pp_menu", "infection_toggle",
                            "enemy_difficulty_slider"], trigger)
    calibrate_grid(screen, ["dup_weapons", "dup_armor", "dup_vanity", "dup_blocks", "dup_furniture", "dup_accesories",
                            "dup_equipment", "dup_consumables", "dup_tools", "dup_materials", "dup_misc"], trigger)
    calibrate(screen, ["dup_x", "dup_search", "dup_first_item"], trigger)

    # Research menu
    calibrate(screen, ["research_window", "research_button"], trigger)

    # Time menu
    calibrate_grid(screen, ["time_freeze", "dawn", "noon", "dusk", "midnight", "speed_slider"], trigger)


if __name__ == "main":
    while True:
        screen = input("Screen 1 or 2: ")
        if screen == "1":
            c = c_main_monitor
        else:
            c = c_second_monitor

        keyboard.wait('v')
        research(c, *pyautogui.position())
