# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:01:50 2021

@author: trekk
"""

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import Analyzer as az
import FileHandler as fh
import linearFunction as ln
import Plotter as pl


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Titration-Analyzer")
        self.root.geometry="800x600"
        self.vSample = 0.0
        self.cTiter = 0.0
        self.cSample = tk.StringVar()
        self.cSample.set("Not Calculated")
        self.fileUrl = tk.StringVar()
        self.fileUrl.set("")
        self.csvData = np.array([[],[]])
        
        tk.Label(self.root, textvariable=self.fileUrl).grid(row=0, column=0)
        self.selectFileButton = tk.Button(self.root, text = "selectFile", command = self.selectFile)
        self.selectFileButton.grid(row=0, column = 1)
        
        tk.Label(self.root, text = "Sample Volume (ml):").grid(row = 1, column = 0)
        self.vSampleEntry = tk.Entry(self.root, width = 10)
        self.vSampleEntry.grid(row = 1, column = 1)
        
        tk.Label(self.root, text = "Titer Concentration (mol/l):").grid(row = 2, column = 0)
        self.cTiterEntry = tk.Entry(self.root, width = 10)
        self.cTiterEntry.grid(row = 2, column = 1)
        
        self.calculateButton = tk.Button(self.root, text = "Calculate", command = self.update)
        self.calculateButton.grid(row = 3, column = 1, columnspan=2)
        
        tk.Label(self.root, text = "Sample Concentration (mol/l):").grid(row = 4, column = 0)
        tk.Label(self.root, textvariable=self.cSample).grid(row = 4, column = 1)
        
        
        
        self.addEmptyPlot()
        pass
        
        
    def selectFile(self):
        self.fileUrl.set(tk.filedialog.askopenfilename(initialdir = "Desktop", title = "Select Data", filetypes = [("CSV Files", "*.csv")] ))
        return None
    
    def update(self):
        self.vSample = float(self.vSampleEntry.get())
        self.cTiter = float(self.cTiterEntry.get())
        if(((self.fileUrl.get() != "") and (self.vSample != 0)) and (self.cTiter != 0)):
            self.csvData = fh.loadFilesFromCsv(self.fileUrl.get())
            self.calculate()
        return None
    
    def calculate(self):
        linearFunction = ln.getLinearFunctionBetweenPointsOfHighestSlope(self.csvData[0],self.csvData[1])
        equivalencePoint = az.calculateEquivalencePoint((self.csvData[0])[linearFunction[3]], (self.csvData[0])[linearFunction[3]+1], linearFunction[0], linearFunction[2])                                                                                                
        figure = pl.plotAllData(self.csvData[0],self.csvData[1], linearFunction[0], linearFunction[2], linearFunction[4], linearFunction[1], equivalencePoint[0], equivalencePoint[1])
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row = 5, column = 0, columnspan=2)
        self.cSample.set(az.calculateConcentration(self.cTiter, equivalencePoint[0], self.vSample))
        return None
        
    
    def addEmptyPlot(self):
        figure = plt.Figure(figsize=(5,4), dpi=100)
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row = 5, column = 0, columnspan=2)
        plt.grid()
        return None