import sys


class User:
    def __init__(self, username):
        self.username = username
        self.password = self.setPassword()

    def setPassword(self):
        userChoice = input("Set a password for your account: ")
        return userChoice

    def checkPassword(self):
        i = 3
        userPassword = input("Please enter your password: ")
        while(i > 1 and userPassword != self.password):
            i = i - 1
            userPassword = input(f"Incorrect password. Try again. You have {i} tries left. ")
        if(userPassword != self.password):
            print("You didn't provide a correct password. Exiting program.")
            sys.exit()
        else:
            print(f"Welcome, {self.username}!")


jachu = User("Jachu")
jachu.checkPassword()