#1
import numpy as np
data = np.random.normal(loc=50, scale=10, size=10)
print(data)

#2
import numpy as np
data = np.random.normal(100, 20, 5)
print(data)

#3
import numpy as np
data = np.random.normal(0, 1, 10)
print(data)

#4
import numpy as np
data = np.random.normal(100, 15, 1000)
print("Mean  :", round(np.mean(data), 2))
print("StdDev:", round(np.std(data), 2))

#REAL WORLD EXAMPLES

#Student Exam Scores:
import numpy as np
scores = np.random.normal(loc=70, scale=10, size=20)
print("Exam Scores:\n", scores)

#Human Heights (in cm)
import numpy as np
heights = np.random.normal(loc=170, scale=7, size=10)
print("Heights (cm):\n", heights)

#Blood Pressure (Systolic)
import numpy as np
bp = np.random.normal(120, 12, 15)
print("Blood Pressure (Systolic):\n", bp)

#IQ Scores
import numpy as np
iq = np.random.normal(100, 15, 12)
print("IQ Scores:\n", iq)
