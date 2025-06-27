#1
import numpy as np
arr = np.array([10, 20, 30])
copy_arr = arr.copy()
copy_arr[0] = 99
print("Original:", arr)     
print("Copy:", copy_arr)   
print(copy_arr.base) 

#2
import numpy as np
arr = np.array([1, 2, 3])
view_arr = arr.view()
view_arr[1] = 99
print("Original:", arr)     
print("View:", view_arr)   
print(view_arr.base) 

#3
import numpy as np
x = np.array([100, 200, 300])
a = x.copy()
b = x.view()
a[0] = 111
b[1] = 222
print(x)
print(a)
print(b)

#4
import numpy as np
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print("Original:", a)   
print("Copy:    ", b)       

#5
import numpy as np
arr = np.array([10, 20, 30])
copied = arr.copy()
print("Base of copied:", copied.base)   

#6
import numpy as np
a = np.array([5, 6, 7])
b = a.view()
b[1] = 99
print("Original:", a)   
print("View:    ", b)   

#7
import numpy as np
arr = np.array([1, 2, 3])
viewed = arr.view()
print("Base of view:", viewed.base is arr)   