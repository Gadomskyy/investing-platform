import sys


class User:
    def __init__(self):
        self.username = self.setUsername()
        self.password = self.setPassword()

    def setUsername(self):
        userChoice = input("Select a username for your account. ")
        while len(userChoice) < 3:
            userChoice = input("Your username needs to be at least 3 characters long. Try again. ")
        return userChoice

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


jachu = User()
