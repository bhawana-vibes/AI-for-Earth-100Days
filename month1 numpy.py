import numpy as np
marks_list = [70, 80, 90, 60]
marks_arr = np.array(marks_list)
print(marks_arr)
grace_marks = marks_arr+5
print(grace_marks)
print("Average (Mean):", np.mean(marks_arr))
print("Max Marks:", np.max(marks_arr))
print("Min Marks:", np.min(marks_arr))
print("Total Sum:", np.sum(marks_arr))