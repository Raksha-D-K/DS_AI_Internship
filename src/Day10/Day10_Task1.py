# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:19:53 2026

@author: RAKSHA
"""

import pandas as pd
df=pd.read_csv("customer_orders.csv")
print("First rows:\n", df.head())
print("Shape of the dataset:", df.shape)
print("\nMissing values per column:")
print(df.isna().sum())
df["order_id"] = df["order_id"].fillna(df["order_id"].median())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)
