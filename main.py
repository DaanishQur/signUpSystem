import random
import string
import smtplib
from email.message import EmailMessage

genCode = random.randrange(244124, 847447)

def runLogin():
    print("Welcome to the signup page.")
    sendPrompt = input("Enter email - ")
    verifyCode(sendPrompt)

def verifyCode(sendPrompt):

    recieverAddress = sendPrompt
    senderAddress = "senderEmail@gmail.com"
    password = "your sender email password" # READ - Google gives you a new custom password, visit Google's app password.
    subject = "Verification Code"
    body = "Your verification code is " + str(genCode)

    createEmail(recieverAddress, senderAddress, subject, body, password)

def createEmail(recieverAddress, senderAddress, subject, body, password):
    email = EmailMessage()
    email["From"] = senderAddress
    email["To"] = recieverAddress
    email["Subject"] = subject
    email.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:  # Use your SMTP server here
            smtp.starttls()
            smtp.login(senderAddress, password)
            smtp.send_message(email)
        print()
        print("Email Sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

    checkCode()

def checkCode():

    verifyPrompt = input("What is the six digit code sent to your email? - ")

    verifyPrompt = int(verifyPrompt)

    if verifyPrompt == genCode:
        print("Code accepted.")
        createPassword()
    else:
        print("Access denied. Please retry.")
        runLogin()

def createPassword():
    print()
    print("Your password must have the following requirements:")
    print(" - Must have digits greater than 6")
    print(" - Must have a symbol")
    print(" - Must have at least 1 uppercase letter")
    print()

    enterPassword = input("Enter password - ")

    hasSymbol = False
    hasUpperCase = False
    
    for char in enterPassword:
        if char not in string.ascii_letters + string.digits:
            hasSymbol = True
        if char in string.ascii_uppercase:
            hasUpperCase = True
    
    if len(enterPassword) > 6 and hasSymbol and hasUpperCase:
        print()
        print("Password is valid.")
        print("Access accepted. Welcome to your dashboard.")
    else:
        print("Password is invalid. Please follow our requirements to proceed.")
        createPassword()


runLogin()
