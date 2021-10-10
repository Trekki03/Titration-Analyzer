# -*- coding: utf-8 -*-
"""
First created on 10/10/2021
@author: github.com/Trekki03
"""

import tkinter as tk
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import plotter
import analyzer
import fileHandler
import linearFunction

class Window:
    """ class containing all functions for the ui
    """
    def __init__(self, root):
        """constructor

        Args:
            root (return of tk.Tk()): root object of the window
        """
        self.root = root
        
        #Init Windows
        self.root.title("Titration-Analyzer")
        self.root.resizable(False, False)
        
        #Add Vars
        self.vSample                = 0.0
        self.cTiter                 = 0.0
        self.cSample                = tk.StringVar()
        self.fileUrl                = tk.StringVar()
        self.csvData                = ([], [])
        
        self.fileUrlLable           = None
        self.sampleVIdentifierLable = None
        self.titerCIdentifierLable  = None
        self.sampleCIdentifierLable = None
        self.sampleCLable           = None
        self.selectFileButton       = None
        self.calculateButton        = None
        self.sampleVEntry           = None
        self.titerCEntry            = None
        self.chart                  = None

            
        #Init Vars
        self.cSample.set("not calculated yet")
        self.fileUrl.set("no file selected")
       

        #create UI elements
        self.fileUrlLable           = tk.Label(self.root, textvariable=self.fileUrl)
        self.sampleVIdentifierLable = tk.Label(self.root, text = "Sample Volume (ml):")
        self.titerCIdentifierLable  = tk.Label(self.root, text = "Titer Concentration (mol/l):")
        self.sampleCIdentifierLable = tk.Label(self.root, text = "Titer Concentration (mol/l):")
        self.sampleCLable           = tk.Label(self.root, textvariable=self.cSample)
        
        self.selectFileButton       = tk.Button(self.root, text = "selectFile", command = self.selectFile)
        self.calculateButton        = tk.Button(self.root, text = "Calculate", command = self.calculate)
        
        self.sampleVEntry           = tk.Entry(self.root, width = 10)
        self.titerCEntry            = tk.Entry(self.root, width = 10)
        
        self.createUiElementFromFigure(plotter.createEmptyFigure())
        
        
        #position UI elements
        self.fileUrlLable               .grid(row=0, column = 0)
        self.selectFileButton           .grid(row=0, column = 1)
        
        self.sampleVIdentifierLable     .grid(row = 1, column = 0)
        self.sampleVEntry               .grid(row = 1, column = 1)
        
        self.titerCIdentifierLable      .grid(row = 2, column = 0)
        self.titerCEntry                .grid(row = 2, column = 1)
        
        self.calculateButton            .grid(row = 3, column = 1)
        
        self.sampleCIdentifierLable     .grid(row = 4, column = 0)
        self.sampleCLable               .grid(row = 4, column = 1)
        #chart in createUiElementFromFigure Function
        pass
    
    def createUiElementFromFigure(self, figure: plt.figure):
        """turn an matplotlib figure into an ui element and saves it in self.chart

        Args:
            figure (plt.figure): matplotlib figure
        """
        self.chart = FigureCanvasTkAgg(figure, self.root)
        self.chart.get_tk_widget().grid(row = 5, column = 0, columnspan=2)
        return None
    
    def calculate(self):
        self.vSample = float(self.sampleVEntry.get())
        self.cTiter = float(self.titerCEntry.get())
        if ((self.fileUrl.get != "no file selected") and (self.vSample != 0.0)) and (self.cTiter != 0.0):
            pointsOfHighestSlope = analyzer.getPointsOfHighestSlope(self.csvData[0], self.csvData[1])
            linFunction = linearFunction.getFunctionBetweenToPoints(pointsOfHighestSlope[0],pointsOfHighestSlope[1], pointsOfHighestSlope[2], pointsOfHighestSlope[3])
            zeroPoint = linearFunction.getZeroPoint(linFunction[0], linFunction[1])
            highPoint = linearFunction.getXforY(linFunction[0], linFunction[1], self.csvData[1][analyzer.getHighestValueOfArray(self.csvData[0])[0]])
            print(highPoint)
            linPlot = linearFunction.createFunctionValuesBetweenToXValues(linFunction[0], linFunction[1], zeroPoint, highPoint)
            equiPoint = linearFunction.getMiddlePointBetweenTwoPointsOnLinearFunction(pointsOfHighestSlope[0], pointsOfHighestSlope[2], linFunction[0], linFunction[1])
            self.cSample.set(analyzer.calculateConcentrationOfSampleSolution(self.cTiter, equiPoint[0], self.vSample))
            
            plot = plotter.createEmptyFigureWithSubplot()
            plotter.addDataToSubplot(plot[1], self.csvData[0], self.csvData[1], color = "blue", marker = "x", label = "titration readings")
            plotter.addDataToSubplot(plot[1], linPlot[0], linPlot[1], color = "green", linestyle ="dashed", label = "highest slope")
            plotter.addDataToSubplot(plot[1], equiPoint[0], equiPoint[1], color = "red", marker ="o", label="equivalence point")
            plotter.enableGridForSubplot(plot[1])
            plotter.enableLegendForSubplot(plot[1])
            self.createUiElementFromFigure(plot[0])
            return None
            
    def selectFile(self):
        self.fileUrl.set(tk.filedialog.askopenfilename(initialdir = "Desktop", title = "Select Data", filetypes = [("CSV Files", "*.csv")] ))
        self.csvData = fileHandler.loadFilesFromCsv(self.fileUrl.get())
        return None
        
        
        
        