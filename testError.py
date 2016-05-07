def checkHandle(prompt,codeArray,wordArray):
    switch = False
    while switch == False:
            #If up to this part in main will run this if statement
                #get input
                print(prompt)
                instanceInput = input()
                instanceInput = instanceInput.lower()
                x = 0
                for Number in codeArray:
                    if Number == instanceInput:
                        switch = True
                        instanceInput = wordArray[x]
                    x = x + 1
                        # Error message - none of the array match input
                    if switch == "False":
                        print("Error input not recognised. \nPlease select what you would like by entering the corosponding letter in brackets")
    return instanceInput

def getAge():
    # asks user for the passenger's age. Ensures age is within reasonable range.
    switch = False
    while switch == False:
        print("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.")
        inputAge = input()
        while not int(inputAge):
            inputAge = input()

        passengerAge = int(inputAge)

        if passengerAge >= 0 and passengerAge <= 130:
            switch = True
        else:
            print("Please ensure you entered the correct age of the passenger")
    return passengerAge

def orderTicket(userName):

    age = getAge()

    codeArray = ["c", "s", "p"]
    wordArray = ["Cairns","Sydney","Perth"]
    prompt = "Please select the destination for your return trip. Base fare prices are listed below: \n(C)airns – $400 \n(S)ydney – $575 \n(P)erth - $700"

    tripDestination= checkHandle(prompt,codeArray,wordArray)
    print("Testing full word print; " + tripDestination)


    codeArray = ["o", "r"]
    wordArray = ["one-way","return"]
    prompt = "Is this a: \n(R)eturn trip  \n(O)ne-Way"


    flightType = checkHandle(prompt,codeArray,wordArray)
    print("Testing full word print; " + flightType)


    codeArray = ["b", "e","f"]
    wordArray = ["business", "economy", "frugal"]
    prompt = "Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. \nPlease note choosing Frugal fare means you will not be offered a seat choice. \n(B)usiness - $275 \n(E)conomy - $25 \n(F)rugal - $0"

    seatType = checkHandle(prompt, codeArray, wordArray)
    print("Testing full word print; " + seatType)

    if seatType == "frugal":
        seatClass = middle
    else:
        codeArray = ["w", "a","m"]
        wordArray = ["window", "aisle", "middle"]
        prompt = "Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare. \n(W)indow  $75 \n(A)isle  $50 \n(M)iddle -$25"

        seatClass = checkHandle(prompt, codeArray, wordArray)
    print("Testing full word print; " + seatClass)


def main():
    userName = greeting()
    exitProgram = False
    ticketCost = []

    while not exitProgram:
        print("Tropic Airlines Ticket Ordering System: \n (I)nstructions \n (O)rder ticket \n (E)xit ");

        userInput = input()
        userInput = userInput.lower()
        if userInput == "o":
            ticketCost.append(orderTicket(userName))

        elif userInput == "e":
            # exits program
            ticketCost.sort()
            print(userName + " your orders are: ")
            ticketCostLength = len(ticketCost)
            i = 0
            if ticketCostLength < 1:
                print(userName + ", your order is: " + ticketCost + " Your final total is: " + ticketCost)
            else:
                for price in ticketCost:
                    i = i + 1
                    print("Ticket " + str(i) + " " + price)

            print("Thank you for choosing Tropical Airlines for your air travel needs.")
            quitProgram = True

        elif userInput == "i":
            print(
                "Thank you for choosing Tropical Airlines for your air travel needs. \nYou will be asked questions regarding what type of ticket you would like to purchase as well as destination information. \nWe also offer 50% discounted fares for children under the age of 16. Infants under the age of 2 are free.")
            print("You have been returned to the main menu.")
            print(" ")
        else:
            print("ERROR: Input not recognised. Please enter the letter in brackets to complete the intended action.")

main()