import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

dbPassword =os.getenv('dbPassword')
mydb = mysql.connector.connect(host="localhost", user="root", passwd=dbPassword, database="address_book")

cursor = mydb.cursor() 

def delete_person_by_name(nameToDelete):
    print(f"HEre in delete person by name {nameToDelete}")
    cursor.execute(f"SELECT * FROM Persons WHERE name=%s ", (nameToDelete,))
    fetchedRow = cursor.fetchone()
    print(fetchedRow)
    if (fetchedRow):
            print("This value exist in the table, proceeding with Delete query")
            cursor.reset()
            sqlForDeleteByName = """DELETE FROM PERSONS WHERE NAME = %s"""
            updateVals = (nameToDelete, )
            # try:
            cursor.execute(sqlForDeleteByName, updateVals)
            mydb.commit()
            print("Record deleted")
            cursor.reset()
            cursor.close()

            # except mysql.connector.Error as error:
            #     print("Failed to delete the record, check if exist in table: {}".format(error))    
                
    
    
    
