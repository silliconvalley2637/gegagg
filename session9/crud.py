things=["Harry Potter"," Steph Curry"," Kevin Durant"," Klay Thompson","Draymond Green","AWM"]
m=input("chọn đê ")
if m== "create":
    p=input("create what?")
    things.append(p)
    print(*things, sep = " , ")
elif m== "review":
    for i, thing in enumerate(things):
        print(i, ":", *thing)
elif m== "update":
    p=int(input("which?"))
    replace=input("to?")
    things[p]=replace
    for i, thing in enumerate(things):
        print(i, ":",*thing)
elif m=="delete":
    z=input("choose positon or value")
    if z== "position":
       u=int(input("position?"))
       things.pop(u)
       print(*things, sep= " , ")
    elif z== "value":
        t=input("remove what?")
        things.remove(t)
        print(*things, sep= " , ")
