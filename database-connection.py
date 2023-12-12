import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="qwerty123")

print(mydb)

if(mydb):
    print("Connection successfull.")
else:
    print("Connection failed.")
