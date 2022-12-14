import time
import pandas as pd
from colorama import Fore, init  # for colors in text outputs
init(autoreset=True)


class registration:

    def home():
        homepage = open("../resources/welcome_cp.txt", "r")
        s = homepage.read()
        print(Fore.YELLOW + s)

        time.sleep(3)
        name = input("What is your name? - \n")
        print()
        print(f"Welcome to C.A.P.A.R.E. " + name)
        print("one moment please..")
        time.sleep(3)
        return name


    def dashboard(name, userdata):

        dash = input("Hi " + name + " ! Please choose where would you like to proceed: "
                     "\n1) New C.A.P.A.R.E. Game"
                     "\n2) Load saved C.A.P.A.R.E. Game"
                     "\n3) LeaderBoard"
                     "\n4) About C.A.P.A.R.E."
                     "\n5) Help"
                     "Enter the associated number [example - 1] or the first word of any option [example - new]")

        if dash.lower() == "new" or dash.lower() == "1":
            username = input(Fore.YELLOW + "Please enter a Username - ")
            if username in userdata['username'].values:  # checking if username already exists
                print("Username already exists, Please choose a different Username")
                registration.dashboard(name, userdata)
            else:
                password = input(Fore.YELLOW + "Please enter a password - ")
                temp_df = pd.Series({"username": username,
                                    "password": password})
                new_userdata = pd.concat([userdata, temp_df.to_frame().T], ignore_index=True)   # storing username in the csv file if it's not already stored before
                new_userdata.to_csv('../resources/userdata_cp.csv', index=False, header=True)
                print("Welcome to CAPARE " + name)
                user_info = [username, password]
                return user_info


        elif dash.lower() == "load" or dash.lower() == "2":
            userdata = pd.read_csv('../resources/userdata_cp.csv')
            username = input(Fore.RED + "Please enter a Username - ")
            if username in userdata['username'].values:
                user_index = userdata.index[userdata['username'] == username]
                password = input(Fore.RED + "Please enter a password - ")
                if (userdata.iloc[user_index]['password'] == password).bool():  # validating password
                    print("Welcome to CAPARE" + name)
                    user_info = [username, password]
                    return user_info
                else:
                    print("Wrong Password, try again!")
                    registration.dashboard(name, userdata)
            else:
                print("User does not exist or invalid user, please try again!")
                registration.dashboard(name, userdata)

        elif dash.lower() == "leaderboard" or dash.lower() == "3":
            df = pd.read_csv('../resources/userdata_cp.csv')
            lead = df.sort_values(by=['score'], ascending=False)  # to arrange the leaderboard from highest to lowest
            new_lead = lead.drop('password', axis=1)
            print(new_lead)
            registration.dashboard(name, userdata)
            print("\n\n\n\n\n\n")

        elif dash.lower() == "about" or dash.lower() == "4":
            about = open("../resources/about_cp.txt", "r")
            a = about.read()
            print(a)
            print("\n")
            registration.dashboard(name, userdata)
        elif dash.lower() == "help" or dash.lower() == "5":
            help = open("../resources/help_cp.txt", "r")
            h = help.read()
            print(h)
            print("\n")
            registration.dashboard(name, userdata)
        else:
            print("Please select a valid option " + name)
            print("\n")
            registration.dashboard(name, userdata)
