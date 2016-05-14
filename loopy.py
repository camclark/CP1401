def main():
    #gets age from the user, ensure is within expected range
    continueSwitch = False
    while continueSwitch == False:
        passengerAge = int(input("What is the age of the passenger?"))
        if passengerAge > 0 and passengerAge <= 130:
            continueSwitch = True
        else:
            print("Please ensure you entered the correct age of the passenger")
    print("yey you win - ie exited ")
main()