#Without using ufuncs

a = [1, 2, 3]
b = [4, 5, 6]
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print(result)


#Using with ufuncs

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.add(a, b))

#Without using ufuncs

a = [2, 4, 6]
b = [1, 3, 5]
result = []
for i in range(len(a)):
    result.append(a[i] * b[i])
print(result) 

#Using with ufuncs

import numpy as np
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
print(np.multiply(a, b)) 

#Without using ufuncs

a = [10, 20, 30]
b = [2, 5, 3]
result = []
for i in range(len(a)):
    result.append(a[i] / b[i])
print(result) 

#Using with ufuncs

import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 5, 3])
print(np.divide(a, b))

import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(np.subtract(a, b))  

import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(np.power(a, b))    

import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(np.mod(a, b))       

import numpy as np
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(np.floor_divide(a, b))  
