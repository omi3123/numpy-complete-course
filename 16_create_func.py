#Custom Add Function

import numpy as np
def my_add(x, y):
    return x + y
add_ufunc = np.frompyfunc(my_add, 2, 1)
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(add_ufunc(a, b))  

#Custom String Merge Function

def merge_strings(x, y):
    return str(x) + "-" + str(y)
merge_func = np.frompyfunc(merge_strings, 2, 1)
a = np.array(["Umair", "Ali", "Zain"])
b = np.array(["01", "02", "03"])
print(merge_func(a, b)) 

#Add 3 Arrays using Custom ufunc

import numpy as np
def my_add3(x, y, z):
    return x + y + z
add3_ufunc = np.frompyfunc(my_add3, 3, 1)
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
c = np.array([5, 5, 5])
print(add3_ufunc(a, b, c))

#Check Even or Odd (Single input)

import numpy as np
def even_or_odd(x):
    return "Even" if x % 2 == 0 else "Odd"
check_func = np.frompyfunc(even_or_odd, 1, 1)
nums = np.array([10, 15, 22, 31])
print(check_func(nums))

#Grade Generator (2 inputs: name + marks)

def assign_grade(name, marks):
    grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"
    return name + " → " + grade
grade_func = np.frompyfunc(assign_grade, 2, 1)
names = np.array(["Ali", "Zain", "Umair"])
scores = np.array([92, 80, 65])
print(grade_func(names, scores))
