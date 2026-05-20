no = int(input("Enter a number you want to not appear (1-5): "))

list = [1,2, 3, 4, 5]
def ifsee():
        see = (input("Do you want to see the list? (true/false)"))
        if see == ("True"):
            print(list)
        elif see == ("False"):
            print("Okay, no worries")
        else:
            print("Sorry. Please enter if True or False")
            ifsee()

if no in list:
    list.remove(no)
    print("Rest of the list:", list)
else:
    print("That number is not in the list")
    ifsee()
