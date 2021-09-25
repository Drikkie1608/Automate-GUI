"""
The program consists of 3 seperate threads:
- While True: execute flow
- While True: toggle global RUNNING on/off
- Main: interface to add to flow
"""
import toolkit as tk

if __name__ == "__main__":
    tk.seperate_thread(tk.flow)
    tk.seperate_thread(lambda: tk.toggle('v'))
    # RUNNING = False
