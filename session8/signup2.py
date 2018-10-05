while True:
    n=input("To sign up, we need some information from yours, are you ready?")
    if n=="ok":
        input("Whats your email address?")
        input("And your username?")
        m=input("type your password for your account")
        p=input("please type again to make sure that your password is correct")
        if m==p:
             print("You have created your account")
             break
        elif m!=p:
            print("please type again")              
    else:
        print("FUCK OFF")
        break