import pandas as pd
data = {
    "Name": ["Aman", "Pooja", "Rohan", "Sneha"],
    "Branch": ["CSE", "IT", "CSE", "ECE"],
    "Marks": [80, 95, 60, 88]
}
df = pd.DataFrame(data)
print(df)