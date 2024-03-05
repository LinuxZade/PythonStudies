#-----------------------------------------
# Numpy Library :
#-----------------------------------------
import numpy as np

#-----------------------------------------
# Array Declerations and Basic Operations:
#-----------------------------------------
a = np.array( [ [0,1,2], [3,4,5] ] )
print(a)        # a = [0 1 2]
                #     [3 4 5]
print(a[0,0])   # ans = 0
print(a[1,1])   # ans = 4

a = np.arange(6).reshape(2,3)
print(a)        # a = [0 1 2]
                #     [3 4 5]

print(a.size)     # ans = 6
print(a.dtype)    # int64
print(a.shape)    # (2,3) 
print(a.shape[0]) # 2
print(a.shape[1]) # 3

a = np.ones(4).reshape(2,2)
print(a)    # [1 1]
            # [1 1]
b = np.arange(4).reshape(2,2) 
print(b)    # [0 1]
            # [2 3]

print(b-a)  # [-1  0]
            # [ 1  2]

print(b*a)  # [0  1] ->dotProduct
            # [2  3]

print(b@a)  # [1  1] ->matrixMult
            # [5  5]

print(b/a)  # [0 1]
            # [2 3]

print(b.min())  # ans = 0
print(b.max())  # ans = 3

print(b.sum(axis=0))  # ans = [2 4] 
print(b.sum(axis=1))  # ans = [1 5]
print(b.sum())        # ans = 6

c = np.array( [1,2,3,4,5,6,7,8,9,10,11,12] )
odd  = c[0:12:2]
even = c[1:12:2]
print(odd)  # [1 3 5 7 9 11]
print(even) # [2 4 5 6 10 12]

h = np.hstack((odd,even))
print(h) # [1 3 5 7 9 11 2 4 6 8 10 12]

v = np.vstack((odd,even))
print(v) # [1 3 5 7 9 11 ]
         # [2 4 6 8 10 12]

# Random Number Gen
randArr = np.random.rand(2,3) # 2x3 arr with uniform dist.

# Find Unique Numbers in Arr
a = np.array([1,1,1,2,2,2,3,3,3,4,4,4])
print(np.unique(a)) # [1 2 3 4]

# Transpose of Arr
a = np.arange(6).reshape(2,3)
print(a)    # [0 1 2]
            # [3 4 5]

print(a.T)  # [0 3]
            # [1 4]
            # [2 5]

print(a@a.T) # [5  14]
             # [14 50]

# Example: mse calculation
N = 10
predictions  = np.array([1, 2, 3])
measurements = np.array([1.1, 2.1, 3.1])

error = (1/N)*np.sum(np.square(predictions-measurements))
print(error) #ans = 0.1*(0.01 + 0.01 + 0.01) = 0.003

# Diagonal Matrix decleration
a = np.eye(3)
print(a) # [1 0 0]
         # [0 1 0]
         # [0 0 1]

b = np.diag([1,2,3,4])
print(b) # [1 0 0 0]
         # [0 2 0 0]
         # [0 0 3 0]
         # [0 0 0 4]

# Structured Arrays
a = np.array( [('Name1',18,75.1)  ,\
               ('Name2',35,85.2)  ,\
               ('Name3',65,91.5)] ,\
               dtype = [('name','<U10')  ,\
                        ('age','<i8')    ,\
                        ('weight','<f8')] )

print(a[0])           # [Name1 18 75.1]
print(a['name'])      # [Name1 Name2 Name3]
print(a['age'])       # [18 35 65]
print(a['weight'])    # [75.1 85.2 91.5]
print(a['age'].min()) # 18


#--------------------------------------------------
# I/O with Numpy
#--------------------------------------------------
from io import StringIO
#np.genfromtxt( StringIO(data), delimeter="," )

#Example:
unicodeDta = u"1,2,3\n4,5,6"
a = np.genfromtxt(StringIO(unicodeDta),delimiter=",")
print(a) # [1 2 3]
         # [4 5 6]
         
print(a[1,1]) # 5

#Example:
unicodeDta = u"""
# This is 1st comment Line
# This is 2nd comment Line
# Parameter is given below:
1 # Param-1
2 # Param-2
3 # Param-3
"""
a = np.genfromtxt(StringIO(unicodeDta),\
                  comments="#",\
                  delimiter=",")

print(a) # [1 2 3]

#Example:
unicodeDta = u"""
# This is 1st comment Line
# This is 2nd comment Line
# Array is given below:
1,2,3.05
4,5,6.05
7,8,9.05
"""
a = np.genfromtxt(StringIO(unicodeDta),\
                  comments="#",\
                  delimiter=",")

print(a) # [1 2 3.05]
         # [4 5 6.05]
         # [7 8 9.05]









































