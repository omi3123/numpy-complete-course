#1
import numpy as np
arr = np.random.randint(0, 10, size=5)
print(arr)

#2
import numpy as np
arr = np.random.rand(5)
print(arr)

#3
import numpy as np
x = np.array([10, 20, 30, 40])
print(np.random.choice(x))

#4
import numpy as np
arr2d = np.random.randint(1, 100, size=(2, 3))
print(arr2d)

#5
import numpy as np
print(np.random.randint(5, 15, size=4))
print(np.random.rand(2, 2))
print(np.random.choice([100, 200, 300]))

#6
import numpy as np
evens = np.random.choice([2, 4, 6, 8, 10], size=3)
print("Random even numbers:", evens)

#7
import numpy as np
floats = np.random.rand(3, 3)
print("3x3 Random float matrix:\n", floats)

#8
import numpy as np
np.random.seed(42)
print(np.random.randint(1, 100, 5))  
