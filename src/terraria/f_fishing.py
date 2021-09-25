import time

import terraria as te
import toolkit as tk

def calculate_time(power):
    """
    Calculate avarage fishing time based on fishing power
    """
    return 11 / (2.5 + ((23 / 600) * power))


def autofish(power):
    """
    Automatic fisher based on fishing power
    """
    tk.click()
    # sleep(calculate_time(power))
    time.sleep(4)
    tk.click()
    time.sleep(1)


def specific_fishing(c, item):
    """
    Fishes untill it sees the correct item, not done
    """
    biome = fishing_biome(item)
    te.visit(c, biome)


def fishing_biome(item):
    return "biome"


def dup_routine(c):
    speak_to_npc(c)
    angler_quest_button(c)

    #fish = detect_idle()
    fish = None
    if fish is None:
        fish = input("fish not detected: " )
        time.sleep(4)
        #activate_screen()

    tk.knopke('esc')
    te.get_dup_item(c, fish)
    speak_to_npc(c)
    tk.click(*c["fisher_quest"])  # return fish

    te.dayskip(c)


def speak_to_npc(c):
    """
    Speak to an npc in a prison
    """
    # npc_middle = [n / 2 for n in [x1 + x2 for x1, x2 in zip(c["npc_left"], c["npc_right"])]]
    tk.rightclick(*c["npc_left"])
    tk.rightclick(*c["npc_middle"])
    tk.rightclick(*c["npc_right"])

def angler_quest_button(c):
    n = 100
    unit = (c["angler_quest_top"][1] - c["angler_quest_bottom"][1]) / n - 1
    for i in range(n):
        tk.click(c["angler_quest_bottom"][0], c["angler_quest_bottom"][1] + i * unit)

def calibrate_fishing(screen, trigger):
    tk.calibrate_grid(screen, ["npc_left", "npc_middle", "npc_right"], trigger)
    tk.calibrate_grid(screen, ["angler_quest_top", "angler_quest_bottom"], trigger)


if __name__ == "__main__":
    screen = "screen2"
    #calibrate_fishing(screen, 'p')

    time.sleep(6)

    c = tk.json_to_dict(screen)
    dup_routine(c)

