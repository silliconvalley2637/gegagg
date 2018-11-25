things=["Harry Potter"," Steph Curry"," Kevin Durant"," Klay Thompson","Draymond Green","AWM"]
n=int(input("position?"))
things.pop(n)

print(*things, sep= " , ")