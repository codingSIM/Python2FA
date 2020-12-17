import tools
import sqlite3
import string

connObj = sqlite3.connect('login.db')

c = connObj.cursor()

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
            c.execute("SELECT email from logins where username=?", (userN,))
            email = c.fetchone()[0]
            print("Password correct, sending code to:", email)

            code = tools.genCode()
            tools.send2FA(email, code)

            # check code is correct
            codeIn = input("2FA code: ")
            if codeIn.strip() == code:
                # Authentication success
                print("2FA code accepted. \n")
                print("You have successfully logged in. \n")
                #print("*Insert rest of app here*")
                print("... \n")
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
