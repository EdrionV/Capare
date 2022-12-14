import sys  # to terminate the program
import numpy as np
import time
from inventory_cp import Inventory
from charCreation1_cp import MainChar
from registration_cp import registration
from enemyCreation_cp import MainEnemy
import pandas as pd
from colorama import Fore, init
init(autoreset=True)


userdata = pd.read_csv('../resources/userdata_cp.csv')  # storing user's stored data in this variable

name = registration.home()  # storing home function in this variable
user_info = registration.dashboard(name, userdata) # storing the dashboard function in this variable
homepage = open("../resources/welcome_cp.txt", "r")
s = homepage.read()  # storing the home page txt file in this variable
new_userdata = pd.read_csv('../resources/userdata_cp.csv') # storing user's updated data in this variable

username = user_info[0]  # storing the first value from the user_info list in registration_cp file
password = user_info[1]  # storing the second value from the user_info list in registration_cp file
char_name = MainChar.char_1(username)  # storing the character's name from Class Mainchar in charCreation1_cp file
char_type = MainChar.char_2(username) # storing the character's type from Class Mainchar in charCreation1_cp file
char_gender = MainChar.char_3(char_name, char_type) # storing the character's gender from Class Mainchar in charCreation1_cp file
enemy_info = MainEnemy.enemy_details() # storing the enemy_info list from Class enemy_details in enemyCreation_cp file
enemy_name = enemy_info[0]  # storing the first value from the enemy_info list in nemyCreation_cp file
enemy_pronouns = enemy_info[1]  # storing the first value from the enemy_info list in nemyCreation_cp file
enemy = enemy_info[2]  # storing the third value from the enemy_info list in nemyCreation_cp file
inventory = []  # declaring the inventory parameter
char_health = 90  # pre-defined values \ character's health
g1_health = 50  # pre-defined values \ first guard's health
g2_health = 50  # pre-defined values \ second guard's health
w1_health = 20  # pre-defined values \ first wolf's health
w2_health = 30  # pre-defined values \ second wolf's health
l1_health = 20  # pre-defined values \ first lion's health
l2_health = 30  # pre-defined values \ second lion's health
enemy_health = 100  # pre-defined values \ main enemy's health (Queen/King)
Inventory = Inventory() # Class Inventory defined


class History:  # Consists of the main storyline
    inventory = []  # defining inventory inside the class
    char_name = char_name  # defining character's name inside the class
    char_type = char_type  # defining character's type inside the class
    char_gender = char_gender  # defining character's gender inside the class
    enemy_name = enemy_name  # defining enemy's name inside the class
    enemy_pronouns = enemy_pronouns  # defining enemy's pronouns inside the class
    enemy = enemy  # defining enemy's title inside the class
    g1_health = g1_health  # defining first guard's health inside the class
    g2_health = g2_health  # defining second guard's name inside the class
    enemy_health = enemy_health  # defining main enemy's name inside the class
    char_health = char_health  # defining character's health inside the class
    w1_health = w1_health  # defining first wolf's health name inside the class
    w2_health = w2_health  # defining second wolf's health name inside the class
    l1_health = l1_health  # defining first lion's health name inside the class
    l2_health = l2_health  # defining second lion's health name inside the class
    new_userdata = new_userdata  # defining our updated user's data inside the class, which is stored in new_userdata.

    def __init__(self, username, password, char_name, char_type, char_gender, char_health, enemy, enemy_name,
                 enemy_pronouns, enemy_health, g1_health, g2_health, inventory, w1_health, w2_health, l1_health,
                 l2_health, new_userdata):
        self.username = username
        self.password = password
        self.char_name = char_name
        self.char_type = char_type
        self.char_gender = char_gender
        self.enemy = enemy
        self.enemy_name = enemy_name
        self.enemy_pronouns = enemy_pronouns
        self.enemy_health = enemy_health
        self.g1_health = g1_health
        self.g2_health = g2_health
        self.inventory = inventory
        self.char_health = char_health
        self.w1_health = w1_health
        self.w2_health = w2_health
        self.l1_health = l1_health
        self.l2_health = l2_health
        self.new_userdata = new_userdata

################################################### SOUTH CODE FROM THE BOTTOM #####################################################################
#  The functions are defined in reverse order for developer's ease.

    def slevels_2(self):  # If user chooses south direction
        slevel_2 = input(Fore.CYAN + "Enter 'leave' or 'l' to leave the temple and get back to the junction - ")
        if slevel_2.lower() == "leave" or slevel_2.lower() == "l":
            print()
            History.levels_2(self, char_name, char_type, enemy)

        else:
            print(Fore.RED + "Enter valid command " + self.char_type + " " + self.char_name + "!!")
            time.sleep(3)
            History.slevels_1(self)

    def slevels_1(self): # If user chooses south direction
        slevel_1 = input(Fore.CYAN + "\nEnter 'pray' or 'p' if you wish to worship OR "
                         "\n Enter 'leave' or 'l' to leave the temple and get back to the junction ")
        if slevel_1.lower() == "pray" or slevel_1.lower() == "p":
            print(Fore.CYAN + "Silence is the word your mind is achieving, while you worship and pray")
            time.sleep(7)
            print(Fore.CYAN + "\nYou are now refreshed and pumped up to continue your mission. ")
            print(Fore.GREEN + "\nBonus - You have received extra 5 health from meditation and prayer")
            self.char_health += 5
            print(Fore.GREEN + "Your Health: " + str(abs(self.char_health)))
            time.sleep(5)
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.slevels_2(self) # after displaying the help page, the game continue automatically
            else:
                print()
                History.slevels_2(self)  # If user entered any key other than the specified ones, then the game continue

        elif slevel_1.lower() == "leave" or slevel_1.lower() == "l":
            print()
            History.levels_2(self, char_name, char_type, enemy)

        else:
            print(Fore.RED + "Enter valid command " + self.char_type + " " + self.char_name + "!!")
            time.sleep(3)
            History.slevels_1(self)

################################################### NORTH CODE FROM THE BOTTOM #####################################################################

    def ends(self):  # End of the game in north direction
        end = input(Fore.WHITE + "\n\n\n\n\n\nHey CAPARE member, "
                    "\nCongratulations!! on your Victory!"
                    "\nEnter 'exit' to return to the main menu "
                    "\nand to explore other Avatar stories!!")
        if end.lower() == "exit":
            print(Fore.YELLOW + "Exited")
            sys.exit()

        else:
            print(Fore.RED + "Wrong command!")
            time.sleep(3)
            History.ends(self)

    def levels_2e(self, char_type, char_name, enemy_pronouns):
        level_2e = input(Fore.BLUE + f"\nLift " + self.enemy_pronouns[1] + " eternal throne and wear it "
                         + self.char_type + " " + self.char_name + " \nEnter 'wear' or 'w' to wear the throne - ")
        if level_2e.lower() == "wear" or level_2e.lower() == "w":
            print(Fore.CYAN + "\n\n\n!!!!!!VICTORY!!!!!!"
                  "\nYour anger has achieved its satisfaction. "
                  "\nA sense of peace you feel within you"
                  "\nYou have conquered this Era " + self.char_type + " " + self.char_name + "!"
                  "\n!!!! This Empire is all yours now and forever, for your revenge is complete"
                  "\n\n !!!!!!!VICTORY!!!!!VICTORY!!!!!!"
                  "\n" + self.char_type.upper() + " " + self.char_name.upper() +
                  " has captured the PAST of the INDUS VALLEY EMPIRE - "
                  "\n\n*THE HISTORIC ERA*")
            print(Fore.YELLOW + "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                  "YOUR GRAND SCORE - " + str(self.char_health))

            self.new_userdata.loc[new_userdata.username == "username", "score"] = self.char_health
            print(self.new_userdata)
            self.new_userdata.to_csv('../resources/userdata_cp.csv', index=False, header=True)

            History.ends(self)

        else:
            print(Fore.RED + "\nCome on! You can't make mistakes at this point. "
                  "\nEnter the correct command")
            time.sleep(3)
            History.levels_2e(self, char_type, char_name, enemy_pronouns)

    def levels_2d(self, char_type, char_name, enemy, enemy_name, enemy_pronouns):
        level_2d = input(f"\nUsing your words, give " + self.enemy_pronouns[2] +
                         f" a final goodbye! Enter 'say' or 's' - ")
        if level_2d.lower() == "say" or level_2d.lower() == 's':
            print(Fore.CYAN + "\n" + self.char_type + " " + self.char_name + ": 'You are done! "
                  "\nand this is my revenge " + self.enemy_name +
                  "for messing with my family's business. \nSee you never!'"
                  "\n\nThe " + self.enemy + " is finally DEAD. \n" + self.enemy_pronouns[0] + ""
                  " is down on your feet, dead and bleeding.\nThere is no other thing as happy as this, for you")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.levels_2e(self, char_type, char_name, enemy_pronouns)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.levels_2e(self, char_type, char_name, enemy_pronouns)  # If user entered any key other than the specified ones, then the game continue

        else:
            print(Fore.RED + "\nWhat's that ? Enter the right command")
            time.sleep(3)
            History.levels_2d(self, char_type, char_name, enemy, enemy_name, enemy_pronouns)

    def actions_4(self, char_type, char_name, enemy_pronouns, enemy):
        action_4 = input(f"Enter 'attack' or 'a' to kill " + self.enemy_pronouns[2] + " - ")
        i = 0
        if action_4.lower() == "attack" or action_4.lower() == "a":
            while (self.enemy_health > 0):  # the loop starts until the enemy;s health reaches or goes beyond 0
                print(Fore.RED + "The " + self.enemy + " has attacked you back!")
                time.sleep(2)
                self.char_health -= np.random.randint(5, 10)
                self.enemy_health -= np.random.randint(10, 15)
                time.sleep(3)
                print("Your Health: " + str(abs(self.char_health)))
                time.sleep(1)

                if self.enemy_health > 0:  # continue the loop
                    print("\n" + self.enemy + "'s Health: " + str(abs(self.enemy_health)))
                    print(Fore.RED + "Oh " + self.enemy_pronouns[0] + " is a tough thing !")
                    print(Fore.RED + "The " + self.enemy + " has attacked you back!")
                if self.char_health < 0:  # terminates the loop and exits user back to the game's dashboard
                    print(Fore.RED + "YOU HAVE DIED!!!! GAME OVER")
                    print(s)
                    registration.dashboard(name, userdata)

            print(f"\n The " + self.enemy + " is now all yours " + self.char_type + " " + self.char_name + "!"
                  "\nKill is the only thing which comes to your mind now")
            History.levels_2d(self, char_type, char_name, enemy, enemy_name, enemy_pronouns)

        else:
            print(Fore.RED + "\nPlease enter correct command before he gets out of your way!")
            time.sleep(3)
            History.actions_4(self, char_type, char_name, enemy_pronouns, enemy)

    def levels_2c(self, enemy_name, enemy_pronouns, enemy):

        level_2c = input(f"Enter 'stab' or 's' to kill the 2nd lion - ")
        i = 0
        if level_2c.lower() == "stab" or level_2c.lower() == "s":

            while (self.l2_health > 0):
                print(Fore.RED + "The Second lion has attacked you back!")
                time.sleep(2)
                self.char_health -= np.random.randint(2, 8)
                self.l2_health -= np.random.randint(8, 10)
                time.sleep(3)
                print("Your Health: " + str(abs(self.char_health)))
                print("Second Lion's Health: " + str(abs(self.l2_health)))
                time.sleep(1)

                if self.l2_health > 0:
                    print(Fore.RED + "Roar!!!! it won't die so easily")
                if self.char_health < 0:
                    print(Fore.RED + "YOU HAVE DIED!!!! GAME OVER")
                    print(s)
                    registration.dashboard()
            print("\nYes! Both Lions down! and you are finally at your target's doorsteps!"
                  "\n With your previously chosen weapon, you now have to kill "
                  + self.enemy + " " + self.enemy_name +
                  "\nYou have to kill " + self.enemy_pronouns[2] + " and wear \n"
                  + self.enemy_pronouns[1] + " crown by which, you will become "
                  "the new Ruler of this Empire! \nYou have to hurry up before anyone else "
                  "enters " + self.enemy_pronouns[1] + " room. "
                  "\n\n You are now standing in the " + self.enemy + " 's room, "
                  "looking straight into " + self.enemy_pronouns[1] + " eyes, where " + self.enemy_pronouns[1] +
                  " eyes are full of fear and anger at the same time. Before " + self.enemy_pronouns[0] +
                  " tries to jump out of " + self.enemy_pronouns[1] + " window, "
                  "Use your chosen weapon to kill " + self.enemy_pronouns[2])
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.actions_4(self, char_type, char_name, enemy_pronouns, enemy)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.actions_4(self, char_type, char_name, enemy_pronouns, enemy)  # If user entered any key other than the specified ones, then the game continue

        else:
            print(Fore.RED + f"\nWhom are you stabbing ? Enter the correct command please")
            time.sleep(3)
            History.levels_2c(self, enemy_name, enemy_pronouns, enemy)

    def levels_2b(self):

        level_2b = input(f"Enter 'stab' or 's' to kill the 1st lion with your knife - ")
        i = 0
        if level_2b.lower() == "stab" or level_2b.lower() == "s":
            while (self.l1_health > 0):  # The loop starts until the lion's health reaches or goes beyond 0
                print(Fore.RED + "The First lion attacked you too!")
                time.sleep(2)
                self.char_health -= np.random.randint(2, 8)
                self.l1_health -= np.random.randint(8, 10)
                time.sleep(3)
                print("Your Health: " + str(abs(self.char_health)))
                print("First Lion's Health: " + str(abs(self.l2_health)))
                time.sleep(1)

                if self.l1_health > 0:  # loop continues
                    print(Fore.RED + "It's still alive!!!!")
                if self.char_health < 0:  # terminates the loop and exits user back to the game's dashboard
                    print(Fore.RED + "YOU HAVE DIED!!!! GAME OVER")
                    print(s)
                    registration.dashboard()
            print(f"Excellent! one down, 1 to go!")
            History.levels_2c(self, enemy_name, enemy_pronouns, enemy)

        else:
            print(Fore.RED + "\nWhom are you stabbing ? Enter the correct command please")
            time.sleep(3)
            History.levels_2b(self)

    def actions_3(self):

        action_3 = input(f"\nEnter 'fire' or 'f' to attack the lions - ")
        if action_3.lower() == "fire" or action_3.lower() == "f":
            self.l1_health -= np.random.randint(5, 8)
            self.l2_health -= np.random.randint(2, 7)
            print(Fore.RED + "The wolves have scratched your face while u scare them!")
            self.char_health -= np.random.randint(2, 7)
            print("Your Health: " + str(self.char_health))
            print("First Lion's Health: " + str(self.l1_health))
            print("Second Lion's Health: " + str(self.l2_health))
            self.inventory.remove("Firelight")
            print("Brilliant! its easy to kill them now as they are weak and scared!")
            History.levels_2b(self)

        else:
            print(Fore.RED + f"\nWrong command! There's no time! please press the right command! "
                  f"\nThe lions are coming towards you!")
            time.sleep(3)
            History.actions_3(self)

    def eqs_1(self, char_name, inventory):

        eq_1 = input(f"Enter 'pick' or 'p' to pick a firelight - ")

        if eq_1.lower() == "pick" or eq_1.lower() == "p":
            self.inventory.append("Firelight")
            Inventory.view_inventory(self.inventory)
            print(f"\n\n*Firelight added to your equipment*"
                  f"\n\n Climbing the last floor, you are now right in front, facing the 2 deadly lions!"
                  f"\nBefore taking any further step, you have to use your 'Firelight' on the lions.")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.actions_3(self)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.actions_3(self)  # If user entered any key other than the specified ones, then the game continue

        else:
            print(Fore.RED + f"Enter valid command Witch " + self.char_name + "!!")
            time.sleep(3)
            History.eqs_1(self, char_name, inventory)

    def levels_2a(self):

        level_2a = input(f"\nEnter 'climb' or 'c' to climb the stairs - ")

        if level_2a.lower() == "climb" or level_2a.lower() == "c":
            print(
                f"\n\nYou are now climbing the stairs. On your way up you see Firelights, "
                f"\nyou can pick one of them,"
                f" as this will be of great help fighting the Lions upstairs.")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.eqs_1(self, char_name, inventory)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.eqs_1(self, char_name, inventory)  # If user entered any key other than the specified ones, then the game continue

        else:
            print(Fore.RED + "\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.levels_2a(self)

    def actions_2(self, enemy, enemy_pronouns):

        action_2 = input(f"\nTake out the keys from the guards vest, to open the front gate"
                         f"Enter 'open' or 'o' to do so - ")

        if action_2.lower() == "open" or action_2.lower() == 'o':
            print(f"\n\nWalla! you have now entered the Castle. Your mission is not too far now to be accomplished. "
                  "\n\nThe " + self.enemy + " is on the top floor, preparing to sleep (probably forever). "
                  "The guards are on their rounds \nbut currently not outside the " + self.enemy + " 's room. "
                  "\n To reach " + self.enemy_pronouns[2] + " , you have to quickly climb 2 floors and "
                  "\nface 2 deadly Lions owned by the " + self.enemy + " for " + self.enemy_pronouns[2] + " protection.")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.levels_2a(self)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.levels_2a(self)  # If user entered any key other than the specified ones, then the game continue

        else:
            print(Fore.RED + "\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.actions_2(self, enemy, enemy_pronouns)

    def actions_1(self):

        action_1 = input("\nPress 'Knife' or 'k' to use your Knife - ")

        if action_1 == "knife" or action_1 == 'k':
            MainChar.char_health -= 5
            print("Your Health: " + str(self.char_health))

            self.g1_health -= 25
            print(Fore.RED + "Guard attacked you too!")
            self.char_health -= np.random.randint(5, 10)
            print("Your Health: " + str(self.char_health))
            print("Guard's Health: " + str(self.g1_health))

            def a3():
                a3_attack = input(Fore.RED + f"\nHe's not dead yet! Use the knife to cut that guard's throat"
                                  f"\nEnter 'cut' or 'ct' - ")
                if a3_attack.lower() == "cut" or a3_attack.lower() == "ct":
                    self.g1_health -= 25
                    print("Your Health: " + str(self.char_health))
                    print("Guard's Health: " + str(self.g1_health))
                    time.sleep(2)
                else:
                    print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
                    time.sleep(3)
                    a3()
            a3()
            History.actions_2(self, enemy, enemy_pronouns)

        else:
            print(Fore.RED + "\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.actions_1(self)

    def eqs(self, inventory, char_name, char_type):  # Start of the north direction

        eq = input("\nPress 'pick' or 'p' to collect them")

        if eq.lower() == "pick" or eq.lower() == "p":
            self.inventory.append("Footwear")
            self.inventory.append("Knife")
            Inventory.view_inventory(inventory)

            print(f"\n*Knife and Footwear added to your equipment*. "
                  f"\n\nYou are now reaching the Castle's outer North gate. \nPhew! the guards are asleep for now")
            time.sleep(2)
            print(Fore.RED + "\n\n\n\nOh no!  A GUARD HAS SPOTTED YOU   " + self.char_type.upper() +
                  " " + self.char_name.upper() + "!!! "
                  "\nBefore he wakes the other guards up and alerts the Castle, you have to do something!!"
                  "\n Use the knife to shut that guard forever. ")
            History.actions_1(self)

        else:
            print(Fore.RED + "\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.eqs(self, inventory, char_name, char_type)

################################################### EAST CODE FROM THE BOTTOM #####################################################################

    def ends_e(self):  # End of the game in east direction
        end_e = input(Fore.WHITE + "\n\n\n\n\n\nHey CAPARE member, "
                      "\nCongratulations!! on your Victory!"
                      "\nEnter 'exit' to return to the main menu "
                      "\nand to explore your other Avatars!!")
        if end_e.lower() == "exit":
            sys.exit()

        else:
            print(Fore.RED + "Wrong command!")
            time.sleep(3)
            History.ends_e(self)

    def elevels_riddle(self, enemy, enemy_name, char_type, char_name):

        for i in range(3):  # the loop starts until the attempt reaches 3
            riddle = input(Fore.YELLOW + f"\n\nRIDDLE - What can cut like a knife and sting like a bee. "
                           f"\nCarry truth and lies but never move or speak. What are we? "
                           f"\n(You have just 3 ATTEMPTS until "
                           + self.enemy + " " + self.enemy_name + " 's guards are here)"
                           f"\n What is your answer? - ")
            if riddle.lower() == "words" or riddle.lower() == "word": #  if the answer is correct, History.ends_e(self) function is called
                print(Fore.CYAN + "\n\n\n!!!!!!VICTORY!!!!!!"
                      "\nYour anger has achieved its satisfaction. "
                      "\nA sense of peace you feel within you"
                      "\nYou have conquered this Era " + self.char_type + " " + self.char_name +
                      "\n!!!! This Empire is all yours now and your revenge is complete"
                      "\n\n !!!!!!!VICTORY!!!!!VICTORY!!!!!!\n"
                      + self.char_type + " " + self.char_name +
                      " has captured the PAST of the INDUS VALLEY EMPIRE - "
                      "\n*THE HISTORIC ERA*")
                print(Fore.YELLOW + "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
                      "YOUR GRAND SCORE - " + str(self.char_health))
                time.sleep(3)
                self.new_userdata.loc[new_userdata.username == "username", "score"] = self.char_health
                print(self.new_userdata)
                self.new_userdata.to_csv('../resources/userdata_cp.csv', index=False, header=True)
                History.ends_e(self)
                break  # loop breaks and the History.ends_e(self) function is called
            else:  # sends the user back to attempt the question again
                print(Fore.RED + f"\n\nWrong answer ! - Give it another go (Hint - One has to be careful while using us)"
                                 f"\nYou attempted " + str(i+1) + "times")
                time.sleep(3)

        else:  # exits the user and the loop ends
            print(Fore.RED + f"\n\nTIME'S UP!! The guards have come and have lynched you! "
                  f"\nYOU'RE DEAD!!")
            print(Fore.YELLOW + "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYOUR GRAND SCORE - " + str(self.char_health))
            time.sleep(3)
            print(s)
            registration.dashboard(name, userdata)

    def elevels_5a(self, char_type, char_name, enemy_pronouns):  # EAST LEVEL
        elevel_5a = input(Fore.BLUE + f"Pick up " + self.enemy_pronouns[1] + " eternal throne and wear it  "
                          + self.char_type + " " + self.char_name +
                          "\nEnter 'wear' or 'w' to wear this magical throne - ")
        if elevel_5a.lower() == "wear" or elevel_5a.lower() == "w":
            print(Fore.YELLOW + "\n\nThe THRONE is magical and it listens to the one who understands it"
                  "\nIn order to own the throne, You have to solve a riddle by giving the correct answer")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter 'z' to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.elevels_riddle(self, self.enemy, enemy_name, char_type, char_name)  # after displaying the help page, the game continue automatically
            elif e.lower() == "z":
                print()
                History.elevels_riddle(self, self.enemy, enemy_name, char_type, char_name)  # If user entered this key other then the specified ones, then the game continue
            else:
                print("Please enter valid command")
        else:
            print(Fore.RED + "\nCome on! You can't make mistakes at this point. "
                  "\nEnter the correct command")
            time.sleep(3)
            History.elevels_5a(self, char_type, char_name, enemy_pronouns)

    def elevels_5(self, enemy, enemy_pronouns, enemy_name):  # EAST LEVEL
        elevel_5 = input(Fore.BLUE + f"\n\nYou are heading towards the " + self.enemy + ", with your previously chosen weapon, "
                         f"\nyou have fight with " + self.enemy_pronouns[2] + "\nEnter 'fight' or 'f' to fight "
                         + self.enemy + " " + self.enemy_name + " \n- ")
        i = 0
        if elevel_5.lower() == "fight" or elevel_5.lower() == "f":
            while (self.enemy_health > 0):  # loop starts until the enemy's health reaches of goes beyond 0
                print("\n" + Fore.RED + self.enemy + " attacked you too!")
                time.sleep(2)

                self.char_health -= np.random.randint(5, 10)  # selects randomly between 5 to 9, the number to be deducted from character's health )
                self.enemy_health -= np.random.randint(10, 20)  # selects randomly between 10 to 19, the number to be deducted from enemy's health )
                time.sleep(3)
                print(Fore.YELLOW + "Your Health: " + str(abs(self.char_health)))  #  will display chracter's health
                time.sleep(1)
                if self.enemy_health > 0:
                    print(Fore.YELLOW + self.enemy + "'s Health: " + str(abs(self.enemy_health)))
                    print(Fore.YELLOW + "The battle continues!!!!")
                if self.char_health < 0:
                    print(Fore.RED + "YOU HAVE DIED!!!! GAME OVER")
                    print(s)
                    registration.dashboard(name, userdata)

            print(Fore.GREEN + "\n" + self.enemy + " " + self.enemy_name + " is finally DEAD. " + self.enemy_pronouns[0] +
                  " is down on your feet, bleeding."
                  "\nThere is no other thing as happy as this, for you")
            History.elevels_5a(self, char_type, char_name, enemy_pronouns)

        else:
            print(Fore.RED + f"Wrong entry! Please try again - ")
            time.sleep(3)
            History.elevels_5(self, enemy, enemy_pronouns, enemy_name)

    def elevels_4b(self, enemy, enemy_name, enemy_pronouns):  # EAST LEVEL

        elevel_4b = input(Fore.BLUE + f"\nEnter 'enter' or 'e' to open the door and enter the dining area quietly - ")
        if elevel_4b.lower() == "enter" or elevel_4b.lower() == "e":
            print(Fore.YELLOW + "\n\n" + self.enemy.upper() + " " + self.enemy_name.upper() + " IS FINALLY IN FRONT OF YOU! "
                  "\nThis is your chance to kill " + self.enemy_pronouns[2] + " and take on " + self.enemy_pronouns[1] +
                  " throne to rule the entire empire! \nYou see " + self.enemy_pronouns[1] +
                  " filled with anger and fear. Before " + self.enemy_pronouns[0] + " runs away, you have to eliminate "
                  + self.enemy_pronouns[2] + " !")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.elevels_5(self, enemy, enemy_pronouns, enemy_name)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.elevels_5(self, enemy, enemy_pronouns, enemy_name)  # If user entered any key other then the specified ones, then the game continue


        else:
            print(Fore.RED + f"\nWhere are you trying to enter ? Please enter correct command")
            time.sleep(3)
            History.elevels_4b(self, enemy, enemy_name, enemy_pronouns)

    def elevels_4a(self, inventory):  # EAST LEVEL

        elevel_4a = input(Fore.BLUE + f"\nEnter 'kill' or 'k' to kill the wolf!! - ")
        if elevel_4a.lower() == "kill" or elevel_4a.lower() == "k":
            self.w2_health -= 15
            print(Fore.RED + "Wolf attacked you too!")
            self.char_health -= np.random.randint(5, 10)
            print(Fore.YELLOW + "Your Health: " + str(self.char_health))
            print(Fore.YELLOW + "Wolf's Health: " + str(self.w2_health))

            def w2():
                w2_attack = input(Fore.BLUE + f"\nUse the Steel Chain to attack the second wolf again"
                                  f"\nEnter 'kill' or 'k' - ")
                if w2_attack.lower() == "kill" or w2_attack.lower() == "k":
                    self.w2_health -= 10
                    print(Fore.GREEN + "\nYeaahh! You have killed the wolf")
                    time.sleep(2)
                else:
                    print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
                    time.sleep(3)
                    w2()

            w2()

            print(Fore.RED + f"\n\n The steel chain is now of no use and broken")
            self.inventory.remove("Steel chain")
            Inventory.view_inventory(self.inventory)
            print(Fore.BLUE + f"\nBefore anyone else spots you, you have to enter the dining area")
            History.elevels_4b(self, self.enemy, enemy_name, enemy_pronouns)

        else:
            print(Fore.RED + f"\nEnter valid command !")
            time.sleep(3)
            History.elevels_4a(self, inventory)

    def elevels_4(self, inventory):  # EAST LEVEL

        elevel_4 = input(Fore.RED + "\nThe Wolf has spotted you and it's coming towards you!!"
                         "\nUsing the Firelight and the steel chain, kill the hungry wolf"
                         "\nEnter 'kill' or 'k' to get rid of the wolf - ")

        if elevel_4.lower() == "kill" or elevel_4.lower() == "k":
            self.w1_health -= 10
            print(Fore.RED + "Wolf attacked you too!")
            self.char_health -= np.random.randint(5, 10)
            print(Fore.YELLOW + "Your Health: "+str(self.char_health))
            print(Fore.YELLOW + "Wolf's Health: "+str(self.w1_health))

            def w1():  # wolf fight scene
                w1_attack = input(Fore.BLUE + f"\nUse the Firelight to attack the first wolf again"
                                  f"\nEnter 'kill' or 'k' - ")
                if w1_attack.lower() == "kill" or w1_attack.lower() == "k":
                    self.w1_health -= 10
                    print(Fore.GREEN + "\nYeaahh! You have killed the wolf")
                    time.sleep(2)
                else:
                    print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
                    time.sleep(3)
                    w1()
            w1()

            print(Fore.GREEN + f"\n\nBravo!! The wolf is dead ! and the wait is finally over"
                  f"\nThere is nothing stopping you from entering the dining area now")
            time.sleep(2)
            Inventory.del_inventory(inventory, "Firelight")  # will remove the item firelight from the inventory list
            Inventory.view_inventory(self.inventory)
            print(Fore.RED + f"\n\n\nOh wait! YOU HAVE BEEN ATTACKED BY ANOTHER WOLF FROM BEHIND!!!!!!")
            self.char_health -= np.random.randint(5, 10)
            print(Fore.YELLOW + "Your Health: " + str(self.char_health))
            time.sleep(4)
            History.elevels_4a(self, inventory)

        else:
            print(Fore.RED + f"\nEnter valid command !")
            time.sleep(3)
            History.elevels_4(self, inventory)

    def eeqs_2(self, inventory):  # EAST LEVEL

        eeq_2 = input(Fore.BLUE + "\n\nYou see many Firelights hanging around the backyard. You can use this "
                      "to frighten the wolf and kill it with the steel chain"
                      "Enter 'fire' or 'f' to pick one Firelight - ")

        if eeq_2.lower() == "fire" or eeq_2.lower() == "f":
            inventory.append("Firelight")
            Inventory.view_inventory(self.inventory)
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.elevels_4(self, inventory)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.elevels_4(self, inventory)  # If user entered any key other then the specified ones, then the game continue

        else:
            print(Fore.RED + "\n Nah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.eeqs_2(self, inventory)

    def message(self, enemy, enemy_pronouns):  # EAST LEVEL

        message_1 = input(Fore.BLUE + "\n\nEnter 'listen' or 'l' to hear what the guard has to say - ")
        if message_1.lower() == "listen" or message_1.lower() == "l":
            print(Fore.CYAN + f"\n\nGUARD: 'THE " + self.enemy + " IS IN " + self.enemy_pronouns[1] + " "
                  "DINING HALL ALONE, PREPARING FOR " + self.enemy_pronouns[1] + " DINNER'"
                  f"\n\n After listening to the now dead guard, you head into the castle."
                  f"\nHiding yourself you have managed to reach the castle's backyard, "
                  f"\nfrom where you can enter the dining"
                  f"hall, through it's back door. \nYou are now at the backyard and you see a "
                  f"hungry wolf roaming around the backyard"
                  f"\nYou have to kill the wolf to enter the back door of the dining hall.")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.eeqs_2(self, inventory)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.eeqs_2(self, inventory)  # If user entered any key other then the specified ones, then the game continue

        else:
            print(Fore.RED + "\n Invalid command! Please re-enter")
            time.sleep(3)
            History.message(self, enemy, enemy_pronouns)

    def elevels_3a(self, enemy):  # EAST LEVEL

        elevel_3a = input(Fore.BLUE + f"\nUse the chain to choke the second guard's neck"
                          f"\nEnter 'choke' or 'ch' - ")

        if elevel_3a.lower() == "choke" or elevel_3a.lower() == "ch":
            self.g2_health -= 25
            print(Fore.RED + "Guard attacked you too!")
            self.char_health -= np.random.randint(5, 10)
            print(Fore.YELLOW + "Your Health: "+str(self.char_health))
            print(Fore.YELLOW + "Guard's Health: "+str(self.g2_health))

            def a2():
                a2_attack = input(Fore.BLUE + f"\nUse the chain to choke the second guard's neck again"
                                  f"\nEnter 'choke' or 'ch' - ")
                if a2_attack.lower() == "choke" or a2_attack.lower() == "ch":
                    self.g2_health -= 25
                    print(Fore.GREEN + "\nYeaahh! You have killed the second guard")
                    time.sleep(2)
                else:
                    print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
                    time.sleep(3)
                    a2()
            a2()
            print(Fore.GREEN + "\nHurray! another one bites the dust!")
            print(Fore.BLUE + f"\n\nWhile the guard is breathing his lasts, you try to ask him where is the " + self.enemy +
                  " ?? is " + self.enemy_pronouns[1] + " alone??")
            History.message(self, enemy, enemy_pronouns)

        else:
            print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
            time.sleep(3)
            History.elevels_3a(self, enemy)

    def elevels_3(self):  # EAST LEVEL

        elevel_3 = input(Fore.BLUE + f"\nUse the chain to choke the first guard's neck"
                         f"\nEnter 'choke' or 'ch' - ")

        if elevel_3.lower() == "choke" or elevel_3.lower() == "ch":
            self.g1_health -= 25
            print(Fore.RED + "Guard attacked you too!")
            self.char_health -= np.random.randint(5, 10)
            print(Fore.YELLOW + "Your Health: "+str(self.char_health))
            print(Fore.YELLOW + "Guard's Health: "+str(self.g1_health))

            def a1():
                a1_attack = input(Fore.BLUE + f"\nUse the chain to choke the first guard's neck again"
                                  f"\nEnter 'choke' or 'ch' - ")
                if a1_attack.lower() == "choke" or a1_attack.lower() == "ch":
                    self.g1_health -= 25
                    print(Fore.GREEN + "\nYeaahh! You have killed the first guard")
                    time.sleep(2)
                else:
                    print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
                    time.sleep(3)
                    a1()
            a1()

            print(Fore.RED + "\nOh no! the other Guard attacks you from behind")
            self.char_health -= np.random.randint(5, 10)
            print(Fore.YELLOW + "Your Health: " + str(self.char_health))
            History.elevels_3a(self, enemy)
        else:
            print(Fore.RED + "\nWhat's that? Enter the right command or you're dead!")
            time.sleep(3)
            History.elevels_3(self)

    def eeqs_1(self, inventory, enemy):  # EAST LEVEL

        eeq_1 = input(Fore.BLUE + "\n\nEnter 'pick' or 'p' to pick the chain - ")

        if eeq_1.lower() == "pick" or eeq_1.lower() == "p":
            self.inventory.append("Steel chain")
            Inventory.view_inventory(self.inventory)
            print(Fore.BLUE + "\n\nThe Castle's getting closer. \n2 GUARDS HAVE SPOTTED YOU!!"
                  "\nYou have to fight them or else the " + self.enemy + " will know that you are alive!")
            History.elevels_3(self)

        else:
            print(Fore.RED + "\n Nah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.eeqs_1(self, inventory, enemy)

    def elevels_2(self, char_name, char_type):  # EAST LEVEL

        elevel_2 = input(Fore.BLUE + "\nEnter 'climb' or 'c' to climb on the bark and resume your journey - ")

        if elevel_2.lower() == "climb" or elevel_2.lower() == "c":
            print(Fore.BLUE + "\n\nYou are a brave thing! Good job " + self.char_type + " " + self.char_name + "!!")
            MainChar.char_3a(self, char_name, char_type)
            print(Fore.RED + f"\nKnowing that you have drowned, the " + self.enemy + " and " + self.enemy_pronouns[1] +
                  " men, think that you're dead now"
                  f"\n\n Haha! use this as an opportunity as they will be at ease now."
                  f"\nOn your way, you find an abandoned heavy steel chain, which might be useful for your protection")
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter any key to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.eeqs_1(self, inventory, enemy)  # after displaying the help page, the game continue automatically
            else:
                print()
                History.eeqs_1(self, inventory, enemy)  # If user entered any key other then the specified ones, then the game continue

        else:
            print(Fore.RED + "\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.elevels_2(self, char_name, char_type)

    def elevels_1(self):  # Start of the east direction

        elevel_1 = input(Fore.BLUE + f"\n Enter 'hold' or 'h' to hold on to that bark - ")

        if elevel_1.lower() == "hold" or elevel_1.lower() == 'h':
            print(Fore.BLUE + "\n\nYes! you are now hanging on to the bark")
            History.elevels_2(self, char_name, char_type)

        else:
            print(Fore.RED + "\n\nPlease enter a valid command!")
            time.sleep(3)
        History.elevels_1(self)

################################################### INTRO #####################################################################

    def levels_2(self, char_name, char_type, enemy):  # asking user which direction she/he would like to go

        print(Fore.YELLOW + f"You are now at a junction, on the way towards the " + self.enemy + " 's Castle. ")
        time.sleep(4)
        print(Fore.BLUE + f"\nYou have 3 ways to move ahead. North, South and East. ")
        time.sleep(3)

        level_2 = input(Fore.YELLOW + f"Enter North or n to move to the North direction "
                        f"\nor Enter East or e to move towards the East direction "
                        f"\nor Enter South or s to move towards the South direction \n- ")

        if level_2.lower() == "North" or level_2.lower() == "n":  # NORTH LEVEL
            print(Fore.BLUE + "\n\nYou have now headed towards the North, running through a farmland"
                  "\nand on your way you see many soldiers from afar, searching for you")
            time.sleep(4)
            print(Fore.BLUE + "\nBut you have managed to continue moving in disguise. ")
            time.sleep(4)
            print(Fore.BLUE + "\nOn your way you find an abandoned knife and a footwear, "
                  "which would be very useful for you on your mission. ")
            History.eqs(self, inventory, char_name, char_type)  # will call the north direction's function

        elif level_2.lower() == "East" or level_2.lower() == "e":  # EAST LEVEL
            print(Fore.BLUE + f"\n\n You have now headed towards the East, besides you flows a silent and cold river"
                  "\n You are walking in disguise")
            time.sleep(4)
            print(Fore.BLUE + "\n You see few men are heading towards you with their cattle, they seem to be harmless "
                  "\nYou are passing them without eye contact")
            time.sleep(6)
            print(Fore.RED + f" \n\nTHEY HAVE PUSHED YOU IN THE RIVER ! "
                             f"It seems they were the " + self.enemy + " 's men!")
            time.sleep(4)
            print(Fore.BLUE + f"\n You are drowning and flowing along with the river. "
                              f"You see a tree's bark hanging upon the river")
            History.elevels_1(self) # will call the east direction's function

        elif level_2.lower() == "South" or level_2.lower() == "s":  # SOUTH LEVEL
            print(Fore.BLUE + "\nYou have entered a temple.")
            time.sleep(3)
            print(Fore.BLUE + "\nYou see people busy worshipping God")
            History.slevels_1(self)  # will call the south direction's function

        else:
            print(Fore.RED + f"\n\nPlease enter a valid direction " + self.char_type + " " + self.char_name + "!")
            time.sleep(3)
            History.levels_2(self, char_name, char_type, enemy)

    def levels_1(self, char_name, char_type, char_health, enemy_name, enemy, enemy_pronouns):

        print(Fore.BLUE + f"\n\n\n" + self.char_type + " " + self.char_name + " You're now on the run, "
              "as after killing your parents, \n" + self.enemy + " " + self.enemy_name + " 's men are after you! ")
        time.sleep(5)
        print(Fore.BLUE + "\nBut this can't stop you from killing the " + self.enemy + " and taking on the throne.")
        time.sleep(3)
        weapon_1 = input(Fore.BLUE +
                         "\nSince you are on the run and in a hurry, you have decided to take any one weapon "
                         "\nfrom your storeroom as soon as possible! Enter your own weapon of choice \n- ")
        Inventory.load_inventory(self.inventory, weapon_1)
        Inventory.view_inventory(self.inventory)
        time.sleep(2)
        print(Fore.BLUE + "\n\nRunning from your shelter, you are currently hiding in a jungle, "
              "\nyou have to get to the " + self.enemy + " ASAP! "
              "and kill " + self.enemy_pronouns[2] + "\n when " +
              self.enemy_pronouns[0] + " is ALONE! and UNARMED! "
              "\nIt's Dusk and you are hungry"
              "You see many coconuts fallen from the coconut trees ")
        time.sleep(7)
        level_1 = input(Fore.GREEN + "Your health is now: " + str(self.char_health) +
                        "\n\n Press 'eat' or 'e' to eat the fallen coconuts - ")

        if level_1.lower() == "eat" or level_1.lower() == "e":
            print(Fore.GREEN + f"\nYou ate the coconuts and gained 10 health!")
            self.char_health += 10
            print(Fore.YELLOW + "\nYour health is now: " + str(self.char_health))
            e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                      + Fore.BLUE + " or \n Enter 'z' to continue - ")  # Will ask user what to do next
            if e.lower() == "exit":  # option to exit the game
                print(Fore.YELLOW + "BA BYE")
                registration.dashboard(name, userdata)
            elif e.lower() == "help":  # option to open the help page
                help = open("../resources/help_cp.txt", "r")
                h = help.read()
                print(Fore.YELLOW + h)
                History.levels_2(self, char_name, char_type, enemy)  # after displaying the help page, the game continue automatically
            elif e.lower() == "z":
                print()
                History.levels_2(self, char_name, char_type, enemy)  # If user entered this key other then the specified ones, then the game continue
            else:
                print("Please enter valid command")
        else:
            print(Fore.RED + "\nUghh! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.levels_1(self, char_name, char_type, char_health, enemy_name, enemy, enemy_pronouns)  # calling the same function again

    def intro(self, char_name, char_type, char_health, enemy, enemy_pronouns, enemy_name):

        print(Fore.YELLOW + f"\n\n\n\n\nYou're now in the --> "
              f"\n                                                                               *HISTORIC ERA*")
        time.sleep(5)
        print(Fore.BLUE + f"\n\nBorn in the ANCIENT INDUS VALLEY EMPIRE, "
              f"to a magical family, \nYou, " + self.char_name +
              " had seen your family being gifted with a magical Gem from your ancestors ,\n")
        time.sleep(7)
        print(Fore.BLUE + "\nThe Gem had powers to rule the entire human race, Your parents owned the Gem"
              "\nBut soon the the Gems attracted the empire's " + self.enemy + ". "
              + self.enemy + " " + self.enemy_name + " and " + enemy_pronouns[2] +
              " greed for power.")
        time.sleep(5)
        print(Fore.BLUE + "\nOne day " + enemy_pronouns[2] + " manages to get your parents killed, "
              "by torturing them in his Castle's cage"
              "\nThe Gem is now with " + self.enemy + " " + self.enemy_name + " and " +
              enemy_pronouns[1] +
              " has placed it in " + enemy_pronouns[2] + " throne"
              "\nThe entire world is under " + enemy_pronouns[2] + " control now. This breaks you from within.")
        time.sleep(10)
        print(Fore.BLUE + "\nBut, not for long! you are now decided to Kill the person, who killed your parents, "
              "THE " + self.enemy.upper() + " ! "
              "\nand take the Gem, your Gem! back!!. ")
        time.sleep(7)
        print(Fore.BLUE + "\nFor you, " + self.char_type + " " + self.char_name +
              " are the rightful owner of your family's treasure! and to rule for generations to come!")
        time.sleep(2)
        e = input(Fore.RED + "\nEnter 'Exit' to exit game or " + Fore.GREEN + "\n'help' to see the Help section"
                  + Fore.BLUE + " or \n Enter 'z' to continue - ")  # Will ask user what to do next
        if e.lower() == "exit":  # option to exit the game
            print(Fore.YELLOW + "BA BYE")
            registration.dashboard(name, userdata)
        elif e.lower() == "help":  # option to open the help page
            help = open("../resources/help_cp.txt", "r")
            h = help.read()
            print(Fore.YELLOW + h)
            History.levels_1(self, char_name, char_type, char_health, enemy_name, enemy, enemy_pronouns)  # after displaying the help page, the game continue automatically
        elif e.lower() == "z":
            print()
            History.levels_1(self, char_name, char_type, char_health, enemy_name, enemy,
                             enemy_pronouns)  # If user entered this key other then the specified ones, then the game continue
        else:
            print("Please enter valid command")


history = History(username, password, char_name, char_type, char_gender,  # defining Class History into the variable 'history'
                  char_health, enemy, enemy_name, enemy_pronouns,
                  enemy_health, g1_health, g2_health, inventory,
                  w1_health, w2_health, l1_health, l2_health, new_userdata)
history.intro(char_name, char_type, char_health, enemy, enemy_pronouns, enemy_name)  # calling the intro function (from Class History) via variable 'history'
