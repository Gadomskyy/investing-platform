import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="qwerty123")


def createDatabase():
    mycursor = mydb.cursor()
    mycursor.execute("Create database investingDB")

createDatabase()
