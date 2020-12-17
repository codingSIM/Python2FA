import tools
import sqlite3
import string

saltChars = string.ascii_letters + string.digits
codeGen = string.ascii_uppercase

connObj = sqlite3.connect('login.db')

c = connObj.cursor()

# ------------CHECKING IF TABLE EXISTS / Creating table
# get the count of tables with the name
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='logins' ''')

# if the count is 1, then table exists
if c.fetchone()[0] == 1:
    print('Table exists.')
else:
    c.execute('''CREATE TABLE logins
             (username, email, password, salt)''')

# Just be sure any changes have been committed or they will be lost.
connObj.close()
# ------------------------------------------------------------


# Loop for login + SENDING MAIL 2factor
while True:
    print("Universal Log Authentication")
    print("Main menu: \n 1. Sign in \n 2. Log in \n 3. Exit")
    select = input()
    if select == "1":
        import addRecord
        del addRecord
    elif select == "2":
        import login
        del login
    elif select == "3":
        print("Goodbye")
        break
    else:
        print("Please enter 1 or 2")
        
    


    
