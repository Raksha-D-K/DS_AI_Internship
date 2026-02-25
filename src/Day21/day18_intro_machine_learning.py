# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:59:29 2026

@author: RAKSHA
"""

# ===============================
# 1. Import Libraries
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ===============================
# 2. Load Dataset
# ===============================
df = pd.read_csv("Bengaluru_House_Data.csv")
print("Dataset Shape:", df.shape)
print(df.head())

# ===============================
# 3. Data Cleaning
# ===============================

# Drop unnecessary columns
df.drop(['area_type', 'availability', 'society', 'balcony'], axis=1, inplace=True)

# Drop missing values
df.dropna(inplace=True)

# Convert total_sqft to numeric
def convert_sqft(x):
    try:
        if '-' in str(x):
            tokens = x.split('-')
            return (float(tokens[0]) + float(tokens[1])) / 2
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(inplace=True)

# ===============================
# 4. Feature Engineering
# ===============================

# Create BHK column
df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]))
df.drop('size', axis=1, inplace=True)

# Price per sqft
df['price_per_sqft'] = df['price']*100000 / df['total_sqft']

# Reduce rare locations
location_stats = df['location'].value_counts()
df['location'] = df['location'].apply(lambda x: x if location_stats[x] > 10 else 'other')

# ===============================
# 5. Outlier Removal
# ===============================

# Remove sqft per BHK less than 300
df = df[df['total_sqft']/df['bhk'] >= 300]

# Remove extreme price per sqft
mean = df['price_per_sqft'].mean()
std = df['price_per_sqft'].std()
df = df[(df['price_per_sqft'] > (mean - std)) & (df['price_per_sqft'] <= (mean + std))]

# ===============================
# 6. One-Hot Encoding
# ===============================
df = pd.get_dummies(df, columns=['location'], drop_first=True)

# ===============================
# 7. Train Test Split
# ===============================
X = df.drop(['price', 'price_per_sqft'], axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===============================
# 8. Model Training
# ===============================

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# Lasso
lasso = Lasso()
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)

# Decision Tree
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

# ===============================
# 9. Evaluation Function
# ===============================
def evaluate_model(name, y_test, y_pred):
    print(f"--- {name} ---")
    print("R2 Score:", r2_score(y_test, y_pred))
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
    print()

evaluate_model("Linear Regression", y_test, lr_pred)
evaluate_model("Lasso Regression", y_test, lasso_pred)
evaluate_model("Decision Tree", y_test, dt_pred)

# ===============================
# 10. Feature Importance (Decision Tree)
# ===============================
importance = pd.Series(dt.feature_importances_, index=X.columns)
importance.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 Important Features")
plt.show()