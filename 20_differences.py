#Basic difference

import numpy as np
a = np.array([10, 20, 25, 40])
print(np.diff(a))

#2nd order difference (n=2)

import numpy as np
a = np.array([10, 20, 25, 40])
print(np.diff(a, n=2))

#Differences in 2D array (row-wise flatten)

import numpy as np
x = np.array([[5, 10, 15],
              [20, 25, 30]])
print(np.diff(x))

#Temperature Change (1st Order)

import numpy as np
temps = np.array([22, 25, 21, 26, 30])
change = np.diff(temps)
print(change)

#2nd Order – Change in speed (acceleration)

import numpy as np
speeds = np.array([0, 10, 25, 55])
first_diff = np.diff(speeds)
second_diff = np.diff(speeds, n=2)
print("1st Order:", first_diff)   
print("2nd Order:", second_diff)    

#Difference in repeated pattern

import numpy as np
x = np.array([5, 5, 5, 10, 10, 15])
print(np.diff(x))  
