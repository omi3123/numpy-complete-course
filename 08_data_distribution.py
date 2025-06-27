#1
import numpy as np
data = np.random.normal(loc=50, scale=10, size=1000)
print(data[:5]) 

#2
import numpy as np
a = np.random.normal(0, 1, 5)    
b = np.random.normal(10, 2, 3)   
c = np.random.normal(loc=100, scale=20, size=2)
print(a)
print(b)
print(c)

#3
import numpy as np
x = np.random.normal(0, 1, 10) 
print("Normal dist sample:", x)

#4
import numpy as np
x = np.random.normal(50, 15, 8)  
print("Spread out values:", x)

#5
import numpy as np
samples = np.random.normal(0, 1, 1000)
print(samples)

#6
import numpy as np
a = np.random.normal(0, 1, 1000)   
b = np.random.normal(0, 5, 1000)   
print("Mean of a:", np.mean(a))
print("Mean of b:", np.mean(b))
