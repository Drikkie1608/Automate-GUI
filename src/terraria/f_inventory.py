
def slot_locator(c, slot):
    """
    Takes in an inventory slot (e.g. "a1") and returns it's coördinates
    """
    row = ord(slot[0]) - 96
    column = slot[1]
    if column == 0: column = 10

    x_unit = ( c["e0_slot"][0] - c["a1_slot"][0] ) / 9
    y_unit = ( c["e0_slot"][1] - c["a1_slot"][1] ) / 4

    x = c["a1_slot"][0] + (column-1) * x_unit
    y = c["a1_slot"][1] + (row - 1) * y_unit

    return x, y