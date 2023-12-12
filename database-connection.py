import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="qwerty123")

mycursor = mydb.cursor()

def createDatabase(name):
    mycursor.execute(f"Create database {name}")


