"""
The program consists of 3 seperate threads:
- While True: execute flow
- While True: toggle global RUNNING on/off
- Main: interface to add to flow
"""
from tk_essentials import seperate_thread
from t
if __name__ == "__main__":
    seperate_thread(flow)
    seperate_thread(lambda: toggle('v'))
    # RUNNING = False
