import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

dbPassword =os.getenv('dbPassword')

mydb = mysql.connector.connect(host="localhost", user="root", passwd=dbPassword, database="address_book")

cursor = mydb.cursor() 

def view_all_contacts():

    print("Here in view all contacts")
    sqlSelectAll = "SELECT * FROM Persons"
    cursor.execute(sqlSelectAll)
    result = cursor.fetchall()
    
    for row in result:
        print(row)
    cursor.reset()
    # mydb.commit()