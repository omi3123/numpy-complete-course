#Basic LCM

import numpy as np
print(np.lcm(4, 6))

#LCM of arrays

import numpy as np
a = np.array([3, 6, 9])
b = np.array([5, 4, 12])
print(np.lcm(a, b))  

#Use with broadcasting

import numpy as np
x = np.array([2, 4])
y = 6
print(np.lcm(x, y))  

#LCM of Two Scalars

import numpy as np
print(np.lcm(8, 12))

#LCM of Two Arrays (Same Shape)

import numpy as np
a = np.array([2, 4, 6])
b = np.array([3, 5, 9])
print(np.lcm(a, b))  

#LCM of Array with Scalar (Broadcasting)

import numpy as np
arr = np.array([3, 6, 9])
value = 12
print(np.lcm(arr, value)) 

#2D and 1D Array (Matrix-style Broadcasting)

import numpy as np
x = np.array([[2], [4], [6]])
y = np.array([3, 6])
print(np.lcm(x, y))
