while True:
    n=input("To sign up, we need some information from yours, are you ready?")
    if n=="ok":
        z=input("email:")
        if "@" in z:
            print(ok) 
            break
        else:
            print("your email must has @")
            input("type again")
    else:
        print("FUCK OFF")
        break       
while True:
    input("And your username?")
    m=input("type your password for your account")
    p=input("please type again to make sure that your password is correct")
    if m==p:
        print("You have created your account")
        break
    elif m!=p:
            print("please type again")              
