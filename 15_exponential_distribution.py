#Real Examples


#Phone Call Timing (avg 10 min)

import numpy as np
calls = np.random.exponential(scale=10, size=6)
print("Time between calls (minutes):", calls)

#Light Bulb Failure Time (in hours)

import numpy as np
failures = np.random.exponential(1000, 5)
print("Bulb failure after hours:", failures)

#Time between customers at restaurant

import numpy as np
customers = np.random.exponential(8, 7)
print("Minutes between customer arrivals:", customers)

#Server Request Interval

import numpy as np
requests = np.random.exponential(2, 10)
print("Time between API requests (sec):", requests)

#Recharge Wait Time (in minutes)

import numpy as np
recharge_wait = np.random.exponential(scale=5, size=6)
print("Recharge wait times (min):", recharge_wait)

#Time to Detect Security Breach

import numpy as np
breach_time = np.random.exponential(72, 5)
print("Hours to detect security breach:", breach_time)

#Train Arrival Gaps (in minutes)

import numpy as np
train_gap = np.random.exponential(15, 7)
print("Train arrival intervals:", train_gap)

#Waiting Time for Job Interview Call

import numpy as np
wait_call = np.random.exponential(4, 10)
print("Days to receive interview call:", wait_call)
