import stockinfo
import datetime
import dbase_conn

class Portfolio:

    def __init__(self, user):
        self.user = user
        self.balance = 0
        self.stocks = {}
        self.balanceHistory = {}

    def showBalance(self):
        balance = self.user.portfolio.balance
        print(f"Your balance: {balance}")

    def showBalanceHistory(self):
        print(f"Your balance history is: ")
        for element in self.balanceHistory:
            print(element, self.balanceHistory[element])
        self.showBalance()

    def buyStock(self, ticker, amount):
        stock = stockinfo.stockInfo(stockinfo.api_key)
        price = float(stock.getLatestStockPrice(ticker))
        if price * amount > self.balance:
            print("The stocks cost is bigger than your balance. Try again.")
            return 0
        if ticker in self.stocks:
            self.stocks[ticker] += amount
        else:
            self.stocks[ticker] = amount
        self.balance -= amount * price

        return 0

    def sellStock(self, ticker, amount):
        stock = stockinfo.stockInfo(stockinfo.api_key)
        price = float(stock.getLatestStockPrice(ticker))
        if ticker not in self.stocks:
            print("You do not have this stock in your portfolio.")
            return 0
        else:
            if amount > self.stocks[ticker]:
                print("You do not have a sufficient amount of stock. Please try again.")
                return 0
            else:
                self.stocks[ticker] -= amount
                self.balance += amount * price
        return 0

    def showPortfolio(self):
        print("Your stock portfolio:", self.stocks)

    def addBalance(self, amount):
        if amount < 0:
            print("You cannot add negative balance.")
        else:
            self.balance += amount
            currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.balanceHistory[currentTime] = amount

        self.user.database.updateBalance(self.user.username, amount)

        return self.balance

    def removeBalance(self, amount):
        if amount > self.balance:
            print("Amount to withdraw cannot be bigger than your balance.")
        else:
            self.balance = self.balance - amount
            currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.balanceHistory[currentTime] = amount

        self.user.database.updateBalance(self.user.username, -amount)

        return self.balance
