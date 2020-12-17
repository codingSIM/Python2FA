import sqlite3
import smtplib, ssl
import re
import string
import random


saltChars = string.ascii_letters + string.digits
codeGen = string.ascii_uppercase

connObj = sqlite3.connect('login.db')

c = connObj.cursor()

#------------CHECKING IF TABLE EXISTS / Creating table
#get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='logins' ''')

#if the count is 1, then table exists
if c.fetchone()[0]==1 :
    print('Table exists.')
else:
    c.execute('''CREATE TABLE logins
             (username, email, password, salt)''')
#------------------------------------------------------------





#def addUser(username, email, password, salt):





#https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def getValidMail():
    while True:
        mail = input("Enter valid mail: ")
        if(re.search(regex,mail)):  
            return mail
        else:  
            pass  



def generateCodes(length, chars):
    string=""
    for x in range(length):
        string+=random.choice(chars)
    return string
        
    



#def 2factor():
    




#Loop to add entries to the db
while True:
    print("Add an entry / sign in: ")
    username = input("Enter username: ")
    mail = getValidMail()
    password = input("Enter password: ")
    salt = generateCodes(24, saltChars)
    #make function to encrypt password
    #encryptPassword()

    #adding entry to db
    acc = [username, mail, password, salt]
    c.execute("INSERT INTO logins VALUES (?,?,?,?)", acc)
    connObj.commit()

    
    again = input("Add another entry? [Y]/n :")
    if again == "" or again.lower() == "y":
        print("------------------------\n")
        pass
    else:
        print("\n")
        break
#-------------------------------------------------


#Loop for login + SENDING MAIL 2factor
#while True:
    











# Just be sure any changes have been committed or they will be lost.
connObj.close()











        
