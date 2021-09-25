from tk_essentials import *


def detect_idle(image, confidence):
    """
    Runs once, returns middle of image or returns None
    """
    result = pyautogui.locateOnScreen(image, confidence=confidence)
    if result:
        left, top, width, height = result
        x = left + width / 2
        y = top + height / 2
        print("Found %s at x = %s, y =  %s" % image % x % y)
        return x, y
    else:
        return None


def detect_overwrite(image, confidence, trigger):
    """
    If image is not detected, switch to manual calibration
    """
    detection = detect_idle(image, confidence)
    if detection is None:
        print("Switching to manual detection, put the mouse above %s and press %s" % image % trigger)
        return mouse_pos(trigger)
