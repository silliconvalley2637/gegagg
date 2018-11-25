person_salary=[]
p1={
   "Name": "Huy",
   "Role": "Waiter",
   "Hours": 12,
   "Salary per hour($)": 0.8,
}
p2={
    "Name": "Tung",
    "Role": "Cook",
    "Hours": 24,
    "Salary per hour($)": 1.5,
}
p3={
    "Name": "M.Duc",
    "Role": "Manager",
    "Hours": 20,
    "Salary per hour($)": 2,
}
person_salary=[p1,p2,p3]
p4={
    "Name": "H.Duc",
    "Role": "Waiter",
    "Hours": 12,
    "Salary per hour($)": 0.9,
}
p5={
    "Name": "Don",
    "Role": "Waiter",
    "Hours": 14,
    "Salary per hour($)": 0.7,
}
person_salary.append(p4)
person_salary.append(p5)
print(person_salary[2]["Salary per hour($)"])
person_salary[0]["Name"]="Huyen"
person_salary[0]["Role"]="Waitress"
person_salary[0]["Hours"] +=2 
person_salary[0]["Salary per hour($)"] +=0.2
del person_salary[4]
for p in person_salary:
    print(p)
    print(p["Name"])
    print(p["Role"])
    print(p["Hours"])
    print(p["Salary per hour($)"])
print(person_salary)