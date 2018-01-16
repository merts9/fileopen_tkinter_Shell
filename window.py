__author__ = "Uni-Nummer: 6593731: Ekaterina Merts, 6621331: Lucas Laub"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__credits__ = "No thanks"
__email__ = "merts.ekaterina@gmail.com, l.g.laub@gmx.de"

import tkinter as tk
from tkinter import filedialog


class selection_window(tk.Tk):
    """A tkinter class only for using the tkinter Filedialog and providing the user an
    environment she/he is used to, the 'real' tkinter window is hidden """
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        self.__file_container = filedialog.askopenfilename(initialdir="/", title="Select file")

    def getter(self):
        """A simple getter method as the name implies"""
        return self.__file_container


def file_tkinter_selection():
    """This functions creates a 'selection_window' class and calls the 'getter' method
        to get the path the user selected and retiurns ist to the main body"""
    win = selection_window()
    file_pathe = win.getter()
    win.update()
    return file_pathe


