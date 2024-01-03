import sys

import dbase_conn
from portfolio import Portfolio


class User:
    database = dbase_conn.Database()

    def __init__(self):
        self.database.createOrConnectDatabase("investingDB")
        self.portfolio = Portfolio(self)
        self.userRecord = None

    def register(self):
        self.username = self.setUsername()
        self.password = self.setPassword()
        self.database.createUserRecord(self.username, self.password)

    def login(self):

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        self.userRecord = self.findUser(username, password)

        if self.userRecord:
            print("Login successful!")
            # Set user attributes based database record
            self.setUserRecords()
        else:
            if self.isLoginTaken(username):
                correctPassword = self.checkPassword(username, password)
                self.userRecord = self.findUser(username, correctPassword)
                if self.userRecord:
                    self.setUserRecords()
            else:
                print("No such login. Try logging again.")

    @staticmethod
    def setAttribute(userRecord, field, failsafe=None):
        return userRecord[field]

    def findUser(self, username, password):
        userRecord = self.database.collection.find_one({"name": username, "password": password})
        return userRecord

    def setUserRecords(self):
        self.username = self.setAttribute(self.userRecord, "name")
        self.password = self.setAttribute(self.userRecord, "password")
        self.portfolio.stocks = self.setAttribute(self.userRecord, "stocks", {})
        self.portfolio.balanceHistory = self.setAttribute(self.userRecord, "balancehistory", {})
        self.portfolio.balance = self.setAttribute(self.userRecord, "balance", 0)

    def setUsername(self):
        userChoice = input("Select a username for your account: ")
        while len(userChoice) < 3 or self.isLoginTaken(userChoice):
            if len(userChoice) < 3:
                userChoice = input("Your username needs to be at least 3 characters long. Try again: ")
            if self.isLoginTaken(userChoice):
               userChoice = input("Username already taken. Please choose a different username: ")
        return userChoice

    @staticmethod
    def setPassword():
        userChoice = input("Set a password for your account: ")
        while len(userChoice) < 6 or not(any(char.isdigit() for char in userChoice)):
            userChoice = input("Your password needs to be at least 6 characters long and contain at least one number. Try again. ")
        return userChoice

    def checkPassword(self, username, userPassword):
        i = 3
        existing_username = self.database.collection.find_one({"name": username})
        password = existing_username.get("password")
        while(i > 1 and userPassword != password):
            i = i - 1
            userPassword = input(f"Incorrect password. Try again. You have {i} tries left. ")
        if(userPassword != password):
            print("You didn't provide a correct password. Exiting program.")
            sys.exit()
        else:
            print(f"Welcome, {username}!")
            return userPassword

    def isLoginTaken(self, username):
        existing = self.database.collection.find_one({"name": username})
        if existing:
            return True
        return False

