#Total sum of all elements

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sum(arr)) 

#Sum column-wise

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sum(arr, axis=0)) 

# Sum row-wise

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sum(arr, axis=1)) 

#Product of all elements

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.prod(arr))

#Product column-wise

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.prod(arr, axis=0)) 

#Product row-wise

import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.prod(arr, axis=1))
