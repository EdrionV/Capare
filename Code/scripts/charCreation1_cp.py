
class MainChar:

    char_health = 100

    def __init__(self, username, char_name, char_type, char_gender, power):
        self.username = username
        self.char_name = char_name
        self.char_type = char_type
        self.char_gender = char_gender
        self.power = power

    def char_1(username):

        char_name = input(f"\n So," + username + ", "
                          "what will be your name in C.A.P.A.R.E.? "
                          "Please Enter your Avatar's name - ")
        return char_name

    def char_2(self):

        char_type = input("What type of a Avatar is this? "
                          "\n(For example: Knight, Witch, Spy, etc) - ")
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

    def char_3a(self, char_name, char_type):

        if self.char_gender.lower() == 'male' or self.char_gender.lower() == 'm':
            print("\nYou are an awesome Man!!. " + self.char_name+" ! the great " + self.char_type)
        else:
            print("\nYou are a fearless woman!!. " + self.char_name+" ! the great " + self.char_type)

