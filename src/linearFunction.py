# -*- coding: utf-8 -*-
"""
First created on 10/10/2021
@author: github.com/Trekki03
"""

import numpy as np
from typing import Tuple


def getFunctionBetweenToPoints(x1: float, y1:float, x2:float, y2:float) -> Tuple[float, float]:
    """calculates m and b for a linear Function (f(x)=mx+b) from two points

    Args:
        x1 (float): x-value of point one
        y1 (float): y-value of point one
        x2 (float): x-value of point two
        y2 (float): y-value of point two

    Returns:
        Tuple[float, float]:
            return[0]: slope (m)
            return[1]: y-axis intercept (b)
    """
    m = (y2-y1)/(x2-x1)
    b = y1 - (m*x1)
    return (m, b)

def getZeroPoint(m: float, b: float) -> float:
    """calculates x-value of the zeropoint of the function

    Args:
        m (float): slope of the function
        b (float): y-axis intercept of the function

    Returns:
        float: x-value of the zeropoint
    """
    x = (0-b)/m
    return x

def getXforY(m: float, b: float, y: float) -> float:
    """calculates x-value for a y-value

    Args:
        m (float): slope of the function
        b (float): y-axis intercept of the function
        y (float): y-value of interest 

    Returns:
        float: return corrosponding x-value or None, if y is true for every x-value
    """
    if m != 0:
        x = (y-b)/m
    else:
        x = None
    return x

def createFunctionValuesBetweenToXValues(m: float, b: float, x1: float, x2: float) -> Tuple[np.array, np.array]:
    """creates lists with function values between two points for e.g. plotting

    Args:
        m (float): slope of the function
        b (float): y-axis interception of the function
        x1 (float): x-value one
        x2 (float): x-Value two

    Returns:
        Tuple[np.array, np.array]:
            return[0]: array with xValues
            return[1]: array with yValues
    """
    xList = np.linspace(x1, x2)
    yList = m*xList + b
    return (xList, yList)

def getMiddlePointBetweenTwoPointsOnLinearFunction(x1: float, x2: float, m: float, b: float) -> Tuple[float, float]:
    """calculates the middle point between to point on a linear function

    Args:
        x1 (float): x-value of first point
        x2 (float): x-value of second point
        m (float): slope of the function
        b (float): y-axis interception of the function

    Returns:
        Tuple[float, float]:
            return[0]: x-value of the point
            return[1]: y-value of the point
    """
    if x1 == x2:
        raise NameError("[getMiddlePointBetweenTwoPointsOnLinearFunction] x1 and x2 are no allowed to be the same")
    
    xE = (x1 + x2)/2
    yE = m*xE+b
    return (xE, yE)