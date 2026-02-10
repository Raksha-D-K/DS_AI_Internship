# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:53:40 2026

@author: RAKSHA
"""

import numpy as np
scores=np.random.randint(50,101,size=(5,3))
mean_scores=scores.mean(axis=0)
centered_scores=scores-mean_scores
print("original scores:")
print(scores)
print("\nMean Score of Each Subject:")
print(mean_scores)

print("\nCentered (Normalized) Scores:")
print(centered_scores)