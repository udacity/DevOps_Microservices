"""Appliable Functions to a Pandas GroupBy Operation (I.E Plugins)"""

import numpy


def tanimoto(list1, list2):
    """tanimoto coefficient

    In [2]: list2=['39229', '31995', '32015']
    In [3]: list1=['31936', '35989', '27489', '39229', '15468', '31993', '26478']
    In [4]: tanimoto(list1,list2)
    Out[4]: 0.1111111111111111

    Uses intersection of two sets to determine numerical score

    """

    intersection = set(list1).intersection(set(list2))
    return float(len(intersection))/(len(list1) + len(list2) - len(intersection))

def npsum(x):
    """Numpy Library Sum"""

    return numpy.sum(x)

def npmedian(x):
    """Numpy Library Median"""

    return numpy.median(x)
