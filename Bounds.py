lower = int(input("Please enter the lower bound: "))
upper = int(input("Please enter the upper bound: "))
theSum = 0

for number in range(lower, upper + 1):
    theSum = theSum + number
    print(theSum)
