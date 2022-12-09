import time

#import gameMain_cp
# print("\n C.A.P.A.R.E \n  Welcomes you \n")


def home():
    homepage = open("../resources/welcome_cp.txt", "r")
    s = homepage.read()
    print(s)

    time.sleep(3)
    name = input("What is your name? - \n")
    print()
    print(f"Welcome to C.A.P.A.R.E. " + name)
    print("one moment please..")
    time.sleep(3)


def userpass():
    while True:

        verify = input("\n Do you have a username ? (yes/no) or (y/n) - ")

        if verify.lower() == "yes" or verify.lower() == "y":
            username = input("Please enter a Username - ")
            password = input("Please enter a password - ")
            return username, password
            break

        elif verify.lower() == "no" or verify.lower() == "n":
            print("Please create an account for yourself")
            username = input("Please enter a Username - ")
            password = input("Please enter a password - ")
            return username, password
            break

        else:
            print("Please enter a valid answer")
            continue
            #print()
            #userpass()

        #print("Wrong credentials")
        #userpass()

#gameMain_cp.MainChar()

home()
credentials = userpass()
username = credentials[0]
password = credentials[1]
