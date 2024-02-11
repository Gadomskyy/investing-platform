import stockinfo
import datetime

class Portfolio:

    def __init__(self, user):
        self.user = user
        self.balance = 0
        self.stocks = {}
        self.balanceHistory = list()

    def showBalance(self):
        balance = round(self.user.portfolio.balance, 2)
        print(f"Your balance: {balance}")

    def showBalanceHistory(self):
        balancehistory = self.user.portfolio.balanceHistory
        print(f"Your balance history is: {balancehistory}\n")
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
        currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.user.database.updateData(self.user.username, "inc", "balance", -amount * price)
        self.user.database.updateData(self.user.username, "set", "stocks", self.stocks)
        transaction = {"type": "Buy", "ticker": ticker, "amount": amount, "price": amount * (-price)}
        self.balanceHistory.append({currentTime: transaction})
        self.user.database.updateData(self.user.username, "push", "balancehistory", {currentTime: transaction})

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
                currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.user.database.updateData(self.user.username, "inc", "balance", amount * price)
                self.user.database.updateData(self.user.username, "set", "stocks", self.stocks)
                transaction = {"type": "Sell", "ticker": ticker, "amount": amount, "price": amount * price}
                self.balanceHistory.append({currentTime: transaction})
                self.user.database.updateData(self.user.username, "push", "balancehistory", {currentTime: transaction})
        return 0

    def showPortfolio(self):
        print("Your stock portfolio:", self.stocks)

    def addBalance(self, amount):
        if amount < 0:
            print("You cannot add negative balance.")
        else:
            amount = round(amount, 2)
            self.balance += amount
            currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            transaction = {"type": "Deposit", "amount": amount}
            self.balanceHistory.append({currentTime: transaction})
            self.user.database.updateData(self.user.username, "inc", "balance", amount)
            self.user.database.updateData(self.user.username, "push", "balancehistory", {currentTime: transaction})

    def removeBalance(self, amount):
        amount = round(amount, 2)
        if amount > self.balance:
            print("Amount to withdraw cannot be bigger than your balance.")
        else:
            self.balance = self.balance - amount
            currentTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            transaction = {"type": "Withdrawal", "amount": -amount}
            self.balanceHistory.append({currentTime: transaction})
            self.user.database.updateData(self.user.username, "inc", "balance", -amount)
            self.user.database.updateData(self.user.username, "push", "balancehistory", {currentTime: transaction})

        return self.balance
