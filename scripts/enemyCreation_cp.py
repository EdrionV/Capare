import numpy as np
#from registration_cp import credentials
#from registration_cp import username, password
#from scripts.charCreation1_cp import MainChar
#from scripts import gameMain_cp
#username = username
#password = password

# char_name = MainChar.char_1(username)
# char_type = MainChar.char_2(username)
# char_gender = MainChar.char_3(char_name, char_type)

class MainEnemy:


    # def __init__(self, kq_name):
    #     self.kq_name = kq_name
    #     # self.power = power

    def enemy_details():

        enemy = input("Would you like your main enemy to be a King or a Queen? "
                   "Enter 'king' or 'k' for King and 'queen' or 'q' for Queen - ")

        if enemy.lower() == "king" or enemy.lower() == "k":
            enemy_pronouns = ["he", "him"]
            enemy_name = input("What would you name this King ? - ")
            enemy_info = [enemy_name, enemy_pronouns]
            return enemy_info

        elif enemy.lower() == "queen" or enemy.lower() == "q":
            enemy_pronouns = ["she", "her"]
            enemy_name = input("What would you name this Queen ? - ")
            enemy_info = [enemy_name, enemy_pronouns]
            return enemy_info

        else:
            print("Enter valid command!")
            MainEnemy.enemy_details()

    def attack(enemy_name, enemy, char_type, char_name):
        enemy_power = np.random.randint(10, 15)
        print(enemy + "" + enemy_name + "attacks "+ char_type + "" + char_name +
              "for " + enemy_power + "damage!")
        return enemy_power

    # def damage(self, enemy_health, enemy_name, enemy):
    #     self.enemy_power -= health
    #     print(enemy + "" + enemy_name + "'s health status:" + {self.power} + "(costed" + {health} + "damage)")

# enemy_info = MainEnemy.enemy_details()
# enemy_name = enemy_info[0]
# enemy_pronouns = enemy_info[1]
# print(enemy_name)
# print(enemy_pronouns[0])
# print(enemy_pronouns[1])

# king_1 = King("Ryan", 20)
# you = King("Dan", 100)
# king_1.attack()
# you.damage(king_1.power)


class Guard:

    def __init__(self, g_name, power):
        self.g_name = g_name          #input("Enter the guard's name - ")
        self.power = power

    def attack(self):
        print(f"Guard {self.g_name} attacks you for {self.power} damage!")

    def damage(self, health):
        self.power -= health
        print(f"Your health status: {self.power} (costed {health} damage))")


# guard_1 = Guard("Max", 10)
# you = Guard("Dan", 100)
# guard_1.attack()
# you.damage(guard_1.power)

#
#
# # class Emperor:
# #
#
# class Gang:
#     health = 250
#     attack = {"fight": 10}
#
#     def __init__(self, ga_name, damage):
#         self.ga_name = ga_name
#         self.damage = damage
#         self.attack = "fight"
#
#     def attack(self):
#         print(f"{self.ga_name} attacks you for {self.health} damage")
#
#
# # class Leader:
#
# class Watchdog:
#     health = 250
#     attack = {"Bite": 15}
#
#     def __init__(self, wd_name, damage):
#         self.wd_name = wd_name
#         self.damage = damage
#         self.attack = "Bite"
#
#     def attack(self):
#         print(f"{self.wd_name} attacks you for {self.health} damage")
