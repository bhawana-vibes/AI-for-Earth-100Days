stu= [
    {"name": "Aman", "marks": 80},
    {"name": "Pooja", "marks": 95},
    {"name": "Rohan", "marks": 60}
]
count = 0
total_marks =0
total_stu = len(stu)
for s in stu:
    if s["marks"]>70:
        count = count+1
        print(s["marks"])
    total_marks = total_marks +s["marks"]
print(total_marks)
avg = total_marks/ total_stu
print("total avg:" , avg)
print("total count:", count)