def getPassword():
    password = input("Enter enter the missile codes: ")
    return password

def checkPassword(password):
    lengthPassword = len(password)
    if lengthPassword >= 6:
        lengthCheck = "true"
    else:
        lengthCheck = "false"
    if password == "a":
        passwordCheck = "true"
    else:
        passwordCheck = "false"


    return lengthCheck, passwordCheck



def main():
    #    character = input("Enter a character: ")
    #    print("The ASCII value of '" + character + "' is", ord(character))

    password = getPassword()
    lengthCheck,passwordCheck = checkPassword(password)
    print("Password length: " + lengthCheck + " Correct password:" + passwordCheck)

main()