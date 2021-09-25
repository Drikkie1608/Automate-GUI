import pyautogui
import keyboard

import toolkit as tk

def dayskip(c):
    """
    Skip one day
    """
    tk.knopke('esc')
    tk.click(*c["power_menu"])
    reset_power_menu(c)
    tk.click(*c["time_menu"])
    tk.click(*c["dusk"])
    tk.click(*c["dawn"])
    tk.click(*c["day"])
    tk.knopke('esc')


def get_dup_item(c, item):
    """
    Puts item from duplication menu in inventory
    """
    tk.knopke('esc')

    reset_power_menu(c)
    tk.click(*c["dup_menu"])

    reset_dup_menu(c)
    tk.click(*c["dup_search"])
    keyboard.write(item)
    keyboard.press('shift')
    tk.click(*c["dup_first_item"])
    keyboard.release('shift')
    tk.click(*c["dup_x"])
    tk.knopke('esc')


def research(c, slot_x, slot_y):
    """
    Research item at coördinate
    """

    tk.knopke('esc')
    tk.knopke('esc')

    tk.click(*c["power_menu"])
    tk.click(*c["dup_menu"])
    tk.click(*c["research_menu"])
    pyautogui.moveTo(slot_x, slot_y, *c["research_window"])
    tk.click(*c["research_button"])

    tk.knopke('esc')
    tk.knopke('esc')

    pyautogui.moveTo(slot_x, slot_y)


def reset_dup_menu(c):
    tk.click(*c["dup_weapons"])
    tk.click(*c["dup_armor"])
    tk.click(*c["dup_armor"])
    tk.click(*c["dup_x"])


def reset_power_menu(c):
    tk.click(*c["dup_menu"])
    tk.click(*c["research_menu"])
    tk.click(*c["research_menu"])


def calibrate_journey(screen, trigger):
    # Power menu
    tk.calibrate(screen, ["power_menu"], trigger)

    # Duplication menu
    tk.calibrate_grid(screen, ["dup_menu", "research_menu", "time_menu", "weather_menu", "pp_menu", "infection_toggle",
                            "enemy_difficulty_slider"], trigger)
    tk.calibrate_grid(screen, ["dup_weapons", "dup_armor", "dup_vanity", "dup_blocks", "dup_furniture", "dup_accesories",
                            "dup_equipment", "dup_consumables", "dup_tools", "dup_materials", "dup_misc"], trigger)
    tk.calibrate(screen, ["dup_x", "dup_search", "dup_first_item"], trigger)

    # Research menu
    tk.calibrate(screen, ["research_window", "research_button"], trigger)

    # Time menu
    tk.calibrate_grid(screen, ["time_freeze", "dawn", "noon", "dusk", "midnight", "speed_slider"], trigger)


if __name__ == "main":
    while True:
        screen = input("Screen 1 or 2: ")
        if screen == "1":
            c = 'c_main_monitor'
        else:
            c = 'c_second_monitor'

        keyboard.wait('v')
        research(c, *pyautogui.position())
