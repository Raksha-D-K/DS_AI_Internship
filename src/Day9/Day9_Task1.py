# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:19:11 2026

@author: RAKSHA
"""

import pandas as pd

products = pd.Series([700, 150, 300], 
                     index=['Laptop', 'Mouse', 'Keyboard'])

print(products)
print(products['Laptop'])
print(products.iloc[:2])
