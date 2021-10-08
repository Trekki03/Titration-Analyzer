# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:57:56 2021

@author: trekk
"""
import numpy as np

def getPointsOfHighestSlope(xList, yList):
    
    hoechsteSteigung = 0
    hoechsteSteigungIndex = -1
    
    for i in range(0, xList.size-1):
        steigung = (yList[i+1]-yList[i])/(xList[i+1]-xList[i])
        if steigung > hoechsteSteigung:
            hoechsteSteigung = steigung
            hoechsteSteigungIndex = i
    return (hoechsteSteigung, hoechsteSteigungIndex)
    
    
def getLinearFunctionBetweenPointsOfHighestSlope(xList, yList):

    highestSlopePointData = getPointsOfHighestSlope(xList, yList)
    m = highestSlopePointData[0]
    xIndex = highestSlopePointData[1]
    x = xList[xIndex] 
    b = yList[xIndex] - (m*x)
    nullPointX = (-b/m)
    return (m,x,b,xIndex,nullPointX)