def formatCurrency(number):
    number = "${:,.2f}".format(cost)
    return number

def main():
    x = 0
    total = 0
    for x in range (1,10):
        print("give me number" + str(x))
        number = int(input())
        number = "${:,.2f}".format(number)
        total = total + number
        x=x+1

main()