#1D
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr[0])  
print(arr[2])  

#2D
import numpy as np
arr2d = np.array([[5, 10, 15],
                  [20, 25, 30]])
print(arr2d[0, 0])  
print(arr2d[1, 2])  

#Negative in 1D
import numpy as np
arr = np.array([100, 200, 300, 400])
print(arr[-1])  
print(arr[-2])  

#Negative 2D
import numpy as np
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d[-1, -1])  

#combo
import numpy as np
x = np.array([[100, 200, 300],
              [400, 500, 600]])
print(x[0, 1])     
print(x[1, -1])    
print(x[-2, -3])   

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])    
print("Last element:", arr[-1])     

import numpy as np
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
print("Row 0, Col 1:", arr2d[0][1])   
print("Row 1, Col 2:", arr2d[1][2])    