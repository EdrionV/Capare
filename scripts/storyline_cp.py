import sys           #to terminate the program
import random
#import scripts.enemyCreation_cp
#import gameMain_cp
import time
#from scripts import charCreation1_cp
from scripts.inventory_cp import Inventory
from scripts.charCreation1_cp import MainChar
from registration_cp import home, username, password
#from scripts.registration_cp import home
from scripts.enemyCreation_cp import MainEnemy

#username = username
#password = password
char_name = MainChar.char_1(username)
char_type = MainChar.char_2(username)
char_gender = MainChar.char_3(char_name, char_type)
enemy_info = MainEnemy.enemy_details()
enemy_name = enemy_info[0]
enemy_pronouns = enemy_info[1]
inventory = []
char_health = 100

# from inventory_cp import inventory
#char_health = MainChar.char_health

# def view_live_inventory(inventory):
#     for i in range(len(inventory)):
#         # print(i)
#         print(inventory[i])
class History:
    inventory = []
    char_name = char_name
    char_type = char_type
    char_gender = char_gender
    #enemy_info = MainEnemy.enemy_details()
    enemy_name = enemy_name
    enemy_pronouns = enemy_pronouns
    char_health = 100

    def __init__(self, username, password, char_name, char_type, char_gender, char_health, enemy_name, enemy_pronouns, inventory):
        self.username = username
        self.password = password
        self.char_name = char_name
        self.char_type = char_type
        self.char_gender = char_gender
        self.enemy_name = enemy_name
        self.enemy_pronouns = enemy_pronouns
        self.inventory = inventory
        self.char_health = char_health
################################################### SOUTH CODE FROM THE BOTTOM #####################################################################
    char_health = 100

    def slevels_2(self):
        slevel_2 = input("Enter 'leave' or 'l' to leave the temple and get back to the junction - ")
        if slevel_2.lower() == "leave" or slevel_2.lower() == "l":
            print()
            History.levels_2(self)

        else:
            print("Enter valid command + kq + !!")
            time.sleep(3)
            History.slevels_1(self)

    def slevels_1(self):
        slevel_1 = input("\nEnter 'pray' or 'p' if you wish to worship OR "
                         "\n Enter 'leave' or 'l' to leave the temple and get back to the junction ")
        if slevel_1.lower() == "pray" or slevel_1.lower() == "p":
            print("Silence is the word your mind is achieving, while you worship and pray")
            time.sleep(7)
            print("You are now refreshed and pumped up to continue your mission")
            time.sleep(5)
            History.slevels_2(self)


        elif slevel_1.lower() == "leave" or slevel_1.lower() == "l":
            print()
            History.levels_2(self)

        else:
            print("Enter valid command + kq + !!")
            time.sleep(3)
            History.slevels_1(self)

################################################### NORTH CODE FROM THE BOTTOM #####################################################################

    def ends(self):
        end = input("\n\n\n\n\n\nHey CAPARE member, "
                    "\nCongratulations!! on your Victory!"
                    "\nEnter 'exit' to return to the main menu "
                    "\nand to explore other Avatar stories!!")
        if end.lower() == "exit":
            print("Exited")  #gameMain_cp.char()

        else:
            print("Wrong command!")
            time.sleep(3)
            History.ends(self)

    def levels_2e(self):
        level_2e = input(f"Pick up his eternal throne and wear it Witch "
                         + self.char_name + "Enter 'wear' or 'w' to wear the throne - ")
        if level_2e.lower() == "wear" or level_2e.lower() == "w":
            print("\n\n\n!!!!!!VICTORY!!!!!!"
                  "\nYour anger has achieved its satisfaction. "
                  "\nA sense of peace you feel within you"
                  "\nYou have conquered this Era Witch " + self.char_name +
                  "\n!!!! This Empire is all yours now and your revenge is complete"
                  "\n\n !!!!!!!VICTORY!!!!!VICTORY!!!!!!"
                  "\nWitch " + self.char_name +
                  "has captured the PAST of the INDUS VALLEY EMPIRE - "
                  "\n\n*THE ANCIENT ERA*")
            History.ends(self)
            #end() loop

        else:
            print("\nCome on! You can't make mistakes at this point. "
                  "\nEnter the correct command")
            time.sleep(3)
            History.levels_2e(self)

    def levels_2d(self):
        level_2d = input(f"\nUsing your knife, finish him! Enter 'knife' or 'k' - ")
        if level_2d.lower() == "knife" or level_2d.lower() == 'k':
            print("\nThe King is finally DEAD. He is down on your feet, bleeding."
                  "\nThere is no other thing as happy as this, for you")
            History.levels_2e(self)

        else:
            print("\nWhat's that ? Enter the right command")
            time.sleep(3)
            History.levels_2d(self)

    def actions_4(self):
        action_4 = input(f"Enter 'hypno' or 'h' to dive into the King's eyes hypnotising him - ")
        if action_4.lower() == "hypno" or action_4.lower() == "h":
            print(f"\n The King is now all yours Witch " + self.char_name + "!"
                  "\nKill is the only thing which comes to your mind now")
            History.levels_2d(self)

        else:
            print("\nPlease enter correct command before he gets out of your way!")
            time.sleep(3)
            History.actions_4(self)

    def levels_2c(self):

        level_2c = input(f"Enter 'stab' or 's' to kill the 2nd lion - ")
        if level_2c.lower() == "stab" or level_2c.lower() == "s":
            print("Yes! you are finally at your target's doorsteps!"
                  "\n With minimum powers and few tools, you now have to kill the "
                  "King. \nYou have to kill him and wear his crown by which, you will become "
                  "the new Ruler of this Empire! \nYou have to hurry up before anyone else "
                  "enters his room. \n\n You are now standing in the King's room, "
                  "looking straight into his eyes, where his eyes are full of fear and anger "
                  "at the same time. Before he tries to jump out of his window, "
                  "Use your last spell to hypnotise him.")
            History.actions_4(self)

        else:
            print(f"\nWhom are you stabbing ? Enter the correct command please")
            time.sleep(3)
            History.levels_2c(self)

    def levels_2b(self):

        level_2b = input(f"Enter 'stab' or 's' to kill the 1st lion - ")
        if level_2b.lower() == "stab" or level_2b.lower() == "s":
            print(f"Excellent! one down, 1 to go!")
            # score += randint()
            History.levels_2c(self)

        else:
            print("\nWhom are you stabbing ? Enter the correct command please")
            time.sleep(3)
            History.levels_2b(self)

    def actions_3(self):

        action_3 = input(f"\nEnter 'blur' or 'b' to blur the lions - ")
        if action_3.lower() == "blur" or action_3.lower() == "b":
            print("Brilliant! its easy to kill them now with their weak eyesight!")
            History.levels_2b(self)

        else:
            print(f"\nWrong command! There's no time! please press the right command! "
                  f"\nThe lions are coming toward you!")
            time.sleep(3)
            History.actions_3(self)

    def eqs_1(self):

        eq_1 = input(f"Enter 'pick' or 'p' to pick a firelight - ")

        if eq_1.lower() == "pick" or eq_1.lower() == "p":
            print(f"\n\n*Firelight added to your equipment*"
                  f"\n\n Climbing the last floor, you are now right in front, facing the 2 deadly lions!"
                  f"\nBefore taking any further step, you have to use your 'blur vision' spell on the lions")
            History.actions_3(self)

        else:
            print(f"Enter valid command Witch " + self.char_name + "!!")
            time.sleep(3)
            History.eqs_1(self)

    def levels_2a(self):

        level_2a = input(f"\nEnter 'climb' or 'c' to climb the stairs - ")

        if level_2a.lower() == "climb" or level_2a.lower() == "c":
            print(
                f"\n\nYou are now climbing the stairs. On your way up you see Firelights, "
                f"you can pick one of them"
                f" as this will be of great help fighting the Lions upstairs.")
            History.eqs_1(self)

        else:
            print("\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.levels_2(self)

    def actions_2(self):

        action_2 = input(f"\nUse your 'destroy' spell to kill all the guards asleep and to break the front gate"
                         f"Enter 'destroy' or 'd' to initiate this spell - ")

        if action_2 == "destroy" or action_2 == 'd':
            print(f"\n\nWalla! you have now entered the Castle. Your mission is not too far now to be accomplished. "
                  "\n\nThe King is on the top floor, preparing to sleep (forever). The guards are on their rounds"
                  "\nbut currently not outside the King's room. To reach him, you have to quickly climb 2 floors and "
                  "\nface 2 deadly Lions owned by the King to protect himself.")
            History.levels_2(self)
        else:
            print("\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.actions_2(self)

    def actions_1(self):

        action_1 = input("\nPress 'cut throat' or 'ct' to use your 'cut throat' spell - ")

        if action_1 == "cut throat" or action_1 == 'ct':
            print(f"\nYou killed the guard successfully with 20 damage. "
                  f"\nYou are now in front of the castle's front gate. ")
            History.actions_2(self)

        else:
            print("\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.actions_1(self)

    def eqs(self):

        eq = input("\nPress 'pick' or 'p' to collect them")

        if eq.lower() == "pick" or eq.lower() == "p":
            # inventory.append("Footwear")
            # inventory.append("Knife")

            print(f"\n*Knife and Footwear added to your equipment*. "
                  f"\n\nYou are now reaching the Castle's outer North gate. \nPhew! the gaurds are asleep for now")
            time.sleep(2)
            print("\n\n\n\nOh no!  A GUARD HAS SPOTTED YOU WITCH  " + self.char_name + "!!! "
                  "\nBefore he wakes the other guards up and alerts the Castle, you have to do something!!"
                  "\n Use your 'cut throat' spell to shut that guard forever. ")
            History.actions_1(self)

        else:
            print("\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.eqs(self)

################################################### EAST CODE FROM THE BOTTOM #####################################################################

    def ends_e(self):  # EAST LEVEL
        end_e = input("\n\n\n\n\n\nHey CAPARE member, "
                      "\nCongratulations!! on your Victory!"
                      "\nEnter 'exit' to return to the main menu "
                      "\nand to explore your other Avatars!!")
        if end_e.lower() == "exit":
            home()
            MainChar()

        else:
            print("Wrong command!")
            time.sleep(3)
            History.ends_e(self)

    def elevels_riddle(self):

        for i in range(4):
            riddle = input(f"\n\nRIDDLE - What can cut like a knife and sting like a bee. "
                           f"\nCarry truth and lies but never move or speak. What are we? "
                           f"\n(You have just 3 ATTEMPTS until the"
                           f"King's guards are here)")
            if riddle.lower() == "words" or riddle.lower() == "word":
                print("\n\n\n!!!!!!VICTORY!!!!!!"
                      "\nYour anger has achieved its satisfaction. "
                      "\nA sense of peace you feel within you"
                      "\nYou have conquered this Era " + self.char_type + + self.char_name +
                      "\n!!!! This Empire is all yours now and your revenge is complete"
                      "\n\n !!!!!!!VICTORY!!!!!VICTORY!!!!!!"
                      "\nWitch " + self.char_name +
                      "has captured the PAST of the INDUS VALLEY EMPIRE - "
                      "\n\n*THE HISTORIC ERA*")
                time.sleep(3)
                History.ends_e(self)
                break
            else:
                print(f"\n\nWrong answer ! - Give it another go (Hint - One has to be careful while using us)")
                time.sleep(3)

        else:
            print(f"\n\nTIME'S UP!! The guards have come and have lynched you! "
                  f"\nYOU'RE DEAD!!")
            time.sleep(3)
            home()
            MainChar()

    def elevels_5a(self):  # EAST LEVEL
        elevel_5a = input(f"Pick up his eternal throne and wear it  " + self.char_type +
                          + self.char_name + "Enter 'wear' or 'w' to wear the throne - ")
        if elevel_5a.lower() == "wear" or elevel_5a.lower() == "w":
            print("\n\nThe THRONE is magical and it listen to the one who understands it"
                  "\nIn order to own the throne, You have to solve a riddle by giving the correct answer")
            History.elevels_riddle(self)

        else:
            print("\nCome on! You can't make mistakes at this point. "
                  "\nEnter the correct command")
            time.sleep(3)
            History.elevels_5a(self)

    def elevels_5(self):  # EAST LEVEL
        elevel_5 = input(f"\n\nYou are heading towards the king. With no tools left, "
                         f"\nyou have fight a hand to hand combat with him"
                         f"\nEnter 'fight' or 'f' to fight the King - ")
        if elevel_5.lower() == "fight" or elevel_5.lower() == "f":
            char_1 = MainChar("", 50)
            guard_2 = MainChar("Dan", 50)
            char_1.attack()
            guard_2.damage(char_1.power)
            print("\nThe King is finally DEAD. He is down on your feet, bleeding."
                  "\nThere is no other thing as happy as this, for you")
            History.elevels_5a(self)

        else:
            print(f"Wrong entry! Please try again - ")
            time.sleep(3)
            History.elevels_5(self)

    def elevels_4b(self):  # EAST LEVEL

        elevel_4b = input(f"\nEnter 'enter' or 'e' to open the door and enter the dining area quietly - ")
        if elevel_4b.lower() == "enter" or elevel_4b.lower() == "e":
            print("\n\nTHE KING IS FINALLY IS FRONT OF YOU! This is your chance to kill him and take on his throne"
                  "to rule the entire empire! You see him filled with anger and fear. Before he runs away, you have"
                  "to eliminate him!")
            History.elevels_5(self)

        else:
            print(f"\nWhere are you trying to enter ? Please enter correct command")
            time.sleep(3)
            History.elevels_4b(self)

    def elevels_4a(self, inventory):  # EAST LEVEL

        elevel_4a = input(f"\nEnter 'kill' or 'k' to kill the wolf!! - ")
        if elevel_4a.lower() == "kill" or elevel_4a.lower() == "k":
            # char_1 = MainChar("", 50)
            # guard_2 = MainChar("Dan", 50)
            # char_1.attack()
            # guard_2.damage(char_1.power)
            print(f"\n\n The steel chain is now of no use and broken")
            inventory.remove()
            print(f"\nBefore anyone else spots you, you have to enter the dining area")
            History.elevels_4b(self)

        else:
            print(f"\nEnter valid command !")
            time.sleep(3)
            History.elevels_4a(self)

    def elevels_4(self):  # EAST LEVEL

        elevel_4 = input("\nThe Wolf has spotted you and it's coming towards you!!"
                         "\nUsing the Firelight and the steel chain, kill the hungry wolf"
                         "\nEnter 'kill' or 'k' to get rid of the wolf - ")
        if elevel_4.lower() == "kill" or elevel_4.lower() == "k":
            # char_1 = MainChar("", 50)
            # guard_2 = MainChar("Dan", 50)
            # char_1.attack()
            # guard_2.damage(char_1.power)
            print(f"\n\nBravo!! The wolf is dead ! and the wait is finally over"
                  f"\nThere is nothing stopping you from entering the dining area")
            time.sleep(2)
            print(f"\n\n\nOh wait! YOU HAVE BEEN ATTACKED BY ANOTHER WOLF FROM BEHIND!!!!!!")
            History.elevels_4a(self)

        else:
            print(f"\nEnter valid command !")
            time.sleep(3)
            History.elevels_4(self)

    def eeqs_2(self):  # EAST LEVEL

        eeq_2 = input("\n\nYou see many Firelights hanging around the backyard. You can use this "
                      "to frighten the wolf and kill it with the steel chain"
                      "Enter 'fire' or 'f' to pick one Firelight - ")

        if eeq_2.lower() == "fire" or eeq_2.lower() == "f":
            inventory.append("Firelight")
            inventory.view()
            History.elevels_4(self)

        else:
            print("\n Nah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.eeqs_2(self)

    def message(self):  # EAST LEVEL

        message_1 = input("\n\nEnter 'listen' or 'l' to hear what the guard has to say - ")
        if message_1.lower() == "listen" or message_1.lower() == "l":
            print(f"\n\nGUARD: 'THE KING IS IN HIS DINING HALL ALONE, PREPARING FOR DINNER'"
                  f"\n\n After listening to the now dead man, you head into the castle."
                  f"\nHiding yourself you have managed to reach the castle's backyard, "
                  f"\nfrom where you can enter the dining"
                  f"hall, through it's back door. \nYou are now at the backyard and you see a "
                  f"hungry wolf roaming around the backyard"
                  f"\nYou have to kill the wolf to enter the back door of the dining hall.")
            History.eeqs_2(self)

        else:
            print("\n Invalid command! Please re-enter")
            time.sleep(3)
            History.message(self)

    def elevels_3a(self):  # EAST LEVEL

        elevel_3a = input(f"\n\nBut you have to kill that guard ! Enter 'kill' or 'k' to finish him! - ")
        if elevel_3a.lower() == "kill" or elevel_3a.lower() == "k":
            print("\nHurray! another one bites the dust!")
            # char_1 = MainChar("", 50)
            # guard_2 = MainChar("Dan", 50)
            # char_1.attack()
            # guard_2.damage(char_1.power)
            print(f"\n\nWhile the guard is breathing his lasts, you try to ask him where is the King?? is he alone??")
            History.message(self)

        else:
            print("\nWhat's that? Enter the right command or you're dead!")
            time.sleep(3)
            History.elevels_3a(self)

    def elevels_3(self):  # EAST LEVEL

        elevel_3 = input(f"\nUse the chain to choke the first guard's neck"
                         f"\nEnter 'choke' or 'ch' - ")

        if elevel_3.lower() == "choke" or elevel_3.lower() == "ch":
            MainChar.health -= 10
            print("\nYeaahh! You have killed the first guard")
            time.sleep(2)
            print("\nOh no! the other Guard attacks you from behind")
            #guard_2 = enemyCreation_cp.Guard("Max", 10)
            #you = enemyCreation_cp.Guard(+ gameMain_cp.char_type + gameMain_cp.char_name + 100)
            #guard_2.attack()
            #you.damage(guard_2.power)
            History.elevels_3a(self)

        else:
            print("\nWhat's that? Enter the right command or you're dead!")
            time.sleep(3)
            History.elevels_3(self)

    def eeqs_1(self, inventory):  # EAST LEVEL

        eeq_1 = input("\n\nEnter 'pick' or 'p' to pick the chain - ")

        if eeq_1.lower() == "pick" or eeq_1.lower() == "p":
            self.inventory.append("Steel chain")
            self.inventory.view()
            print("\n\nThe Castle's getting closer. 2 GUARDS HAVE SPOTTED YOU!!"
                  "\nYou have to fight them or else the King will know you are alive!")
            History.elevels_3(self)

        else:
            print("\n Nah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.eeqs_1(inventory)

    def elevels_2(self, char_name, char_type):  # EAST LEVEL

        elevel_2 = input("\nEnter 'climb' or 'c' to climb on the bark and resume your journey - ")

        if elevel_2.lower() == "climb" or elevel_2.lower() == "c":
            print("\n\nYou are a brave thing! Good job " + self.char_type + self.char_name + "!!")
            MainChar.char_3a(self)
            print(f"\nKnowing that you have drowned the King and his men think you're dead now"
                  f"\n\n Haha! use this as an opportunity as they will be at ease now."
                  f"\nOn your way, you find an abandoned heavy steel chain, which might be useful for your protection")
            History.eeqs_1(self)

        else:
            print("\nNah! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.elevels_2(char_name, char_type)

    def elevels_1(self):  # EAST LEVEL

        elevel_1 = input(f"\n Enter 'hold' or 'h' to hold on to that bark - ")

        if elevel_1.lower() == "hold" or elevel_1.lower() == 'h':
            print("\n\nYes! you are now hanging on to the bark")
            History.elevels_2(self)

        else:
            print("\n\nPlease enter a valid command!")
            time.sleep(3)
        History.elevels_1(self)

################################################### INTRO #####################################################################

    def levels_2(self):

        print(f"You are now at a junction, on the way towards to + kq +'s Castle. ")
        time.sleep(4)
        print(f"\nYou have 3 ways to move ahead. North, South and East. ")
        time.sleep(4)

        level_2 = input(f"Enter North or n to move to the North direction "
                        f"\nor Enter East or e to move towards the East direction "
                        f"\nor Enter South or s to move towards the South direction - ")

        if level_2.lower() == "North" or level_2.lower() == "n": # NORTH LEVEL
            print("\n\nYou have now headed towards the North, running through a farmland"
                  "\nand on your way you see many soldiers from afar, searching for you")
            time.sleep(4)
            print("\nBut you have managed to continue moving in disguise. ")
            time.sleep(4)
            print("\nOn your way you find an abandoned knife and a footwear, "
                  "which would be very useful for you on your mission. ")
            History.eqs(self)

        elif level_2.lower() == "East" or level_2.lower() == "e":  # EAST LEVEL
            print(f"\n\n You have now headed towards the East, besides you flows a silent and cold river"
                  "\n You are walking in disguise")
            time.sleep(4)
            print("\n You see few men are heading towards you with their cattle, they seem to be harmless "
                  "\nYou are passing them without eye contact")
            time.sleep(5)
            print(f" \n\nTHEY HAVE PUSHED YOU IN THE RIVER ! It seems they were the + kq +'s men")
            time.sleep(4)
            print(f"\n You are drowning and flowing along with the river. You see a tree's bark hanging upon the river")
            History.elevels_1(self)

        elif level_2.lower() == "South" or level_2.lower() == "s":  # SOUTH LEVEL
            print("You have entered a temple.")
            time.sleep(3)
            print("You see people busy worshipping God")
            History.slevels_1(self)

        else:
            print(f"\n\nPlease enter a valid direction Witch " + self.char_name)
            time.sleep(3)
            History.levels_2(self)

    def levels_1(self, char_name, char_type, char_health):

        print(f"\n" + self.char_type + "" + self.char_name + "You're now on the run, "
              "as after killing your parents, the + kq + "" + kq_name + 's men are after you! ")
        time.sleep(5)
        print("\n But this can't stop you from killing the + kq + and taking on the throne.")
        time.sleep(3)
        weapon_1 = input("! \nSince you are on the run and in a hurry,you have decided to take any one weapon "
                         "from your storeroom as soon as possible! Enter your own weapon of choice - ")
        Inventory.load_inventory(self.inventory, weapon_1)
        Inventory.view_inventory(self.inventory)
        time.sleep(2)
        print("\n\nRunning from your shelter, you are currently hiding in a jungle, "
              "\nyou have to get to the + kq + ASAP! "
              "and kill " + self.enemy_pronouns[1] + " when + k_gender1 + is ALONE! and UNARMED! "
              "\nIt's Dusk and you are hungry"
              "You see many coconuts fallen from the coconut trees ")
        time.sleep(7)
        level_1 = input("Your health is now: " + str(self.char_health) +
                        "\n\n Press 'eat' or 'e' to eat the fallen coconuts - ")

        if level_1.lower() == "eat" or level_1.lower() == "e":
            print(f"\nYou ate the coconuts and gained 10 health!")
            self.char_health += 10
            History.levels_2()

        else:
            print("\nUghh! there's no such command! Please enter a valid command!")
            time.sleep(3)
            History.levels_1(self, char_name, char_type, char_health)

    def intro(self, char_name, char_type, char_health):

        print(f"\nYou're now in the --> "  
            f"\n                                                                               *HISTORIC ERA*")
        time.sleep(5)
        print(f"\n\nBorn in the ANCIENT INDUS VALLEY EMPIRE, to a magical family, \nYou, " + self.char_name +
            " had seen your family being gifted with a magical Gem from your ancestors ,\n")
        time.sleep(7)
        print("\nThe Gem had powers to rule the entire human race, Your parents owned the Gem"
              "\nBut soon the the Gems attracted the empire's King and his greed for power.")
        time.sleep(5)
        print("\nOne day he manages to get your parents killed, by torturing them in his Castle's cage"
              "\nThe Gem is now with the King and he has placed it in his throne"
              "\nThe entire world is under his control now. This breaks you from within.")
        time.sleep(10)
        print("\nBut, not for long! you are now decided to Kill the person, who killed your parents, THE KING! "
              "\nand take the Gem, your Gem! back!!. ")
        time.sleep(7)
        print("\nFor you, " + self.char_type + "" + self.char_name +
              " are the rightful owner of your family's treasure! and to rule for generations to come!")
        time.sleep(2)

        History.levels_1(self, char_name, char_type, char_health)


history = History(username, password, char_name, char_type, char_gender, char_health, enemy_name, enemy_pronouns, inventory)
history.intro(char_name, char_type, char_health)


