# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:54:41 2021

@author: trekk
"""
import numpy as np

def loadFilesFromCsv(fileName):
    csvData = np.loadtxt(fileName, delimiter=",", skiprows=1)
    x = []
    y = []
    for counter in csvData:
        x.append(counter[0])
        y.append(counter[1])
    x = np.array(x)
    y = np.array(y)
    return (x,y)
