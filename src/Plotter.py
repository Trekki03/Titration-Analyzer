# -*- coding: utf-8 -*-
"""
First created on 10/10/2021
@author: github.com/Trekki03
"""

import matplotlib.pyplot as plt
from typing import Tuple

def createEmptyFigure() -> plt.figure:
    """generates an empty matplotlib figure in size (5,4)

    Returns:
        plt.figure: empty figure
    """
    figure = plt.Figure(figsize=(5,4), dpi=100)
    return figure

def createEmptyFigureWithSubplot() -> Tuple[plt.figure, plt.subplot]:
    """generates an empty figure with subplot

    Returns:
        Tuple[plt.figure, plt.subplot]:
            return[0]: figure
            return[1]: subplot
    """
    figure = plt.Figure(figsize=(5,4), dpi=100)
    subplot = figure.add_subplot(1,1,1)
    return (figure,subplot)

def addDataToSubplot(subplot: plt.subplot, xData, yData, **kwargs):
    """adds data to a subplot

    Args:
        subplot (plt.subplot): subplot to which data should be added
        xData (float/int, np.array, list): x-Value or Array
        yData (float/int, np.array, list): y-Value or Array
    
    **Kwargs:
        color (str): color of the data
        marker (str): marker of the data
        linestyle (str): linestyl of the data
        label (str): label of the data
    """
    color = kwargs.get("color", None)
    marker = kwargs.get("marker", None)
    linestyle = kwargs.get("linestyle", None)
    label = kwargs.get("label", None)
    subplot.plot(xData, yData, color = color, marker = marker, linestyle = linestyle, label = label)
    return None

def enableLegendForSubplot(subplot: plt.subplot):
    """enables  legend for subplot

    Args:
        subplot (plt.subplot): subplot
    """
    subplot.legend()
    return None
    
def enableGridForSubplot(subplot: plt.subplot):
    """enables or disables grid for subplot

    Args:
        subplot (plt.subplot): subplot
    """
    subplot.grid()
    return None