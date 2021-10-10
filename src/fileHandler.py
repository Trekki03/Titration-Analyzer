# -*- coding: utf-8 -*-
"""
First created on 10/10/2021
@author: github.com/Trekki03
"""

import numpy as np
from typing import Tuple

def loadFilesFromCsv(fileName: str) -> Tuple[np.array, np.array]:
    """loades data from csv-File into two arrays
    csv has to be from styl:
    
    comment\\
    volume,pH\\
    volume,pH\\
    volume,pH\\
    ...
    
    Args:
        fileName (str): url to file

    Returns:
        Tuple[np.array, np.array]:
            return[0]: x-Values
            return[1]: y-Values
    """
    csvData = np.loadtxt(fileName, delimiter=",", skiprows=1)
    x = []
    y = []
    for counter in csvData:
        x.append(counter[0])
        y.append(counter[1])
    x = np.array(x)
    y = np.array(y)
    return (x,y)
