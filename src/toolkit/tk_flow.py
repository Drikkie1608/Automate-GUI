import threading
import keyboard

FLOW = list()
TIMED = list()
RUNNING = False


def seperate_thread(function):
    x = threading.Thread(target=function, daemon=True)
    x.start()


def flow():
    """
    Seperate thread, works one by one through the list FLOW
    """
    while True:
        if RUNNING:
            FLOW[0]()
            FLOW.pop()


def atf(function, seconds=None):
    """
    Adds a function to the flow, function must be lambda, can also be on a timer
    """
    FLOW.append(function)
    if RUNNING & type(seconds) == 'int':
        t = threading.Timer(seconds, lambda: atf(function, seconds))
        t.daemon = True
        t.start()
        TIMED.append(t)


def toggle(key):
    """
    Seperate thread, keeps track of RUNNING or not RUNNING with a toggle key
    """
    while True:
        keyboard.wait(key)
        RUNNING = not RUNNING
