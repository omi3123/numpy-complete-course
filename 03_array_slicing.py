#1
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])  
print(arr[:3])   
print(arr[2:])    

#2
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[-3:-1])  

#3
import numpy as np
x = np.array([
    [ 1,  2,  3,  4],  
    [ 5,  6,  7,  8],  
    [ 9, 10, 11, 12],   
    [13, 14, 15, 16]     
])
print(x[0:2, 0:2])
print(x[2:, 2:])

#4
import numpy as np
x = np.array([
    [ 1,  2,  3,  4],  
    [ 5,  6,  7,  8],  
    [ 9, 10, 11, 12],   
    [13, 14, 15, 16]     
])
print(x[1:3, 1:3])
print(x[:2, 2:])
print(x[-2:, :2])

#5
#Array Slicing in 1D

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])  
print(arr[:3])     
print(arr[-3:])   

#6
#Array Slicing in 2D

import numpy as np
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9,10,11,12]])
print(arr2d[0:2, 1:3])   
print(arr2d[:, 2:])    