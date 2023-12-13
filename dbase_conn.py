from pymongo import MongoClient

class Database:

    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")

    def createDatabase(self, name):
        self.db = self.client[name]

    def createCollection(self, collection_name):
        if hasattr(self, 'db'):
            self.collection = self.db[collection_name]
        else:
            print("No database selected. Create database first.")

    def createUserRecord(self, name, password):
        mydict = {"name": name, "password": password, "stocks": {}}
        self.collection.insert_one(mydict)



x = Database()
x.createDatabase("investingDB")
x.createCollection("userinfo")




