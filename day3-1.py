import numpy as np
temp = np.array([
    [30, 32, 31], 
    [25, 26, 28],   
    [20, 22, 21]
])
print(temp[1,1])
print(temp[2, 2])
grid = temp[0:2 ,0:2]
print(grid)
temps = temp[0:2 , 1: ]
print(temps)