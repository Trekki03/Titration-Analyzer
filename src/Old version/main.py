# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:23:37 2021

@author: trekk
"""


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import ui



root = tk.Tk()
gui = ui.Window(root)
root.mainloop()