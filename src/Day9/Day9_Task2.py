# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:35:32 2026

@author: RAKSHA
"""

import pandas as pd
grades=pd.Series([85, None,92,45,None,78,55])
print("original:\n",grades)
print("\nMissing:\n", grades.isnull())

filled = grades.fillna(0)
print("\nFilled:\n", filled)

print("\nAbove 60:\n", filled[filled > 60])