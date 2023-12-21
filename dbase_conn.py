from pymongo import MongoClient

class Database:

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")

    def createOrConnectDatabase(self, name):
        self.db = self.client[name]
        self.collection = self.db["userinfo"]

    def createCollection(self, collection_name):
        if hasattr(self, 'db'):
            self.collection = self.db[collection_name]
        else:
            print("No database selected. Create database first.")

    def createUserRecord(self, name, password):
        if self.collection.find_one({"name": name}):
            print(f"User with name '{name}' already exists. Please choose another name.")
        else:
            mydict = {"name": name, "password": password, "stocks": {}, "balance": 0, "balancehistory": {}}
            self.collection.insert_one(mydict)


    #updates the balance field in the database
    def updateData(self, login, operation, field, amount):
        recordfilter = {"name": login}
        newdata = {f"${operation}": {field: amount}}
        self.collection.update_one(recordfilter, newdata)





