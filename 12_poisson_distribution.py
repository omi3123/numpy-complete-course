#Real World Examples

#Call Center receives 5 calls per hour

import numpy as np
calls = np.random.poisson(lam=5, size=10)
print("Calls received each hour:", calls)

#Tyre punctures per week
import numpy as np
punctures = np.random.poisson(2, 7)
print("Tyre punctures per week:", punctures)

#Accidents at traffic signal
import numpy as np
accidents = np.random.poisson(3, 5)
print("Daily accidents (5 days):", accidents)

#Server Crashes per Day
import numpy as np
crashes = np.random.poisson(1, 10)
print("Crashes per day (10 days):", crashes)

#Website Visitors per Minute
import numpy as np
visitors = np.random.poisson(lam=12, size=6)
print("Website visitors per minute (6 mins):", visitors)

#Misprints in a Book
import numpy as np
misprints = np.random.poisson(lam=1, size=10)
print("Misprints per page (10 pages):", misprints)

#Lightning Strikes per Month
import numpy as np
strikes = np.random.poisson(0.3, 12)
print("Lightning strikes per month (1 year):", strikes)

#Software Bugs Found Daily
import numpy as np
bugs = np.random.poisson(4, 7)
print("Bugs found each day (1 week):", bugs)
