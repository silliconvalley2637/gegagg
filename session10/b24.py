Books={
    "Name": "Harry Potter",
    "Published": 1996,
    "Characters":["Harry Potter", "Hermione Granger", "Ronald Weasley", "Albus Dumbledore", "Lord Voldemort"]
}
Books["Country"]= "England"
Books["Characters"]=["Severus Snape", "Dobby", "Cedric Diggory"]
Books["Characters"].append("Kreacher")
print(Books["Characters"][1])
for k, v in Books.items():
    print(k, "-",v)
print(Books)