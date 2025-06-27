# import numpy as np
# x = np.array([10, 20, 30])
# print(x)

# import numpy as np
# arr=np.array([1,2,3])
# arr2d=np.array([[1,2],[3,4],[5,6]])
# print(arr)
# print(arr2d)

# import numpy as np
# arr_2d = np.array([[10, 20], [30, 40], [50, 60]])
# print(arr_2d)

# import numpy as np
# zero_arr=np.zeros((2,2))
# print(zero_arr)

# import numpy as np
# zero_arr=np.zeros((2,2,3))
# print(zero_arr)

#array of ones
# import numpy as np
# ones = np.ones((3,2))
# print(ones)

# import numpy as np
# ones = np.ones((3,2,2))
# print(ones)

#array of empty
# import numpy as np
# empty = np.empty((2,2))
# print(empty)

# import numpy as np
# empty = np.empty((2,2,2))
# print(empty)

#using arange(array range)
# import numpy as np
# arr = np.arange(0, 10, 2) 
# print(arr)

#using linespace
# import numpy as np
# arr = np.linspace(0, 1, 5)
# print(arr)  

#identity matrix
# import numpy as np
# i = np.eye(3)
# print(i)

#combo
# import numpy as np

# a = np.zeros((2, 4))
# b = np.ones((3, 3))
# c = np.arange(5, 15, 3)
# d = np.eye(4)

# print(a)
# print(b)
# print(c)
# print(d)



#array indexing starts from here

#1D
# import numpy as np
# arr = np.array([10, 20, 30, 40])
# print(arr[0])  
# print(arr[2])  

#2D
# import numpy as np
# arr2d = np.array([[5, 10, 15],
#                   [20, 25, 30]])
# print(arr2d[0, 0])  
# print(arr2d[1, 2])  

#Negative in 1D
# import numpy as np
# arr = np.array([100, 200, 300, 400])
# print(arr[-1])  
# print(arr[-2])  

# #negative 2D
# import numpy as np
# arr2d = np.array([[1, 2], [3, 4]])
# print(arr2d[-1, -1])  

#combo
# import numpy as np

# x = np.array([[100, 200, 300],
#               [400, 500, 600]])

# print(x[0, 1])     
# print(x[1, -1])    
# print(x[-2, -3])   




#array slicing starts from here


# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[1:4])  
# print(arr[:3])   
# print(arr[2:])    

# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[-3:-1])  

# import numpy as np

# x = np.array([
#     [ 1,  2,  3,  4],  
#     [ 5,  6,  7,  8],  
#     [ 9, 10, 11, 12],   
#     [13, 14, 15, 16]     
# ])
# print(x[0:2, 0:2])
# print(x[2:, 2:])


# import numpy as np
# x = np.array([
#     [ 1,  2,  3,  4],  
#     [ 5,  6,  7,  8],  
#     [ 9, 10, 11, 12],   
#     [13, 14, 15, 16]     
# ])
# print(x[1:3, 1:3])
# print(x[:2, 2:])
# print(x[-2:, :2])




#datatypes in numpy starts from here


# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr.dtype)  

# import numpy as np
# arr = np.array([1, 2, 3], dtype='float')
# print(arr)
# print(arr.dtype)  



#astype() changes the types
# import numpy as np
# arr = np.array([1.1, 2.2, 3.3])
# new_arr = arr.astype('int')
# print(new_arr)       
# print(new_arr.dtype)  

# import numpy as np
# a = np.array([5, 10, 15])
# b = np.array([True, False, True])
# c = np.array(['apple', 'banana', 'cherry'])
# d = a.astype('float')
# e = b.astype('int')
# print(a.dtype)
# print(b.dtype)
# print(c.dtype)
# print(d)
# print(e)






#copy vs view starts from here

# import numpy as np
# arr = np.array([10, 20, 30])
# copy_arr = arr.copy()
# copy_arr[0] = 99
# print("Original:", arr)     
# print("Copy:", copy_arr)   
# print(copy_arr.base) 

# import numpy as np
# arr = np.array([1, 2, 3])
# view_arr = arr.view()
# view_arr[1] = 99
# print("Original:", arr)     
# print("View:", view_arr)   
# print(view_arr.base) 

# import numpy as np
# x = np.array([100, 200, 300])
# a = x.copy()
# b = x.view()
# a[0] = 111
# b[1] = 222
# print(x)
# print(a)
# print(b)





#array shape starts from here

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)   

# import numpy as np
# a = np.array([10, 20, 30, 40])
# print(a.shape)   

# import numpy as np
# b = np.array([1, 2, 3, 4, 5, 6])
# reshaped = b.reshape(2, 3)  
# print(reshaped)

# import numpy as np
# c = np.array([10, 20, 30, 40, 50, 60])
# print(c.reshape(3, -1))   

# import numpy as np
# arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(arr3d.shape) 

# combo
# import numpy as np
# x = np.array([1, 2, 3, 4, 5, 6])
# a = x.reshape(3, 2)
# b = x.reshape(2, 3)
# c = x.reshape(-1, 1)
# print(a.shape)   
# print(b.shape)   
# print(c.shape)   


import numpy as np
# a = np.array([10, 20, 30, 40, 50, 60])
# a2d = a.reshape(2, 3)   
# print(a2d)

# import numpy as np
# b = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# b3d = b.reshape(2, 2, 2)
# print(b3d)

# import numpy as np
# d = np.array([1, 2, 3, 4, 5, 6])
# print(d.reshape(-1, 2))  

# import numpy as np
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(x.reshape(2, 4).shape)   
# print(x.reshape(4, 2).shape)  
# print(x.reshape(-1, 1).shape)   
# print(x.reshape(2, 2, 2).shape)  




# Random starts from here

# import numpy as np
# arr = np.random.randint(0, 10, size=5)
# print(arr)

# import numpy as np
# arr = np.random.rand(5)
# print(arr)

# import numpy as np
# x = np.array([10, 20, 30, 40])
# print(np.random.choice(x))

# import numpy as np
# arr2d = np.random.randint(1, 100, size=(2, 3))
# print(arr2d)

# import numpy as np
# print(np.random.randint(5, 15, size=4))
# print(np.random.rand(2, 2))
# print(np.random.choice([100, 200, 300]))

# import numpy as np
# np.random.seed(42)
# print(np.random.randint(1, 100, 5))  

# Generate 1000 values from a normal distribution

# import numpy as np
# data = np.random.normal(loc=50, scale=10, size=1000)
# print(data[:5]) 

# import numpy as np
# a = np.random.normal(0, 1, 5)    
# b = np.random.normal(10, 2, 3)   
# c = np.random.normal(loc=100, scale=20, size=2)
# print(a)
# print(b)
# print(c)

# import numpy as np
# x = np.random.normal(0, 1, 10) 
# print("Normal dist sample:", x)

# import numpy as np
# x = np.random.normal(50, 15, 8)  
# print("Spread out values:", x)

# import numpy as np
# samples = np.random.normal(0, 1, 1000)
# print(samples)

# import numpy as np
# a = np.random.normal(0, 1, 1000)   
# b = np.random.normal(0, 5, 1000)   
# print("Mean of a:", np.mean(a))
# print("Mean of b:", np.mean(b))




#Random Permutation starts from here



# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# shuffled = np.random.permutation(arr)
# print("Original:", arr)
# print("Shuffled:", shuffled)  

# import numpy as np
# arr2d = np.array([[1, 2],
#                   [3, 4],
#                   [5, 6]])
# shuffled_rows = np.random.permutation(arr2d)
# print(shuffled_rows)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# np.random.shuffle(arr)
# print("Shuffled (in-place):", arr)

# REAL WORLD ML EXAMPLE
# import numpy as np
# features = np.array([[1, 2], [3, 4], [5, 6]])
# labels = np.array([0, 1, 0])
# indices = np.random.permutation(len(features))
# shuffled_features = features[indices]
# shuffled_labels = labels[indices]
# # print(shuffled_features)
# # print(shuffled_labels)
# print(labels)
# print(indices)

# REAL WORLD STUDENT GRADE PREDICTION 
# import numpy as np
# features = np.array([[80, 90], [30, 20], [70, 65]])
# labels   = np.array([1, 0, 1])
# indices = np.random.permutation(len(features))
# shuffled_features = features[indices]
# shuffled_labels = labels[indices]
# print("Shuffled Student Marks:\n", shuffled_features)
# print("Shuffled Results (Pass=1, Fail=0):", shuffled_labels)

# REAL WORLD MEDICAL DIAGNOSIS
# import numpy as np
# features = np.array([[4.1, 2.3], [6.5, 3.8], [3.9, 1.2]])
# labels   = np.array([0, 1, 0])
# indices = np.random.permutation(len(features))
# shuffled_features = features[indices]
# shuffled_labels = labels[indices]
# print("Shuffled Test Results:\n", shuffled_features)
# print("Shuffled Cancer Labels (1=Cancer):", shuffled_labels)

# REAL WORLD EAMIL SPAM DETECTION
# import numpy as np
# features = np.array([[1, 0, 5], [0, 1, 1], [1, 1, 3]])  
# labels   = np.array([1, 0, 1])
# indices = np.random.permutation(len(features))
# shuffled_features = features[indices]
# shuffled_labels = labels[indices]
# print("Shuffled Email Features:\n", shuffled_features)
# print("Shuffled Spam Labels (1=Spam):", shuffled_labels)

# REAL WORLD LOAN APPROVAL
# import numpy as np
# features = np.array([[50000, 700], [20000, 400], [65000, 800]]) 
# labels   = np.array([1, 0, 1]) 
# indices = np.random.permutation(len(features))
# shuffled_features = features[indices]
# shuffled_labels = labels[indices]
# print("Shuffled Loan Applications:\n", shuffled_features)
# print("Shuffled Loan Labels (1=Approved):", shuffled_labels)

# REAL WORLD IMAGE CLASSIFICTAION
# import numpy as np
# features = np.array([[120, 130, 110], [200, 190, 180], [100, 140, 160]])
# labels   = np.array([0, 1, 0])
# indices = np.random.permutation(len(features))
# shuffled_features = features[indices]
# shuffled_labels = labels[indices]
# print("Shuffled Image Features:\n", shuffled_features)
# print("Shuffled Labels (0=Cat, 1=Dog):", shuffled_labels)






#NORMAL DISTRIBUTION starts from here


# import numpy as np
# data = np.random.normal(loc=50, scale=10, size=10)
# print(data)

# import numpy as np
# data = np.random.normal(100, 20, 5)
# print(data)

# import numpy as np
# data = np.random.normal(0, 1, 10)
# print(data)

# import numpy as np
# data = np.random.normal(100, 15, 1000)
# print("Mean  :", round(np.mean(data), 2))
# print("StdDev:", round(np.std(data), 2))



#Bionomial distribution starts from here:

#Real World Examples

# #Toss a Coin 10 times, do it 5 times
# import numpy as np
# results = np.random.binomial(n=10, p=0.5, size=5)
# print("Heads in each experiment:", results)

# #Email Delivery (n=20, p=0.9)
# import numpy as np
# emails = np.random.binomial(n=20, p=0.9, size=5)
# print("Delivered emails in each batch:", emails)

# #Student MCQs
# import numpy as np
# mcq = np.random.binomial(n=5, p=0.6, size=10)
# print("Correct answers in 10 students:", mcq)

# #Quality Check
# import numpy as np
# items = np.random.binomial(n=50, p=0.95, size=4)
# print("Items passed in 4 batches:", items)

# #Cricket — Batsman hits 4s
# import numpy as np
# fours = np.random.binomial(n=6, p=0.3, size=10)
# print("4s hit by batsman in 10 overs:", fours)

# #Car Engine Start Attempt
# import numpy as np
# starts = np.random.binomial(n=3, p=0.8, size=6)
# print("Successful engine starts:", starts)

# #Light Bulb Test (Working/Not)
# import numpy as np
# bulbs = np.random.binomial(n=100, p=0.96, size=5)
# print("Working bulbs out of 100:", bulbs)

# #Voting — Agree/Disagree Survey
# import numpy as np
# votes = np.random.binomial(n=30, p=0.7, size=7)
# print("People who agree in 7 surveys:", votes)



# #Real World Examples

# #Call Center receives 5 calls per hour

# import numpy as np
# calls = np.random.poisson(lam=5, size=10)
# print("Calls received each hour:", calls)

# #Tyre punctures per week
# import numpy as np
# punctures = np.random.poisson(2, 7)
# print("Tyre punctures per week:", punctures)

# #Accidents at traffic signal
# import numpy as np
# accidents = np.random.poisson(3, 5)
# print("Daily accidents (5 days):", accidents)

# #Server Crashes per Day
# import numpy as np
# crashes = np.random.poisson(1, 10)
# print("Crashes per day (10 days):", crashes)

# #Website Visitors per Minute
# import numpy as np
# visitors = np.random.poisson(lam=12, size=6)
# print("Website visitors per minute (6 mins):", visitors)

# #Misprints in a Book
# import numpy as np
# misprints = np.random.poisson(lam=1, size=10)
# print("Misprints per page (10 pages):", misprints)

# #Lightning Strikes per Month
# import numpy as np
# strikes = np.random.poisson(0.3, 12)
# print("Lightning strikes per month (1 year):", strikes)

# #Software Bugs Found Daily
# import numpy as np
# bugs = np.random.poisson(4, 7)
# print("Bugs found each day (1 week):", bugs)


# #Real Examples


# #Random float between 0 and 1

# import numpy as np
# values = np.random.uniform(0, 1, 5)
# print("Random values:", values)

# #Random marks between 50 and 100

# import numpy as np
# marks = np.random.uniform(50, 100, 10)
# print("Random marks:", marks)

# #Temperature between 30°C and 45°C

# import numpy as np
# temps = np.random.uniform(30, 45, 7)
# print("Temperature readings (7 days):", temps)

# #Game - Random Speed Generator

# import numpy as np
# speed = np.random.uniform(60, 120, 3)
# print("Car speed (km/h):", speed)

# #Random Discount Percentage (10% to 50%)

# import numpy as np
# discounts = np.random.uniform(10, 50, 6)
# print("Discounts offered:", discounts)

# #Random Time Taken to Complete Task (in minutes)

# import numpy as np
# times = np.random.uniform(20, 60, 5)
# print("Task completion times (minutes):", times)

# #Game Level - Random Spawn Location (X-axis)

# import numpy as np
# x_locations = np.random.uniform(-100, 100, 8)
# print("Enemy spawn locations (x-axis):", x_locations)

# #Random Password Strength Score (1 to 10)

# import numpy as np
# scores = np.random.uniform(1, 10, 4)
# print("Password strength scores:", scores)







#Real Examples


#Simple Logistic Distribution

# import numpy as np
# data = np.random.logistic(loc=0, scale=1, size=10)
# print("Logistic values:", data)

# #Logistic with different mean & scale

# import numpy as np
# data = np.random.logistic(50, 5, 7)
# print("Centered around 50, sharpness 5:", data)

# #Simulate population tendency

# import numpy as np
# pop = np.random.logistic(1000, 100, 6)
# print("Population predictions:", pop)

# #ML use-case simulation (0–1 activation values)

# import numpy as np
# ml_values = np.random.logistic(0.5, 0.1, 12)
# print("Logistic ML scores:", ml_values)

# Delivery Time Estimation (in minutes)

# import numpy as np
# delivery_times = np.random.logistic(loc=30, scale=5, size=6)
# print("Delivery times (minutes):", delivery_times)

# #Logistic Score for Pass/Fail Test

# import numpy as np
# scores = np.random.logistic(loc=50, scale=10, size=8)
# print("Test scores:", scores)

# #Growth Rate of Mobile App Users

# import numpy as np
# growth = np.random.logistic(loc=10000, scale=2000, size=5)
# print("User growth predictions:", growth)

# #Decision Confidence (0 to 1)

# import numpy as np
# confidence = np.random.logistic(loc=0.5, scale=0.1, size=10)
# print("Model decision confidence values:", confidence)





# #Real Examples


# #Phone Call Timing (avg 10 min)

# import numpy as np
# calls = np.random.exponential(scale=10, size=6)
# print("Time between calls (minutes):", calls)

# #Light Bulb Failure Time (in hours)

# import numpy as np
# failures = np.random.exponential(1000, 5)
# print("Bulb failure after hours:", failures)

# #Time between customers at restaurant

# import numpy as np
# customers = np.random.exponential(8, 7)
# print("Minutes between customer arrivals:", customers)

# #Server Request Interval

# import numpy as np
# requests = np.random.exponential(2, 10)
# print("Time between API requests (sec):", requests)

# #Recharge Wait Time (in minutes)

# import numpy as np
# recharge_wait = np.random.exponential(scale=5, size=6)
# print("Recharge wait times (min):", recharge_wait)

# #Time to Detect Security Breach

# import numpy as np
# breach_time = np.random.exponential(72, 5)
# print("Hours to detect security breach:", breach_time)

# #Train Arrival Gaps (in minutes)

# import numpy as np
# train_gap = np.random.exponential(15, 7)
# print("Train arrival intervals:", train_gap)

# #Waiting Time for Job Interview Call

# import numpy as np
# wait_call = np.random.exponential(4, 10)
# print("Days to receive interview call:", wait_call)



#Without using ufuncs

# a = [1, 2, 3]
# b = [4, 5, 6]
# result = []
# for i in range(len(a)):
#     result.append(a[i] + b[i])
# print(result)


#Using with ufuncs

# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.add(a, b))

#Without using ufuncs

# a = [2, 4, 6]
# b = [1, 3, 5]
# result = []
# for i in range(len(a)):
#     result.append(a[i] * b[i])
# print(result) 

# #Using with ufuncs

# import numpy as np
# a = np.array([2, 4, 6])
# b = np.array([1, 3, 5])
# print(np.multiply(a, b)) 

# #Without using ufuncs

# a = [10, 20, 30]
# b = [2, 5, 3]
# result = []
# for i in range(len(a)):
#     result.append(a[i] / b[i])
# print(result) 

# #Using with ufuncs

# import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([2, 5, 3])
# print(np.divide(a, b))









# #Custom Add Function

# import numpy as np
# def my_add(x, y):
#     return x + y
# add_ufunc = np.frompyfunc(my_add, 2, 1)
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# print(add_ufunc(a, b))  

# #Custom String Merge Function

# def merge_strings(x, y):
#     return str(x) + "-" + str(y)
# merge_func = np.frompyfunc(merge_strings, 2, 1)
# a = np.array(["Umair", "Ali", "Zain"])
# b = np.array(["01", "02", "03"])
# print(merge_func(a, b)) 

# #Add 3 Arrays using Custom ufunc

# import numpy as np
# def my_add3(x, y, z):
#     return x + y + z
# add3_ufunc = np.frompyfunc(my_add3, 3, 1)
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# c = np.array([5, 5, 5])
# print(add3_ufunc(a, b, c))




# #Total sum of all elements

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(np.sum(arr)) 

# #Sum column-wise

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(np.sum(arr, axis=0)) 

# # Sum row-wise

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(np.sum(arr, axis=1)) 

# #Product of all elements

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(np.prod(arr))

# #Product column-wise

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(np.prod(arr, axis=0)) 

# #Product row-wise

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])
# print(np.prod(arr, axis=1))










# #Basic difference

# import numpy as np
# a = np.array([10, 20, 25, 40])
# print(np.diff(a))

# #2nd order difference (n=2)

# import numpy as np
# a = np.array([10, 20, 25, 40])
# print(np.diff(a, n=2))

# #Differences in 2D array (row-wise flatten)

# import numpy as np
# x = np.array([[5, 10, 15],
#               [20, 25, 30]])
# print(np.diff(x))

# #Temperature Change (1st Order)

# import numpy as np
# temps = np.array([22, 25, 21, 26, 30])
# change = np.diff(temps)
# print(change)

# #2nd Order – Change in speed (acceleration)

# import numpy as np
# speeds = np.array([0, 10, 25, 55])
# first_diff = np.diff(speeds)
# second_diff = np.diff(speeds, n=2)
# print("1st Order:", first_diff)   
# print("2nd Order:", second_diff)    

# #Difference in repeated pattern

# import numpy as np
# x = np.array([5, 5, 5, 10, 10, 15])
# print(np.diff(x))  








# #Basic LCM

# import numpy as np
# print(np.lcm(4, 6))

# #LCM of arrays

# import numpy as np
# a = np.array([3, 6, 9])
# b = np.array([5, 4, 12])
# print(np.lcm(a, b))  

# #Use with broadcasting

# import numpy as np
# x = np.array([2, 4])
# y = 6
# print(np.lcm(x, y))  

# #LCM of Two Scalars

# import numpy as np
# print(np.lcm(8, 12))

# #LCM of Two Arrays (Same Shape)

# import numpy as np
# a = np.array([2, 4, 6])
# b = np.array([3, 5, 9])
# print(np.lcm(a, b))  

# #LCM of Array with Scalar (Broadcasting)

# import numpy as np
# arr = np.array([3, 6, 9])
# value = 12
# print(np.lcm(arr, value)) 

# #2D and 1D Array (Matrix-style Broadcasting)

# import numpy as np
# x = np.array([[2], [4], [6]])
# y = np.array([3, 6])
# print(np.lcm(x, y))











# #GCD of Two Numbers

# import numpy as np
# print(np.gcd(12, 18))

# #GCD of Two Arrays (Same shape)

# import numpy as np
# a = np.array([12, 15, 21])
# b = np.array([8, 25, 14])
# print(np.gcd(a, b))  

# #GCD with Scalar (Broadcasting)

# import numpy as np
# arr = np.array([10, 20, 30])
# val = 5
# print(np.gcd(arr, val))

# #2D Array with Broadcasting

# import numpy as np
# x = np.array([[10], [20], [30]])
# y = np.array([5, 10])
# print(np.gcd(x, y))

# #GCD in Matrix Broadcasting Style

# import numpy as np
# x = np.array([[18], [30]])
# y = np.array([12, 21])
# print(np.gcd(x, y))

# #GCD of a List with a Common Number

# import numpy as np
# arr = np.array([100, 150, 200])
# common = 50
# print(np.gcd(arr, common))

# #Simplifying Fractions

# import numpy as np
# numerators = np.array([8, 15, 24])
# denominators = np.array([12, 25, 36])
# gcd_values = np.gcd(numerators, denominators)
# simplified_numerators = numerators // gcd_values
# simplified_denominators = denominators // gcd_values
# print("Simplified Fractions:")
# for n, d in zip(simplified_numerators, simplified_denominators):
#     print(f"{n}/{d}")
















#Basic Trig Functions in Radians

# import numpy as np
# angles = np.array([0, np.pi/2, np.pi])  
# print("Sine:", np.sin(angles))     
# print("Cosine:", np.cos(angles))   
# print("Tangent:", np.tan(angles))  

#Convert Degrees → Radians

# import numpy as np
# degrees = np.array([0, 30, 45, 60, 90])
# radians = np.deg2rad(degrees)
# print("Sine of Degrees:", np.sin(radians))

# #nverse Trig Functions

# import numpy as np
# values = np.array([0, 0.5, 1])
# print("arcsin:", np.arcsin(values))  
# print("Degrees:", np.rad2deg(np.arcsin(values)))  

#Angle Sweep (0° to 180°)

# import numpy as np
# degrees = np.arange(0, 181, 30)
# radians = np.deg2rad(degrees)
# sines = np.sin(radians)
# print("Degrees :", degrees)
# print("Sines   :", np.round(sines, 3))

#Tangent Curve Trap (90° issue)

# import numpy as np
# angles_deg = np.array([0, 45, 89, 90])
# angles_rad = np.deg2rad(angles_deg)
# print("Tan values:", np.tan(angles_rad))

# #Inverse Cosine (cos⁻¹)

# import numpy as np
# cos_vals = np.array([1, 0.5, 0, -1])
# angles_rad = np.arccos(cos_vals)
# angles_deg = np.rad2deg(angles_rad)
# print("Cosine Values  :", cos_vals)
# print("Angles in Degs :", np.round(angles_deg, 2))
