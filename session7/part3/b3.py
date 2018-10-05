n=int(input("pick a month"))
if n in (1,3,5,7,8,10,12):
    print("This month has 31 days")
elif n in (4,6,9,11):
    print("This month has 30 days")
elif n==2:
    print("This month has 28 or 29 days")
else:
    print("Are u a bitch")