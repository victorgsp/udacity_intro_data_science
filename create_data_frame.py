#!/usr/bin/env python3

#import pandas as pa
from pandas import DataFrame, Series

data = {
    'name': Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index=['a', 'b', 'c', 'd']),
    'age': Series([22,38,26,35], index=['a', 'b', 'c', 'd']),
    'fare': Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
    'survived?': Series([False, True, True, False], index=['a', 'b', 'c', 'd'])    
    }
dataFrame = DataFrame(data)

print(dataFrame)
