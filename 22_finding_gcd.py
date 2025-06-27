#GCD of Two Numbers

import numpy as np
print(np.gcd(12, 18))

#GCD of Two Arrays (Same shape)

import numpy as np
a = np.array([12, 15, 21])
b = np.array([8, 25, 14])
print(np.gcd(a, b))  

#GCD with Scalar (Broadcasting)

import numpy as np
arr = np.array([10, 20, 30])
val = 5
print(np.gcd(arr, val))

#2D Array with Broadcasting

import numpy as np
x = np.array([[10], [20], [30]])
y = np.array([5, 10])
print(np.gcd(x, y))

#GCD in Matrix Broadcasting Style

import numpy as np
x = np.array([[18], [30]])
y = np.array([12, 21])
print(np.gcd(x, y))

#GCD of a List with a Common Number

import numpy as np
arr = np.array([100, 150, 200])
common = 50
print(np.gcd(arr, common))

#Simplifying Fractions

import numpy as np
numerators = np.array([8, 15, 24])
denominators = np.array([12, 25, 36])
gcd_values = np.gcd(numerators, denominators)
simplified_numerators = numerators // gcd_values
simplified_denominators = denominators // gcd_values
print("Simplified Fractions:")
for n, d in zip(simplified_numerators, simplified_denominators):
    print(f"{n}/{d}")