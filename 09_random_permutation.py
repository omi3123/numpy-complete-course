#1
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
shuffled = np.random.permutation(arr)
print("Original:", arr)
print("Shuffled:", shuffled)  

#2
import numpy as np
arr2d = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
shuffled_rows = np.random.permutation(arr2d)
print(shuffled_rows)

#3
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffled (in-place):", arr)

#REAL WORLD ML EXAMPLE
import numpy as np
features = np.array([[1, 2], [3, 4], [5, 6]])
labels = np.array([0, 1, 0])
indices = np.random.permutation(len(features))
shuffled_features = features[indices]
shuffled_labels = labels[indices]
# print(shuffled_features)
# print(shuffled_labels)
print(labels)
print(indices)

#REAL WORLD STUDENT GRADE PREDICTION 
import numpy as np
features = np.array([[80, 90], [30, 20], [70, 65]])
labels   = np.array([1, 0, 1])
indices = np.random.permutation(len(features))
shuffled_features = features[indices]
shuffled_labels = labels[indices]
print("Shuffled Student Marks:\n", shuffled_features)
print("Shuffled Results (Pass=1, Fail=0):", shuffled_labels)

#REAL WORLD MEDICAL DIAGNOSIS
import numpy as np
features = np.array([[4.1, 2.3], [6.5, 3.8], [3.9, 1.2]])
labels   = np.array([0, 1, 0])
indices = np.random.permutation(len(features))
shuffled_features = features[indices]
shuffled_labels = labels[indices]
print("Shuffled Test Results:\n", shuffled_features)
print("Shuffled Cancer Labels (1=Cancer):", shuffled_labels)

#REAL WORLD EAMIL SPAM DETECTION
import numpy as np
features = np.array([[1, 0, 5], [0, 1, 1], [1, 1, 3]])  
labels   = np.array([1, 0, 1])
indices = np.random.permutation(len(features))
shuffled_features = features[indices]
shuffled_labels = labels[indices]
print("Shuffled Email Features:\n", shuffled_features)
print("Shuffled Spam Labels (1=Spam):", shuffled_labels)

#REAL WORLD LOAN APPROVAL
import numpy as np
features = np.array([[50000, 700], [20000, 400], [65000, 800]]) 
labels   = np.array([1, 0, 1]) 
indices = np.random.permutation(len(features))
shuffled_features = features[indices]
shuffled_labels = labels[indices]
print("Shuffled Loan Applications:\n", shuffled_features)
print("Shuffled Loan Labels (1=Approved):", shuffled_labels)

#REAL WORLD IMAGE CLASSIFICTAION
import numpy as np
features = np.array([[120, 130, 110], [200, 190, 180], [100, 140, 160]])
labels   = np.array([0, 1, 0])
indices = np.random.permutation(len(features))
shuffled_features = features[indices]
shuffled_labels = labels[indices]
print("Shuffled Image Features:\n", shuffled_features)
print("Shuffled Labels (0=Cat, 1=Dog):", shuffled_labels)
