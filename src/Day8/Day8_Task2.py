# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:04:18 2026

@author: RAKSHA
"""

import numpy as np

data = np.arange(24)
print("Original 1D array:")
print(data)
print("Shape:", data.shape)


reshaped_data = data.reshape(4, 3, 2)
print("\nReshaped array (4, 3, 2):")
print(reshaped_data)
print("Shape:", reshaped_data.shape)


transposed_data = reshaped_data.transpose(0, 2, 1)
print("\nTransposed array (4, 2, 3):")
print(transposed_data)
print("Final Shape:", transposed_data.shape)
