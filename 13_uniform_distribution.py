#Real Examples


#Random float between 0 and 1

import numpy as np
values = np.random.uniform(0, 1, 5)
print("Random values:", values)

#Random marks between 50 and 100

import numpy as np
marks = np.random.uniform(50, 100, 10)
print("Random marks:", marks)

#Temperature between 30°C and 45°C

import numpy as np
temps = np.random.uniform(30, 45, 7)
print("Temperature readings (7 days):", temps)

#Game - Random Speed Generator

import numpy as np
speed = np.random.uniform(60, 120, 3)
print("Car speed (km/h):", speed)

#Random Discount Percentage (10% to 50%)

import numpy as np
discounts = np.random.uniform(10, 50, 6)
print("Discounts offered:", discounts)

#Random Time Taken to Complete Task (in minutes)

import numpy as np
times = np.random.uniform(20, 60, 5)
print("Task completion times (minutes):", times)

#Game Level - Random Spawn Location (X-axis)

import numpy as np
x_locations = np.random.uniform(-100, 100, 8)
print("Enemy spawn locations (x-axis):", x_locations)

#Random Password Strength Score (1 to 10)

import numpy as np
scores = np.random.uniform(1, 10, 4)
print("Password strength scores:", scores)
