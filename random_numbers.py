
#%%

# Import the NumPy module.
import numpy as np
import random

# Import timeit.
import timeit

#%%
random.randint(-90,90)

#%%
random.random()

#%%

# generate ramdom latitudes
x = 1

latitudes = []
while x < 11:
    random_lat = random.randint(-90, 90) + random.random()
    latitudes.append(random_lat)
    x += 1
    
print(latitudes)

#%%
# generate ramdom latitudes
y = 1

longitudes = []
while y < 11:
    random_long = random.randint(-90, 90) + random.random()
    longitudes.append(random_long)
    y += 1
    
print(longitudes)

#%%
np.random.uniform(-90.000, 90.000)

#%%
np.random.uniform(-90.000, 90.000, size=50)

#%%
%timeit np.random.uniform(-90.000, 90.000, size=1500)
# np.random.uniform(-90.000, 90.000, size=1500)

# %%
def latitudes(size):
    latitudes = []
    x = 0
    while x < (size):
        random_lat = random.randint(-90, 90) + random.random()
        latitudes.append(random_lat)
        x += 1
    return latitudes
# Call the function with 1500. 
%timeit latitudes(1500)

# %%
