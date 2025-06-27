#Real World Examples

#Toss a Coin 10 times, do it 5 times

import numpy as np
results = np.random.binomial(n=10, p=0.5, size=5)
print("Heads in each experiment:", results)

#Email Delivery (n=20, p=0.9)

import numpy as np
emails = np.random.binomial(n=20, p=0.9, size=5)
print("Delivered emails in each batch:", emails)

#Student MCQs

import numpy as np
mcq = np.random.binomial(n=5, p=0.6, size=10)
print("Correct answers in 10 students:", mcq)

#Quality Check

import numpy as np
items = np.random.binomial(n=50, p=0.95, size=4)
print("Items passed in 4 batches:", items)

#Cricket — Batsman hits 4s

import numpy as np
fours = np.random.binomial(n=6, p=0.3, size=10)
print("4s hit by batsman in 10 overs:", fours)

#Car Engine Start Attempt

import numpy as np
starts = np.random.binomial(n=3, p=0.8, size=6)
print("Successful engine starts:", starts)

#Light Bulb Test (Working/Not)

import numpy as np
bulbs = np.random.binomial(n=100, p=0.96, size=5)
print("Working bulbs out of 100:", bulbs)

#Voting — Agree/Disagree Survey

import numpy as np
votes = np.random.binomial(n=30, p=0.7, size=7)
print("People who agree in 7 surveys:", votes)