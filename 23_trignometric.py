#Basic Trig Functions in Radians

import numpy as np
angles = np.array([0, np.pi/2, np.pi])  
print("Sine:", np.sin(angles))     
print("Cosine:", np.cos(angles))   
print("Tangent:", np.tan(angles))  

#Convert Degrees → Radians

import numpy as np
degrees = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(degrees)
print("Sine of Degrees:", np.sin(radians))

#Inverse Trig Functions

import numpy as np
values = np.array([0, 0.5, 1])
print("arcsin:", np.arcsin(values))  
print("Degrees:", np.rad2deg(np.arcsin(values)))  

#Angle Sweep (0° to 180°)

import numpy as np
degrees = np.arange(0, 181, 30)
radians = np.deg2rad(degrees)
sines = np.sin(radians)
print("Degrees :", degrees)
print("Sines   :", np.round(sines, 3))

#Tangent Curve Trap (90° issue)

import numpy as np
angles_deg = np.array([0, 45, 89, 90])
angles_rad = np.deg2rad(angles_deg)
print("Tan values:", np.tan(angles_rad))

#Inverse Cosine (cos⁻¹)

import numpy as np
cos_vals = np.array([1, 0.5, 0, -1])
angles_rad = np.arccos(cos_vals)
angles_deg = np.rad2deg(angles_rad)
print("Cosine Values  :", cos_vals)
print("Angles in Degs :", np.round(angles_deg, 2))
