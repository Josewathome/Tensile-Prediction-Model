# The following few lines of code will initialize Our model and perform the prediction

import tkinter as tk
from tkinter import ttk
from GUI_classes import DataCollection 
from model import TensileStrength

root = tk.Tk()
root.geometry("500x500")  # Width x Height
my_gui = DataCollection(root)
root.mainloop()
