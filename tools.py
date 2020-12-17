import random
import re
import hashlib
import smtplib
import ssl
import string
from email.message import EmailMessage

def getValidMail():
    # https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    # https://www.regular-expressions.info/email.html
    regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    while True:
        ma = input("Enter valid mail: ")
        if re.search(regex, ma):
            return ma
        else:
            pass


def generateCodes(length, chars):
    st = ""
    for x in range(length):
        st += random.choice(chars)
    return st


def checkUsernameExists(database_cursor, uname):
    """
    Checks if the username is found in the database
    :rtype: bool
    :returns true if value is found
    """
    database_cursor.execute("SELECT username from logins where username=?", (uname,))
    row = database_cursor.fetchall()
    return not len(row) == 0


def getHashedPassword(plain_password, plain_salt):
    """
    :type plain_salt: str
    :type plain_password: str
    :rtype: bool
    :returns the "hexdigest"ed hash from the plain password and plain salt
    """
    saltedPass = plain_password + plain_salt
    saltedPass = saltedPass.encode()
    return hashlib.sha512(saltedPass).hexdigest()


def send2FA(receiver_email, code):
    from my_secrets import email_password
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "UniversalLog2020@gmail.com"  # Enter your email address

    #Set subject:
    #https://stackoverflow.com/questions/7232088/python-subject-not-shown-when-sending-email-using-smtplib-module

    message = EmailMessage()
        #Subject: {} \n\n
    message.set_content(("""\

    Your code is: {} """).format(code))

    message['Subject'] = 'Universal Log 2FA'
    

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    #server.quit() - Not sure if it should be here or not!!!!!


def genCode():
    code = ""
    for _ in range(6):
        code += random.choice(string.digits)

    return code
