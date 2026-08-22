stu= [
    {"name": "Aman", "marks": 80},
    {"name": "Pooja", "marks": 95},
    {"name": "Rohan", "marks": 60}
]
count = 0
total_marks =0
max_marks = 0
min_marks =100
total_stu = len(stu)
for s in stu:
    if s["marks"]>70:
        count = count+1
        print(s["marks"])
    total_marks = total_marks +s["marks"]
    if s["marks"]>max_marks:
        max_marks = s["marks"]
    if s["marks"]<min_marks:
        min_marks =s["marks"]
print(max_marks)
print(min_marks)
print(total_marks)
avg = total_marks/ total_stu
print("total avg:" , avg)
print("total count:", count)

employees = [
    {"name": "Ananya", "salary": 45000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Kavita", "salary": 92000},
    {"name": "Vikas", "salary": 38000}
]
count = 0
max_salary = 0
for emp in employees:
    if emp["salary"]>50000:
        count = count+1
    if emp["salary"]>max_salary:
         max_salary = emp["salary"]
print(count)
print(max_salary)