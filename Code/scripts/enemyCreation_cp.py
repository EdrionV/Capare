

class MainEnemy:

    def enemy_details():

        enemy_type = input("Would you like your main enemy to be a King or a Queen? "
                           "Enter 'king' or 'k' for King and 'queen' or 'q' for Queen - ")

        if enemy_type.lower() == "king" or enemy_type.lower() == "k":
            enemy_pronouns = ["he", "his", "him"]
            enemy_name = input("What would you name this King ? - ")
            enemy_type = "King"
            enemy_health = 150
            enemy_info = [enemy_name, enemy_pronouns, enemy_type, enemy_health]
            return enemy_info

        elif enemy_type.lower() == "queen" or enemy_type.lower() == "q":
            enemy_pronouns = ["she", "her", "her"]
            enemy_name = input("What would you name this Queen ? - ")
            enemy_type = "Queen"
            enemy_health = 150
            enemy_info = [enemy_name, enemy_pronouns, enemy_type, enemy_health]
            return enemy_info

        else:
            print("Enter valid command!")
            MainEnemy.enemy_details()


class Guard:

    def guard_details():
        g1_health = 50
        g2_health = 50
        guard_info = [g1_health, g2_health]
        return guard_info
