# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
a=np.array(([1,2,3],[4,5,6]))
b=np.array(([10,20,30]))
result=a+b
print(result)
print()
arr=np.random.randint(1000000)
print(arr)
squared=arr**2
print(squared)

## 3dimensional array
import numpy as np
a=np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])
print(a)

#zero dimension
import numpy as np

a = np.array(5)
print(a)

#1 dimensional array
import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

result = a + b
print(result)

#2 dimensional array
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

result = a + b
print(result)

#reshape
arr=np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)
a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)
hstacked=np.hstack((a,b))
print(hstacked)


data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))

arr=np.arange(1,2,3)
print(arr.shape)
print(arr)

arr=np.random.rand(2,3)
print(arr)

arr=np.linspace(0,3,5)
print(arr)

arr=np.random.uniform(20,30, size=(2,2))
print(arr)
print(arr.size)

arr=np.array([1.2,2.8,-3.7])
print(np.floor(arr))

arr=np.array([1.2,2.8,-3.7])
print(np.ceil(arr))
print(np.trunc(arr))
print(np.round(arr))
