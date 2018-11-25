person_salary=[]
p1={
   "Name": "Huy",
   "Role": "Waiter",
   "Hours": 12,
   "Salary per hour($)": 0.8,
   "Salary per month($)": 0.8*12*30,
}
p2={
    "Name": "Tung",
    "Role": "Cook",
    "Hours": 24,
    "Salary per hour($)": 1.5,
    "Salary per month($)": 1.5*24*30,
}
p3={
    "Name": "M.Duc",
    "Role": "Manager",
    "Hours": 20,
    "Salary per hour($)": 2,
    "Salary per month($)": 2*20*30,
}
person_salary=[p1,p2,p3]
p4={
    "Name": "H.Duc",
    "Role": "Waiter",
    "Hours": 12,
    "Salary per hour($)": 0.9,
    "Salary per month($)": 0.9*12*30,
}
p5={
    "Name": "Don",
    "Role": "Waiter",
    "Hours": 14,
    "Salary per hour($)": 0.7,
    "Salary per month($)": 0.7*14*30,
}
person_salary.append(p4)
person_salary.append(p5)
del person_salary[4]
for p in person_salary:
    print(p)
    print(p["Name"])
    print(p["Role"])
    print(p["Hours"])
    print(p["Salary per hour($)"])
    print(p["Salary per month($)"])
print(person_salary)
n=2*20*30+1.5*24*30+2*20*30+0.9*12*30+0.7*14*30
print("Value of all salary is",n)