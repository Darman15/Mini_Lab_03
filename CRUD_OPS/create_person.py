import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

dbPassword =os.getenv('dbPassword')
mydb = mysql.connector.connect(host="localhost", user="root", passwd=dbPassword, database="address_book")

cursor = mydb.cursor() 

def create_person(name, phoneNumber, email):
    print("Here in create Person")
    sqlInsert = "Insert into persons(name, phoneNumber, email) values(%s, %s, %s)"
    sqlInsertParams = (name, phoneNumber, email)
    print(type(sqlInsertParams))
    cursor.execute(sqlInsert, sqlInsertParams)
    mydb.commit()