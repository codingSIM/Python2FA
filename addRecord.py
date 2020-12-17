import tools
import sqlite3
import string

saltChars = string.ascii_letters + string.digits
codeGen = string.ascii_uppercase

connObj = sqlite3.connect('login.db')

c = connObj.cursor()


# Loop to add entries to the db
while True:
    print("Add an entry / sign in: ")
    username = input("Enter username: ")
    if not (tools.checkUsernameExists(c, username)):
        mail = tools.getValidMail()
        password = input("Enter password: ")
        salt = tools.generateCodes(24, saltChars)
        password = tools.getHashedPassword(password, salt)

        # adding entry to db
        acc = [username, mail, password, salt]
        c.execute("INSERT INTO logins VALUES (?,?,?,?)", acc)
        connObj.commit()

        again = input("Add another entry? [Y]/n :")
        if again == "" or again.lower() == "y":
            print("------------------------\n")
            pass
        else:
            print()
            break
    else:
        print("Username taken")
# -------------------------------------------------

# Just be sure any changes have been committed or they will be lost.
connObj.close()
