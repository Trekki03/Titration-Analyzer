# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:08:04 2021

@author: trekk
"""
import matplotlib.pyplot as plt
import numpy as np




def plotAllData(xListTitration, yListTitration, mLin, bLin, xNullLin, xHighSlopeLin, xE, yE):
    figure = plt.Figure(figsize=(5,4), dpi=100)
    ax = figure.add_subplot(1,1,1)
    ax.plot(xListTitration, yListTitration, color = "blue", marker = "x", label = "titration readings")
    linFuncValues = createLinValues(mLin, bLin, xNullLin, xHighSlopeLin)
    ax.plot(linFuncValues[0],linFuncValues[1], color = "green", linestyle ="dashed", label = "highest slope")
    ax.plot(xE, yE, color = "red", marker ="o", label="equivalence point")
    ax.legend()
    ax.grid()
    return figure

def createLinValues(m, b, xNull, xHighSlope):
    x = np.linspace(xNull, xHighSlope+1)
    y = (m*x) + b
    return (x,y)
