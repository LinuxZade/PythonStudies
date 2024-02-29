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
print(b-a)      # [1 1 1 1]
print(b+a)      # [3 5 7 9]
print(b*a)      # [2 6 12 20]
print(b/a)      # [2 1.5 1.33 1.25]
print(a<=2)     # [True True False False]
print(a@b)      # Matrix mult, ans = 40
print(b.sum())  # ans = 14
print(b.min())  # ans = 2
print(b.max())  # ans = 5

c = np.array( [1,2,3,4,5,6,7,8,9,10,11] )
print(c[0:11:2]) # [1 3 5 7 9 11]
print(len(c))    # ans = 11

d = np.array( [ (11,12,13,14,15),
                (16,17,18,19,20),
                (21,22,23,24,25) ] )

for row in d:   # [11 12 13 14 15]
    print(row)  # [16 17 18 19 20]
                # [21 22 23 24 25] 
    
for element in d.flat: 
    print(element)

print(d.reshape(1,15))
print(d.reshape(15,1))
print(d.reshape(3,5))




















