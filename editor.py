# Imports
from tkinter import *
import ctypes
import re
from functions.changes import changes
from functions.markdown import search_re

# Setup
root = Tk()
root.title('Markdown Editor')
root.geometry('1000x600')

# Setting the Font globaly
root.option_add('*Font', 'Calibri 15')


# Starting the Application
changes()
root.mainloop()

# Increas Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)
