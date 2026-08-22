stu= [
    {"name": "Aman", "marks": 80},
    {"name": "Pooja", "marks": 95},
    {"name": "Rohan", "marks": 60}
]
count = 0
for s in stu:
    if s["marks"]>70:
        count = count+1
        print(s["marks"])
print("total count:", count)