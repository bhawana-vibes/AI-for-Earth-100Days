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


arr = np.array([10, 20, 30, 40, 50, 60])
grid1 = arr.reshape(2,3)
print(grid1)

flat_arr = grid1.flatten()
print(flat_arr)


data = np.arange(1,13)
grid2 = data.reshape(3,4)
print(grid2)