
from Tkinter import *
import ttk


def TensileFunction():
    class GuiApplicaion:
        def __init__(self):
            self.master = Tk()
            self.notebook = ttk.Notebook(self.master)

            self.tab2D = ttk.Frame(self.notebook)
            self.tab3D = ttk.Frame(self.notebook)
            self.notebook.add(self.tab2D, text="2D model")
            self.notebook.add(self.tab3D, text="3D model")

            self.notebook.pack()
