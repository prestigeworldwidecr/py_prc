
#   Filename: assessment.py                                   
#   Author: Craig Saiz                                         
#   Date: 04-may-2023                                          
#   Purpose: Write a function median_absolute_deviation(data) that takes a list of numbers as input and returns the median absolute deviation (MAD) of the data. The MAD is defined as the median of the absolute differences between each data point and the median of the data. For example, if the data is [1, 3, 5, 7, 9], the median is 5, and the absolute differences between each data point and the median are [4, 2, 0, 2, 4]. The median of these differences is 2, so the MAD is 2.

#   Edge cases:
#   If the input data is empty, the function should return None.
#   If the input data has only one element, the function should return 0.
#   If the input data has an even number of elements, the function should return the average of the two medians.
#   Tip: use the statistics module by starting with import statistics

# print (1 + 1)

import math
import random
import statistics
from collections import Counter

test1 = []
test2 = [1]
test3 = [1, 3, 5, 7, 9]
test4 = [4, 2, 0, 2, 4]
test5 = [4, 2, 0, 2]
test6 = [1, 3, 5, 7, 9, 11]

## returns list of absolute differences
def getAbsDifferences(data) :
    absDifferences = []
    m2 = statistics.median(data)

    for i in range(0, len(data)) :
        absDifferences.append(abs(data[i] - m2))

    return absDifferences

def median_absolute_deviation(data) :
    l = len(data)
    m1 = statistics.median(data)

    if l == 0 :
        MAD = None
    if l == 1 :
        MAD = 0
    if (l % 2) == 0 :
        m2 = statistics.median(getAbsDifferences(data))
        MAD = statistics.mean([m1, m2])
    else :
        MAD = statistics.median(getAbsDifferences(data))

    # print(MAD)
    return MAD

median_absolute_deviation(test6)