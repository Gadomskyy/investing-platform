class Portfolio:
    def __init__(self):
        self.balance = 0
        self.stocks = {}

    def buyStock(self):
        pass

    def sellStock(self):
        pass

    def showPortfolio(self):
        pass

    def addBalance(self, amount):
        self.balance += amount

    def removeBalance(self, amount):
        if amount > self.balance:
            print("Amount to withdraw cannot be bigger than your balance.")
        else:
            self.balance = self.balance - amount
        return self.balance

