import sqlite3
import smtplib, ssl
import re
import string


saltChars = string.ascii_letters + string.digits
codeGen = ascii_uppercase

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
def checkMail(mail):
    if(re.search(regex,email)):  
        return "Valid"
    else:  
        return "Invalid"  



def generateCodes(length, chars):
    string=""
    for x in range(length):
        string+=random.choice(chars)
    return string
        
    



#def 2factor():
    





while True:
    username = input("Enter username:")
    email = checkMail()
    if email == "Valid":
        


















        
