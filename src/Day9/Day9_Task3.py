# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:45:17 2026

@author: RAKSHA
"""

import pandas as pd


usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])


cleaned = usernames.str.strip().str.lower()


contains_a = cleaned.str.contains('a')

print("Cleaned Usernames:\n", cleaned)
print("\nContains 'a':\n", contains_a)
