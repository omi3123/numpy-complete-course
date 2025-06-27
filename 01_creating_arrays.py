#Creating Arrays
#1
import numpy as np
x = np.array([10, 20, 30])
print(x)

#2
import numpy as np
arr=np.array([1,2,3])
arr2d=np.array([[1,2],[3,4],[5,6]])
print(arr)
print(arr2d)

#3 Two Dimensions
import numpy as np
arr_2d = np.array([[10, 20], [30, 40], [50, 60]])
print(arr_2d)

#4 Zero Array
import numpy as np
zero_arr=np.zeros((2,2))
print(zero_arr)

import numpy as np
zero_arr=np.zeros((2,2,3))
print(zero_arr)

#5 Array of Ones

import numpy as np
ones = np.ones((3,2))
print(ones)

import numpy as np
ones = np.ones((3,2,2))
print(ones)

#6 Array Of Empty

import numpy as np
empty = np.empty((2,2))
print(empty)

import numpy as np
empty = np.empty((2,2,2))
print(empty)

#7 Using arange()
#using arange(array range)
import numpy as np
arr = np.arange(0, 10, 2) 
print(arr)

#8 Using linspace
import numpy as np
arr = np.linspace(0, 1, 5)
print(arr)  

#9 Identity matrix
import numpy as np
i = np.eye(3)
print(i)

#10 Combo
import numpy as np
a = np.zeros((2, 4))
b = np.ones((3, 3))
c = np.arange(5, 15, 3)
d = np.eye(4)
print(a)
print(b)
print(c)
print(d)