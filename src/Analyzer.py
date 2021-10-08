# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:40:33 2021

@author: trekk
"""

#Import 
import numpy as np

def calculateEquivalencePoint(x1, x2, m, b):
    xE = (x2 + x1)/2
    yE = m*xE+b
    return (xE, yE)

def calculateConcentration(cTiter, vTiter, vSample):
    cSample = (cTiter * vTiter)/vSample
    return cSample




