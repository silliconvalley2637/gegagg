n=input("key:")
m=input("value:")
person= {
    n : m,
}
print(person)
p=input("create?")
if p == "no" :       
   print("ok")
elif p == "yes" :  
    l=input("create key:")
    j=input("create value:")
    person[l]=j
print(person)

