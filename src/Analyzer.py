# -*- coding: utf-8 -*-
"""
First created on 10/10/2021
@author: github.com/Trekki03
"""

import numpy as np
from typing import Tuple

def getPointsOfHighestSlope(xArray: np.array, yArray: np.array) -> Tuple[float, float, float, float, int]:
    """calculates the highest slope between two following points in an x-y-dataset

    Args:
        xArray (np.array): array with x-Values
        yArray (np.array): array with y-Values

    Returns:
        Tuple[float, float, float, float, int]:
            return[0]: x-Value of first point
            return[1]: y-Value of first point
            return[2]: x-Value of second point
            return[3]: y-Value of second point
            return[4]: array index of the first point
    """
    if(xArray.size != yArray.size):
        raise NameError("[getPointsOfHighestSlope] more or less x than y values")
    
    highestSlope = 0
    highestSlopeIndex = -1
    
    for i in range(0, xArray.size-1):
        slope = abs((yArray[i+1]-yArray[i])/(xArray[i+1]-xArray[i]))
        if slope > highestSlope:
            highestSlope = slope
            highestSlopeIndex = i
            
    if(highestSlopeIndex == -1):
        output = None
    else:
        output = (xArray[highestSlopeIndex], yArray[highestSlopeIndex], xArray[highestSlopeIndex+1], yArray[highestSlopeIndex+1], highestSlopeIndex)
    return output

def getHighestValueOfArray(array: np.array) -> Tuple[int, float]:
    """searches for highest value in an array

    Args:
        array (np.array): array to be searched

    Returns:
        Tuple[int, float]: OR NONE if failed
            return[0]: index of highest value of
            return[1]: highest value
    """
    highestValue = float("-inf")
    highestValueIndex = None
    for i in range(0,array.size):
        if array[i] > highestValue:
            highestValue = array[i]
            highestValueIndex = i
    if(highestValueIndex != None):
        output = (highestValueIndex, highestValue)
    else:
        output = None
    return output
            

def calculateConcentrationOfSampleSolution(cTiter: float, vTiter: float, vSample: float) -> float:
    """calculates the concentraiton of the sample acid or base 

    Args:
        cTiter (float): conentration of the titer in mol/l
        vTiter (float): volume of the titer in ml
        vSample (float): volume of the sample in ml

    Returns:
        float: concentration of the sample in mol/l
    """
    cSample = (cTiter * vTiter) / vSample
    return cSample