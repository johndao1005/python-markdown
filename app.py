"""Data Explore Application
The program helps presenting as well as reading data regard the tagging of white shark
With the application user can view data in graph with matplotlib while enjoy the GUI navigation of Tkinter

"""
import ctypes
from display import Editor

def start():
    app = Editor()
    app.mainloop()
    ctypes.windll.shcore.SetProcessDpiAwareness(True)


if __name__ == '__main__':
    """
    Initiate the app
    """
    start()
