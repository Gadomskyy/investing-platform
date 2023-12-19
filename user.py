import sys
import dbase_conn
from portfolio import Portfolio


class User:
    def __init__(self):
        self.database = dbase_conn.Database()
        self.database.createOrConnectDatabase("investingDB")
        self.portfolio = Portfolio(self)

    def register(self):
        self.username = self.setUsername()
        self.password = self.setPassword()
        self.database.createUserRecord(self.username, self.password)

    def login(self):

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        userRecord = self.database.collection.find_one({"name": username, "password": password})

        if userRecord:
            print("Login successful!")
            # Set user attributes based database record
            self.username = userRecord["name"]
            self.password = userRecord["password"]
            self.portfolio.stocks = userRecord.get("stocks", {})
            self.portfolio.balanceHistory = userRecord.get("logs", {})
        else:
            print("Invalid username or password. Please try again.")


    def setUsername(self):
        userChoice = input("Select a username for your account: ")
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

x = User()
x.login()
x.portfolio.addBalance(1000)
