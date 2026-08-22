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


prices = np.array([100, 200, 300])
#grace_prices = prices*2
print("grace_prices:" ,prices*2)

scores = np.array([40, 75, 90, 30, 85])
#high_scores = scores[scores>50]
print("high_scores:" , scores[scores>50])

ages = np.array([12, 25, 17, 30, 15, 40])
print("highest ages:" ,ages[ages >= 18])