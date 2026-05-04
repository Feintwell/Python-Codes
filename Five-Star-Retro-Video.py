 def main():
    newvdo = getnewvdo()
    oldvdo = getoldvdo()
    sum1 = calculatesum1(newvdo,oldvdo)
    displaysum1(newvdo,oldvdo,sum1)

def getnewvdo():
    newvdo = int(input("Enter the number of new videos rented for the night :"))
    return newvdo
def getoldvdo():
    oldvdo = int(input("Enter the number of old videos rented for the night :"))
    return oldvdo
def calculatesum1(newvdo,oldvdo):
    totalnew = newvdo * 3.00
    totalold = oldvdo * 2.00
    sum1 = totalnew + totalold
    return sum1

def displaysum1(newvdo,oldvdo,sum1):
    print("Your total is : $", sum1)
main()
