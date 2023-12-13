import sys
import dbase_conn


class User:
    def __init__(self):
        self.database = dbase_conn.Database()
        self.database.createOrConnectDatabase("investingDB")
        self.username = self.setUsername()
        self.password = self.setPassword()
        self.database.createUserRecord(self.username, self.password)

    def setUsername(self):
        userChoice = input("Select a username for your account. ")
        while len(userChoice) < 3:
            userChoice = input("Your username needs to be at least 3 characters long. Try again. ")
        return userChoice

    def setPassword(self):
        userChoice = input("Set a password for your account: ")
        while len(userChoice) < 6 or not(any(char.isdigit() for char in userChoice)):
            userChoice = input("Your password needs to be at least 6 characters long and contain at least one number. Try again. ")
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
