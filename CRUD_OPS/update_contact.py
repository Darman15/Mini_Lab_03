import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

dbPassword =os.getenv('dbPassword')

mydb = mysql.connector.connect(host="localhost", user="root", passwd=dbPassword, database="address_book")

cursor = mydb.cursor() 

def updateContact(name):
    print(f"Here from the update contact with the name  {name}")
    # ask what the user wants to update
    wants_to_update = input("What field would you like to update, name, phone number, or email?: ").lower()
    # validate input at least minimully
    if wants_to_update != "name" and wants_to_update != "phone number" and wants_to_update != "email":
        print("that was not an option bye")

    elif wants_to_update == "name":   
        # validate name exist in database
        cursor.execute(f"SELECT * FROM Persons WHERE name=%s ", (name,))
        fetchedRow = cursor.fetchone()
        print(fetchedRow)
        if (fetchedRow):
            print("This value exist in the table, proceeding with update query")
            updateNameTo = input("What would you like the name to be? ")
            sqlForUpdateName = "UPDATE PERSONS SET NAME = %s WHERE name = %s"
            updateVals = (updateNameTo, name)
            cursor.execute(sqlForUpdateName, updateVals)
            mydb.commit()
            cursor.reset()
            
        else:
            print("This name is not currently in the contact list. Goodbye")
    
    elif wants_to_update == "phone number":
          # validate name exist in database
        cursor.execute(f"SELECT * FROM Persons WHERE name=%s ", (name,))
        fetchedRow = cursor.fetchone()
        print(fetchedRow)
        if (fetchedRow):
            print("This value exist in the table, proceeding with update query")
            updatePhoneNumberTo = input("What would you like the new email to be?: ")
            sqlForUpdatePhoneNumber = "UPDATE PERSONS SET PHONENUMBER = %s where name = %s"
            updateVals = (updatePhoneNumberTo, name)
            cursor.execute(sqlForUpdatePhoneNumber, updateVals)
            mydb.commit()
    elif wants_to_update == "email":
          # validate name exist in database
        cursor.execute(f"SELECT * FROM Persons WHERE name=%s ", (name,))
        fetchedRow = cursor.fetchone()
        print(fetchedRow)
        if (fetchedRow):
            print("This value exist in the table, proceeding with update query")
            updateEmailTo = input("What would you like the new email to be?: ")
            sqlForUpdateEmail = "UPDATE PERSONS SET EMAIL = %s where name = %s"
            updateVals = (updateEmailTo, name)
            cursor.execute(sqlForUpdateEmail, updateVals)
            mydb.commit()   
    cursor.reset()            
    # set conditionals for each possiblity
    # ask for each possibilities update
    # capture update value
    # input that update value into row. 