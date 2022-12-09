# def intro(self):
#     print(f"\nYou're now in the --> "
#           f"\n                                                                               *ANCIENT ERA*")
#     print(f"\n\nBorn in the ANCIENT INDUS VALLEY EMPIRE, to a poor family, " + gameMain_cp.char_name +
#           " had seen her parents getting involved in dark magic, in order to be rich,\n"
#           "Seeing her parents practicing this kind of magic and giving sacrifices of human and animal lives,\n"
#           "she herself became fond of this magic. Evidencing this havoc in the empire,"
#           " with numerous incidents of people dying suspiciously,\nthe King of the INDUS VALLEY EMPIRE"
#           " ordered his guards to cage" + gameMain_cp.char_name + "'s parents and torture them. "
#                                                                   "\nUnder pressure of the people of his empire, the king finally decides to get "
#           + gameMain_cp.char_name + "'s parents killed. \n\nThis breaks " + gameMain_cp.char_name + " from within."
#                                                                                                     " But, not for long! She is now on the run to Kill the person, who killed her parents THE KING! "
#                                                                                                     "\nand rule the INDUS VALLEY EMPIRE of the ANCIENT ERA!")
#
#     levels_1()
#
#
# def levels_1():
#     level_1 = input(f"\nWitch " + gameMain_cp.char_name + " You're now on the run, as after killing your parents, "
#                                                           "the King is after you Witch " + gameMain_cp.char_name +
#                     "! \nSince you are new to professional attack, your powers are currently minimal"
#                     "\nBut this can't stop you from killing the king and taking on"
#                     " the throne. \n\nYou are currently hiding in a jungle, you have to get to the King ASAP! "
#                     "and kill him when he is ALONE! and UNARMED! \nIt's Dusk and you have just managed to kill "
#                     "a solider in the forest and have sustained injuries which has cost you 10 damage. ")
#     charCreation1_cp.Witch.health -= 10
#     print("Your health is now: " + charCreation1_cp.Witch.health +
#           "\n\n Press 'eat' or 'e' to eat the soldier's flesh, in order to gain health (10) "
#           "OR press 'continue' or 'c' to move forward - ")
#
#     if level_1.lower() == "eat" or level_1.lower() == "e":
#         print(f"\nYou ate that soldier's juicy flesh and gained 10 health!")
#         charCreation1_cp.Witch.health += 10
#         levels_2()
#     elif level_1.lower() == "continue" or level_1.lower() == "c":
#         print(f"\nYou choose to ignore the soldier's flesh and move forward Witch " + gameMain_cp.char_name)
#         levels_2()
#     else:
#         print("\nUghh! there's no such command! Please enter a valid command!")
#         levels_1()
#
#
# def levels_2():
#     level_2 = input(f"You are now on your way towards to King's Castle. "
#                     f"\nYou have 2 ways to move ahead. North and East. "
#                     f"Enter North or n to move to the North direction "
#                     f"\nor Enter East or e to move towards the East - ")
#
#     if level_2.lower() == "North" or level_2.lower() == "n":
#         print("\n\nYou have now headed towards the North, running through a farmland"
#               "\nand on your way you see many soldiers from afar, searching for you"
#               "\nBut you have managed to continue moving in disguise. "
#               "\nOn your way you find an abandoned knife and a footwear, "
#               "which would be very useful for you on your mission. ")
#         eqs()
#
#     elif level_2.lower() == "East" or level_2.lower() == "e":  # EAST LEVEL
#         print(f"\n\n You have now headed towards the East, besides you flows a silent and cold river"
#               "\n You are walking in disguise"
#               "\n You see few men are heading towards you with their cattle, they seem to be harmless "
#               "\nYou are passing them without eye contact")
#         time.sleep(2)
#         print(f" \n\nTHEY HAVE PUSHED YOU IN THE RIVER ! IT SEEMS THEY WERE THE KING'S MEN"
#               f"\n You are drowning and flowing along with the river. You see a tree's bark hanging upon the river")
#         elevels_1()
#         # east level
#
#     else:
#         print(f"\n\nPlease enter a valid direction Witch " + gameMain_cp.char_name)
#         levels_2()
#
#
# ################################################### EAST CODE STARTS #####################################################################
#
# def elevels_1():  # EAST LEVEL
#
#     elevel_1 = input(f"\n Enter 'hold' or 'h' to hold on to that bark - ")
#
#     if elevel_1.lower() == "hold" or elevel_1.lower() == 'h':
#         print("\n\nYes! you are now hanging on to the bark")
#         elevels_2()
#
#     else:
#         print("\n\nPlease enter a valid command!")
#     elevels_1()
#
#
# def elevels_2():  # EAST LEVEL
#
#     elevel_2 = input("\nEnter 'climb' or 'c' to climb on the bark and resume your journey - ")
#
#     if elevel_2.lower() == "climb" or elevel_2.lower() == "c":
#         print("\n\nYou are a brave thing! Good job " + gameMain_cp.char_type + gameMain_cp.char_name + "!!")
#         gameMain_cp.char3a()
#         print(f"\nKnowing that you have drowned the King and his men think you're dead now"
#               f"\n\n Haha! use this as an opportunity as they will be at ease now."
#               f"\nOn your way, you find an abandoned heavy steel chain, which might be useful for your protection")
#         eeqs_1()
#
#     else:
#         print("\nNah! there's no such command! Please enter a valid command!")
#         elevels_2()
#
#
# def eeqs_1():  # EAST LEVEL
#
#     eeq_1 = input("\n\nEnter 'pick' or 'p' to pick the chain - ")
#
#     if eeq_1.lower() == "pick" or eeq_1.lower() == "p":
#         inventory.append("Steel chain")
#         inventory.view()
#         print("\n\nThe Castle's getting closer. 2 GUARDS HAVE SPOTTED YOU!!"
#               "\nYou have to fight them or else the King will know you are alive!")
#         elevels_3()
#
#     else:
#         print("\n Nah! there's no such command! Please enter a valid command!")
#         eeqs_1()
#
#
# def elevels_3():  # EAST LEVEL
#
#     elevel_3 = input(f"\nUse the chain to choke the first guard's neck"
#                      f"\nEnter 'choke' or 'ch' - ")
#
#     if elevel_3.lower() == "choke" or elevel_3.lower() == "ch":
#         gameMain_cp.MainChar.health -= 10
#         print("\nYeaahh! You have killed the first guard")
#         time.sleep(2)
#         print("\nOh no! the other Guard attacks you from behind")
#         guard_2 = enemyCreation_cp.Guard("Max", 10)
#         you = enemyCreation_cp.Guard(+ gameMain_cp.char_type + gameMain_cp.char_name +, 100)
#         guard_2.attack()
#         you.damage(guard_2.power)
#         elevels_3a()
#
#     else:
#         print("\nWhat's that? Enter the right command or you're dead!")
#         elevels_3()
#
#
# def elevels_3a():  # EAST LEVEL
#
#     elevel_3a = input(f"\n\nBut you have to kill that guard ! Enter 'kill' or 'k' to finish him! - ")
#     if elevel_3a.lower() == "kill" or elevel_3a.lower() == "k":
#         print("\nHurray! another one bites the dust!")
#         char_1 = gameMain_cp.MainChar("", 50)
#         guard_2 = gameMain_cp.MainChar("Dan", 50)
#         char_1.attack()
#         guard_2.damage(char_1.power)
#         print(f"\n\nWhile the guard is breathing his lasts, you try to ask him where is the King?? is he alone??")
#         message()
#
#     else:
#         print("\nWhat's that? Enter the right command or you're dead!")
#         elevels_3a()
#
#
# def message():  # EAST LEVEL
#
#     message_1 = input("\n\nEnter 'listen' or 'l' to hear what the guard has to say - ")
#     if message_1.lower() == "listen" or message_1.lower() == "l":
#         print(f"\n\nGUARD: 'THE KING IS IN HIS DINING HALL ALONE, PREPARING FOR DINNER'"
#               f"\n\n After listening to the now dead man, you head into the castle."
#               f"\nHiding yourself you have managed to reach the castle's backyard, \nfrom where you can enter the dining"
#               f"hall, through it's back door. \nYou are now at the backyard and you see a hungry wolf roaming around the "
#               f"backyard. \nYou have to kill the wolf to enter the back door of the dining hall.")
#         eeqs_2()
#
#     else:
#         print("\n Invalid command! Please re-enter")
#         message()
#
#
# def eeqs_2():  # EAST LEVEL
#
#     eeq_2 = input("\n\nYou see many Firelights hanging around the backyard. You can use this "
#                   "to frighten the wolf and kill it with the steel chain"
#                   "Enter 'fire' or 'f' to pick one Firelight - ")
#
#     if eeq_2.lower() == "fire" or eeq_2.lower() == "f":
#         inventory.append("Firelight")
#         inventory.view()
#         elevels_4()
#
#     else:
#         print("\n Nah! there's no such command! Please enter a valid command!")
#         eeqs_2()
#
#
# def elevels_4():  # EAST LEVEL
#
#     elevel_4 = input("\nThe Wolf has spotted you and it's coming towards you!!"
#                      "\nUsing the Firelight and the steel chain, kill the hungry wolf"
#                      "\nEnter 'kill' or 'k' to get rid of the wolf - ")
#     if elevel_4.lower() == "kill" or elevel_4.lower() == "k":
#         char_1 = gameMain_cp.MainChar("", 50)
#         guard_2 = gameMain_cp.MainChar("Dan", 50)
#         char_1.attack()
#         guard_2.damage(char_1.power)
#         print(f"\n\nBravo!! The wolf is dead ! and the wait is finally over"
#               f"\nThere is nothing stopping you from entering the dining area")
#         time.sleep(2)
#         print(f"\n\n\nOh wait! YOU HAVE BEEN ATTACKED BY ANOTHER WOLF FROM BEHIND!!!!!!")
#         elevels_4a()
#
#     else:
#         print(f"\nEnter valid command !")
#         elevels_4()
#
#
# def elevels_4a():  # EAST LEVEL
#
#     elevel_4a = input(f"\nEnter 'kill' or 'k' to kill the wolf!! - ")
#     if elevel_4a.lower() == "kill" or elevel_4a.lower() == "k":
#         char_1 = gameMain_cp.MainChar("", 50)
#         guard_2 = gameMain_cp.MainChar("Dan", 50)
#         char_1.attack()
#         guard_2.damage(char_1.power)
#         print(f"\n\n The steel chain is now of no use and broken")
#         inventory.remove()
#         print(f"\nBefore anyone else spots you, you have to enter the dining area")
#         elevels_4b()
#
#     else:
#         print(f"\nEnter valid command !")
#         elevels_4a()
#
#
# def elevels_4b():  # EAST LEVEL
#
#     elevel_4b = input(f"\nEnter 'enter' or 'e' to open the door and enter the dining area quietly - ")
#     if elevel_4b.lower() == "enter" or elevel_4b.lower() == "e":
#         print("\n\nTHE KING IS FINALLY IS FRONT OF YOU! This is your chance to kill him and take on his throne"
#               "to rule the entire empire! You see him filled with anger and fear. Before he runs away, you have"
#               "to eliminate him!")
#         elevels_5()
#
#     else:
#         print(f"\nWhere are you trying to enter ? Please enter correct command")
#         elevels_4b()
#
#
# def elevels_5():  # EAST LEVEL
#     elevel_5 = input(f"\n\nYou are heading towards the king. With no tools left, "
#                      f"\nyou have fight a hand to hand combat with him"
#                      f"\nEnter 'fight' or 'f' to fight the King - ")
#     if elevel_5.lower() == "fight" or elevel_5.lower() == "f":
#         char_1 = gameMain_cp.MainChar("", 50)
#         guard_2 = gameMain_cp.MainChar("Dan", 50)
#         char_1.attack()
#         guard_2.damage(char_1.power)
#         print("\nThe King is finally DEAD. He is down on your feet, bleeding."
#               "\nThere is no other thing as happy as this, for you")
#         elevels_5a()
#
#     else:
#         print(f"Wrong entry! Please try again - ")
#         elevels_5()
#
#
# def elevels_5a():  # EAST LEVEL
#     elevel_5a = input(f"Pick up his eternal throne and wear it  " + gameMain_cp.char_type +
#                       + gameMain_cp.char_name + "Enter 'wear' or 'w' to wear the throne - ")
#     if elevel_5a.lower() == "wear" or elevel_5a.lower() == "w":
#         print("\n\nThe THRONE is magical and it listen to the one who understands it"
#               "\nIn order to own the throne, You have to solve a riddle by giving the correct answer")
#         elevels_riddle()
#
#     else:
#         print("\nCome on! You can't make mistakes at this point. "
#               "\nEnter the correct command")
#         elevels_5a()
#
#
# def elevels_riddle():
#     for i in range(4):
#         riddle = input(f"\n\nRIDDLE - What can cut like a knife and sting like a bee. "
#                        f"\nCarry truth and lies but never move or speak. What are we? \n(You have just 3 ATTEMPTS until the"
#                        f"King's guards are here)")
#         if riddle.lower() == "words" or riddle.lower() == "word":
#             print("\n\n\n!!!!!!VICTORY!!!!!!"
#                   "\nYour anger has achieved its satisfaction. "
#                   "\nA sense of peace you feel within you"
#                   "\nYou have conquered this Era " + gameMain_cp.char_type + + gameMain_cp.char_name +
#                   "\n!!!! This Empire is all yours now and your revenge is complete"
#                   "\n\n !!!!!!!VICTORY!!!!!VICTORY!!!!!!"
#                   "\nWitch " + gameMain_cp.char_name +
#                   "has captured the PAST of the INDUS VALLEY EMPIRE - "
#                   "\n\n*THE HISTORIC ERA*")
#             ends_e()
#             break
#         else:
#             print(f"\n\nWrong answer ! - Give it another go (Hint - One has to be careful while using us)")
#
#     else:
#         print(f"\n\nTIME'S UP!! The guards have come and have lynched you! "
#               f"\nYOU'RE DEAD!!")
#         home()
#         gameMain_cp.MainChar()
#
#
# def ends_e():  # EAST LEVEL
#     end_e = input("\n\n\n\n\n\nHey CAPARE member, "
#                   "\nCongratulations!! on your Victory!"
#                   "\nEnter 'exit' to return to the main menu "
#                   "\nand to explore your other Avatars!!")
#     if end_e.lower() == "exit":
#         home()
#         gameMain_cp.MainChar()
#
#     else:
#         print("Wrong command!")
#         ends_e()
#
#
# ################################################### WEST CODE STARTS #####################################################################
#
# def eqs():
#     eq = input("\nPress 'pick' or 'p' to collect them")
#
#     if eq.lower() == "pick" or eq.lower() == "p":
#         # inventory.append("Footwear")
#         # inventory.append("Knife")
#
#         print(f"\n*Knife and Footwear added to your equipment*. "
#               f"\n\nYou are now reaching the Castle's outer North gate. \nPhew! the gaurds are asleep for now")
#         time.sleep(2)
#         print("\n\n\n\nOh no!  A GUARD HAS SPOTTED YOU WITCH  " + gameMain_cp.char_name + "!!! "
#                                                                                           "\nBefore he wakes the other guards up and alerts the Castle, you have to do something!!"
#                                                                                           "\n Use your 'cut throat' spell to shut that guard forever. ")
#         actions_1()
#
#     else:
#         print("\nNah! there's no such command! Please enter a valid command!")
#         eqs()
#
#
# def actions_1():
#     action_1 = input("\nPress 'cut throat' or 'ct' to use your 'cut throat' spell - ")
#
#     if action_1 == "cut throat" or action_1 == 'ct':
#         print(f"\nYou killed the guard successfully with 20 damage. "
#               f"\nYou are now in front of the castle's front gate. ")
#         actions_2()
#
#     else:
#         print("\nNah! there's no such command! Please enter a valid command!")
#         actions_1()
#
#
# def actions_2():
#     action_2 = input(f"\nUse your 'destroy' spell to kill all the guards asleep and to break the front gate"
#                      f"Enter 'destroy' or 'd' to initiate this spell - ")
#
#     if action_2 == "destroy" or action_2 == 'd':
#         print(f"\n\nWalla! you have now entered the Castle. Your mission is not too far now to be accomplished. "
#               "\n\nThe King is on the top floor, preparing to sleep (forever). The guards are on their rounds"
#               "\nbut currently not outside the King's room. To reach him, you have to quickly climb 2 floors and "
#               "\nface 2 deadly Lions owned by the King to protect himself.")
#         levels_2()
#     else:
#         print("\nNah! there's no such command! Please enter a valid command!")
#         actions_2()
#
#
# def levels_2a():
#     level_2a = input(f"\nEnter 'climb' or 'c' to climb the stairs - ")
#
#     if level_2a.lower() == "climb" or level_2a.lower() == "c":
#         print(
#             f"\n\nYou are now climbing the stairs. On your way up you see Firelights, "
#             f"you can pick one of them"
#             f" as this will be of great help fighting the Lions upstairs.")
#         eqs_1()
#
#     else:
#         print("\nNah! there's no such command! Please enter a valid command!")
#         levels_2()
#
#
# def eqs_1():
#     eq_1 = input(f"Enter 'pick' or 'p' to pick a firelight - ")
#
#     if eq_1.lower() == "pick" or eq_1.lower() == "p":
#         print(f"\n\n*Firelight added to your equipment*"
#               f"\n\n Climbing the last floor, you are now right in front, facing the 2 deadly lions!"
#               f"\nBefore taking any further step, you have to use your 'blur vision' spell on the lions")
#         actions_3()
#
#     else:
#         print(f"Enter valid command Witch " + gameMain_cp.char_name + "!!")
#         eqs_1()
#
#
# def actions_3():
#     action_3 = input(f"\nEnter 'blur' or 'b' to blur the lions - ")
#     if action_3.lower() == "blur" or action_3.lower() == "b":
#         print("Brilliant! its easy to kill them now with their weak eyesight!")
#         levels_2b()
#
#     else:
#         print(f"\nWrong command! There's no time! please press the right command! "
#               f"\nThe lions are coming toward you!")
#         actions_3()
#
#
# def levels_2b():
#     level_2b = input(f"Enter 'stab' or 's' to kill the 1st lion - ")
#     if level_2b.lower() == "stab" or level_2b.lower() == "s":
#         print(f"Excellent! one down, 1 to go!")
#         # score += randint()
#         levels_2c()
#
#     else:
#         print("\nWhom are you stabbing ? Enter the correct command please")
#         levels_2b()
#
#
# def levels_2c():
#     level_2c = input(f"Enter 'stab' or 's' to kill the 2nd lion - ")
#     if level_2c.lower() == "stab" or level_2c.lower() == "s":
#         print("Yes! you are finally at your target's doorsteps!"
#               "\n With minimum powers and few tools, you now have to kill the "
#               "King. \nYou have to kill him and wear his crown by which, you will become "
#               "the new Ruler of this Empire! \nYou have to hurry up before anyone else "
#               "enters his room. \n\n You are now standing in the King's room, "
#               "looking straight into his eyes, where his eyes are full of fear and anger "
#               "at the same time. Before he tries to jump out of his window, "
#               "Use your last spell to hypnotise him.")
#         actions_4()
#
#     else:
#         print(f"\nWhom are you stabbing ? Enter the correct command please")
#         levels_2c()
#
#
# def actions_4():
#     action_4 = input(f"Enter 'hypno' or 'h' to dive into the King's eyes hypnotising him - ")
#     if action_4.lower() == "hypno" or action_4.lower() == "h":
#         print(f"\n The King is now all yours Witch " + gameMain_cp.char_name + "!"
#                                                                                "\nKill is the only thing which comes to your mind now")
#         levels_2d()
#
#     else:
#         print("\nPlease enter correct command before he gets out of your way!")
#         actions_4()
#
#
# def levels_2d():
#     level_2d = input(f"\nUsing your knife, finish him! Enter 'knife' or 'k' - ")
#     if level_2d.lower() == "knife" or level_2d.lower() == 'k':
#         print("\nThe King is finally DEAD. He is down on your feet, bleeding."
#               "\nThere is no other thing as happy as this, for you")
#         levels_2e()
#
#     else:
#         print("\nWhat's that ? Enter the right command")
#         levels_2d()
#
#
# def levels_2e():
#     level_2e = input(f"Pick up his eternal throne and wear it Witch "
#                      + gameMain_cp.char_name + "Enter 'wear' or 'w' to wear the throne - ")
#     if level_2e.lower() == "wear" or level_2e.lower() == "w":
#         print("\n\n\n!!!!!!VICTORY!!!!!!"
#               "\nYour anger has achieved its satisfaction. "
#               "\nA sense of peace you feel within you"
#               "\nYou have conquered this Era Witch " + gameMain_cp.char_name +
#               "\n!!!! This Empire is all yours now and your revenge is complete"
#               "\n\n !!!!!!!VICTORY!!!!!VICTORY!!!!!!"
#               "\nWitch " + gameMain_cp.char_name +
#               "has captured the PAST of the INDUS VALLEY EMPIRE - "
#               "\n\n*THE ANCIENT ERA*")
#         ends()
#
#     else:
#         print("\nCome on! You can't make mistakes at this point. "
#               "\nEnter the correct command")
#         levels_2e()
#
#
# def ends():
#     end = input("\n\n\n\n\n\nHey CAPARE member, "
#                 "\nCongratulations!! on your Victory!"
#                 "\nEnter 'exit' to return to the main menu "
#                 "\nand to explore other Avatar stories!!")
#     if end.lower() == "exit":
#         gameMain_cp.char()
#
#     else:
#         print("Wrong command!")
#         ends()

#
#
#
# i = 0
# while i <= 5:
