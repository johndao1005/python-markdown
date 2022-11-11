import tkinter as tk
from tkinter import ttk
from src.constant import app_name, icon
from display.menu_bar.menu import add_menubar

class Editor(tk.Tk):
    """Start an instance of login screen which allow user to sign up with top level window or login directly
        When users login, the class would open to menu which is another class which handle the data view, update, delete while
        destroy the current login to prevent multiple login.
        """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title(app_name)
        # self.iconbitmap(setup.icon)
        self.resizable(0, 0)
        self.geometry('1000x600')
        self.option_add('*Font', 'Calibri 15') 
        add_menubar(self)