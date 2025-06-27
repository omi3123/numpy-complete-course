#1
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   

#2
import numpy as np
a = np.array([10, 20, 30, 40])
print(a.shape)   

#3
import numpy as np
b = np.array([1, 2, 3, 4, 5, 6])
reshaped = b.reshape(2, 3)  
print(reshaped)

#4
import numpy as np
c = np.array([10, 20, 30, 40, 50, 60])
print(c.reshape(3, -1))   

#5
import numpy as np
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d.shape) 

#combo
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
a = x.reshape(3, 2)
b = x.reshape(2, 3)
c = x.reshape(-1, 1)
print(a.shape)   
print(b.shape)   
print(c.shape)   



#7
import numpy as np
a = np.array([10, 20, 30, 40, 50, 60])
a2d = a.reshape(2, 3)   
print(a2d)

#8
import numpy as np
b = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b3d = b.reshape(2, 2, 2)
print(b3d)

#9
import numpy as np
d = np.array([1, 2, 3, 4, 5, 6])
print(d.reshape(-1, 2))  

#10
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(x.reshape(2, 4).shape)   
print(x.reshape(4, 2).shape)  
print(x.reshape(-1, 1).shape)   
print(x.reshape(2, 2, 2).shape)  
