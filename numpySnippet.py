#-----------------------------------------
# Numpy Library :
#-----------------------------------------
import numpy as np

#-----------------------------------------
# Array Declerations :
#-----------------------------------------
a = np.array([1,2,3]) 
print(a[0]+a[1]+a[2]) # ans = 6

b = np.array( [ (1,2,3), (4,5,6) ] )
print(b)        # b = [1 2 3]
                #     [4 5 6]
print(b[0,0])   # ans = 1
print(b[1,1])   # ans = 5

c = np.arange(16).reshape(2,8)
print(c) # [00 01 02 03 04 05 06 07]
         # [08 09 10 11 12 13 14 15]

print(c.size)     # ans = 16
print(c.dtype)    # int64
print(c.shape)    # (2,8) 
print(c.shape[0]) # 2
print(c.shape[1]) # 8

d = np.zeros( (4,4) )
print(d)    # [0 0 0 0]
            # [0 0 0 0]
            # [0 0 0 0]
            # [0 0 0 0]


#-----------------------------------------
# Basic Operations :
#-----------------------------------------
a = np.array( [1,2,3,4] )
b = np.array( [2,3,4,5] )
print(b-a) # [1 1 1 1]
print(b+a) # [3 5 7 9]
print(b*a) # [2 6 12 20]
print(b/a) # [2 1.5 1.33 1.25]













