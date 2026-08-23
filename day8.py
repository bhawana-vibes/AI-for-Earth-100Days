import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
data = [70, 72, 70, 74, 70]
print("Mean:" , np.mean(data))
print("Mean:", np.mean(data))               
print("Median:", np.median(data))                 
print("Mode:", stats.mode(data, keepdims=True)[0][0])
print("variance:" , np.var(data))
print("standard variance:" , np.std(data))

salaries = pd.Series([25, 28, 30, 27, 29, 31, 26, 500])
q1 = salaries.quantile(0.25)
q3 = salaries.quantile(0.75)
iqr = q3-q1
max_limit =  q1+(1.5*iqr)
clean_data = salaries[salaries <= max_limit]
print(clean_data)

heights = np.random.normal(loc=170, scale=10, size=10000)
plt.hist(heights, bins=30, edgecolor="black")
sns.histplot(heights, kde=True, color="skyblue", stat="density")
plt.title("Smooth Bell Curve (Normal Distribution)")
plt.xlabel("Height (cm)")
plt.ylabel("Count")
plt.show()


