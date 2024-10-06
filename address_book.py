import os
import mysql.connector
from CRUD_OPS.create_person import create_person
from CRUD_OPS.view_all_contacts import view_all_contacts
from CRUD_OPS.update_contact import updateContact
from CRUD_OPS.delete_person import delete_person_by_name
from dotenv import load_dotenv
load_dotenv()

dbPassword =os.getenv('dbPassword')


mydb = mysql.connector.connect(host="localhost", user="root", passwd=dbPassword, database="address_book")


def print_menu():
    print("Connection Successful Moving to CRUD operations")
    print("Please select an operation for the address_book:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete a contact")
    print("5. Exit the program")
# verify connection
exitProgram = False

while exitProgram != True:
    if(mydb):
        print_menu()
        userInput = 0
        try: 
            userInput = int(input("I'd like to choose: "))
        except ValueError:
            print("The input was not a valid Integer")
        if userInput != 1 and userInput != 2 and userInput != 3 and userInput != 4 and userInput != 5:
            print("Sorry that was not an option. Exiting the program")
            exitProgram = True
        if userInput == 1:
            name = input("Please input a name for the person: ")
            phoneNumber = input("Please input a phone number: ")
            email = input("please input a email: ")
            create_person(name=name, phoneNumber=phoneNumber, email=email)
        elif userInput == 2:
            view_all_contacts() 
        elif userInput == 3:
            nameToUpdate = input("please put the name of the person you would like to update? ")
            updateContact(name=nameToUpdate) 
        elif userInput == 4:
            nameToDelete = input("Please input the name of the entry you would like to delete: ")
            delete_person_by_name(nameToDelete=nameToDelete) 
        elif userInput == 5:
            exitProgram = True        
# set up enviorment variables to get away from setting my password. Retest all
    # put four methods in another dir and see if I can call each of them
    # create create method and execute
    # test create method, check in MYSQL
    # Create Read/get method, 
    # test the read method, check in MYSQL
    # create Delete method, and execute
    # Test delete method, check in sql
    #  
    
    else:
        print(f"Connection to {mydb.database} failed" )    

mycursor = mydb.cursor()

