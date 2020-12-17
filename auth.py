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
# ------------------------------------------------------------

# Loop to add entries to the db
false = False
while false:
    print("Add an entry / sign in: ")
    username = input("Enter username: ")
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
# -------------------------------------------------


# Loop for login + SENDING MAIL 2factor
while True:
    print("\n### Log in ###")
    userN = input("Enter username: ")

    # Check exists
    if tools.checkUsernameExists(c, userN):
        passW = input("Enter password: ")
        # Get the salt

        c.execute("SELECT salt from logins where username=?", (userN,))
        passSalt = c.fetchone()[0]

        # check if it matches,
        c.execute("SELECT password from logins where username=?", (userN,))
        saltedPass = c.fetchone()[0]

        if tools.getHashedPassword(passW, passSalt) == saltedPass:
            # if it does, send email with code
            c.execute("select email from logins where username=?", (userN,))
            email = c.fetchone()[0]
            print("Password correct, sending code to:", email)

            code = tools.genCode()
            tools.send2FA(email, code)

            # check code is correct
            codeIn = input("2FA code: ")
            if codeIn.strip() == code:
                # Authentication success
                print("2FA code accepted.")
                break

            else:
                print("Bad 2FA code.")

        else:
            print("Password incorrect")

    else:
        # User doesn't exist
        print("User doesn't exist")

# Just be sure any changes have been committed or they will be lost.
connObj.close()
