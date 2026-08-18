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

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.vstack((a,b))
print(result)

result1 = np.hstack((a,b))
print(result1)

clsa = np.array([75, 80, 85])
clsb = np.array([90, 92, 88])
result2 = np.vstack((clsa , clsb))
print(result2)

import numpy as np

Rows: Students (Riya, Aman, Priya)
Columns: Subjects (Maths, Science, English, Hindi)
marks = np.array([
    [85, 78, 92, 88],   
    [56, 62, 58, 60],   
    [95, 90, 89, 94]    
])
print(marks[1, :])
print(np.mean(marks[:, 0]))
print(marks[marks>90])