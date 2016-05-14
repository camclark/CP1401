def checkHandle(prompt,codeArray,wordArray):
    #codes are passed in along with array
    continueSwitch = False
    wrongCheck = True
    while continueSwitch == False:
        #uses prompt provided
        instanceInput = input(prompt + "\n")
        instanceInput = instanceInput.lower()
        for i in range (0,len(codeArray)):
            #checks codeArray for expected
            if codeArray[i] == instanceInput:
                continueSwitch = True
                #changes user input into a word
                instanceInput = wordArray[i]
                wrongCheck = False
            #special case for who for
            elif len(codeArray) == 2 and instanceInput == "s":
                instanceInput = input("Please enter the passenger's name\n")
                continueSwitch = True
                wrongCheck = False
                continue
            # Error message - none of the array match input
        if wrongCheck == True:
            print("Error input not recognised. \nPlease select what you would like by entering the corosponding letter in brackets \n")
    return instanceInput

def main():
    userName = "Bob"
    codeArray = ["y", "s"]
    wordArray = [userName]
    prompt = "Is the ticket for (Y)ou or (S)omeone else?"
    passengerName = checkHandle(prompt,codeArray,wordArray)


    codeArray = ["c", "s", "p"]
    wordArray = ["Cairns","Sydney","Perth"]
    prompt = "Please select the destination for your return trip. Base fare prices are listed below: \n(C)airns – $400 \n(S)ydney – $575 \n(P)erth - $700"
    tripDestination= checkHandle(prompt,codeArray,wordArray)

    print(passengerName + tripDestination)

main()