def main():
    sal = getsal()
    exp = getexp()
    total = caltotal(sal,exp)
    displaysum1(sal,exp,total)

def getsal():
    sal = int(input("What is your monthly salary?"))
    return sal
def getexp():
    exp = int(input("What is your monthly expense?"))
    return exp
def caltotal(sal,exp):
    total = sal - exp
    return total

def displaysum1(sal,exp,total):
    print("Your total is : $", total)

main()
