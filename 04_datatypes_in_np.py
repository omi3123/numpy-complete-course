#1
import numpy as np
arr = np.array([1, 2, 3])
print(arr.dtype)  

#2
import numpy as np
arr = np.array([1, 2, 3], dtype='float')
print(arr)
print(arr.dtype)  

#Using astype()

#astype() changes the types

#3
import numpy as np
arr = np.array([1.1, 2.2, 3.3])
new_arr = arr.astype('int')
print(new_arr)       
print(new_arr.dtype)  

#4
import numpy as np
a = np.array([5, 10, 15])
b = np.array([True, False, True])
c = np.array(['apple', 'banana', 'cherry'])
d = a.astype('float')
e = b.astype('int')
print(a.dtype)
print(b.dtype)
print(c.dtype)
print(d)
print(e)