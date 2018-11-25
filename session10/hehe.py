person={
    "name": "stephen curry",
    "age":"31",
    "occupation": "professional basketball player",
    "team": "golden state warriors",

}
print(person)
m=input("update or create?")
if m=="create":
   l=input("create key:")
   j=input("create value:")
   person[l]=j
elif m=="update":
   o= input("which key?")
   if o in person:
       k=input("to value? ")
       person[o]=k
   elif o not in person:
       u=input("xamlon")
else:
    print("ok")
print(person)
h=input("want to delete?")
if h== "yes":
   i=input("delete what?")
   if i in person:
       del person[i]
   elif i not in person:
       print("xamlon")
if h== "no":
    print(ok)
print(person)