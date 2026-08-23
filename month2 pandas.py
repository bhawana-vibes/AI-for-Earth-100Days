import pandas as pd
data = {
    "Name": ["Aman", "Pooja", "Rohan", "Sneha"],
    "Branch": ["CSE", "IT", "CSE", "ECE"],
    "Marks": [80, 95, 60, 88]
}
df = pd.DataFrame(data)
print(df)
print(df["Marks"])
print("highest marks:" , df[df["Marks"]>75])
df["Final_Marks"] = df["Marks"] + 5
print(df)
print(df.groupby("Branch")["Marks"].mean())
print("stu marks:",df[df["Marks"] < 70])
print("head:" , df.head())
print("info:" , df.info())
print("shape:" , df.shape)
branch_avg = df.groupby("Branch")["Marks"].mean()
print("averge:" , branch_avg)