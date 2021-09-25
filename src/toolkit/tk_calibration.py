import json
import toolkit as tk


def json_to_dict(screen):
    """
    Opens a json file and returns it's contents as a dict
    """
    with open(screen + '.json') as f:
        data = json.load(f)
        return data


def dict_to_json(dictionary, screen):
    """
    Saves a dict to a json file
    """
    with open(screen + '.json', 'w') as f:
        json.dump(dictionary, f, indent=4)


def calibrate(screen, locations, trigger):
    """
    Calibrate locations on screen
    """
    data = json_to_dict(screen)
    for location in locations:
        print("Hover with the mouse over {0} and press {1}".format(
            location, trigger))
        data[location] = tk.mouse_pos(trigger)

    dict_to_json(data, screen)
    print("Json file updated")
    print('')


def calibrate_grid(screen, locations, trigger):
    """
    Takes in a row of positions, adds the entire list to the json file
    """

    print("Hover with the mouse over {0} and press {1}".format(
        locations[0], trigger))
    begin = tk.mouse_pos(trigger)
    print("Hover with the mouse over {0} and press {1}".format(
        locations[-1], trigger))
    end = tk.mouse_pos(trigger)

    result = []
    x_unit = (end[0] - begin[0]) / (len(locations) - 1)
    y_unit = (end[1] - begin[1]) / (len(locations) - 1)

    if abs(x_unit) > abs(y_unit):  # horizontaal
        for i in range(len(locations)):
            x = begin[0] + i * x_unit
            y = begin[1]
            result.append((int(x), y))
    else:  # verticaal
        for i in range(len(locations)):
            y = begin[1] + i * y_unit
            x = begin[0]
            result.append((x, int(y)))

    data = json_to_dict(screen)
    print(data)
    for i in range(len(locations)):
        data[locations[i]] = result[i]
        i += 1

    dict_to_json(data, screen)
    return result
