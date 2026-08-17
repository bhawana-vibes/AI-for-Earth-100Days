import numpy as np
temps =  np.array([10,20,30])
#print("avg tampertaure:" , np.mean(temps))
new_temps = temps +5
print(new_temps)
print(np.max(new_temps))
print(np.min(new_temps))
hot_temps = temps[temps>15]
print(hot_temps)