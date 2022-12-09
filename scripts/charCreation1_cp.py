#from scripts.gameMain_cp import credentials
#from registration_cp import username, password

# from scripts.gameMain_cp import *


# username = username
# password = password


class MainChar:

    char_health = 100

    def __init__(self, username, char_name, char_type, char_gender, power):
        self.username = username
        self.char_name = char_name
        self.char_type = char_type
        self.char_gender = char_gender
        self.power = power
        #self.char_health = 100
    #@staticmethod
    def char_1(username):

        char_name = input(f"\n So," + username + ", "
                          "what will be your name in C.A.P.A.R.E.? "
                          "Please Enter your Avatar's name - ")
        return char_name

    # def __init__(self, char_name, power):
    #     self.char_name = char_name  # input("Enter the King's name - ")
    #     self.power = power

    def attack(self):
        print(f"King {self.char_name} attacks you for {self.power} damage!")

    def damage(self, health):

        health -= 20
        return health
        #print(f"Your health status: {self.power} (costed {health} damage))")

    def char_2(username):

        char_type = input("What type of a Avatar is this " + username + "? "
                          "(For example: Knight, Witch, Spy, etc) - ")
        return char_type


    def char_3(char_name, char_type):

        char_gender = input("Which gender would you like to give to your Avatar? Enter male/female or m/f - ")

        if char_gender.lower() == 'male' or char_gender.lower() == 'm':
            print("\nLet the past begin Sir. " + char_name+"! the great " + char_type)
        elif char_gender.lower() == 'female' or char_gender.lower() == 'f':
            print("\nLet the past begin Madam. " + char_name+"! the great " + char_type)
        else:
            print("Please enter correct gender - ")
            MainChar.char_3(char_name, char_type)

        return char_gender
        #enemyCreation_cp.MainEnemy.enemy_details()

    def char_3a(self):

        if self.char_gender.lower() == 'male' or self.char_gender.lower() == 'm':
            print("\nYou are an awesome Man!!. " + self.char_name+" ! the great " + self.char_type)
        else:
            print("\nYou are a fearless woman!!. " + self.char_name+" ! the great " + self.char_type)
