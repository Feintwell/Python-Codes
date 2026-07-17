import math

firstname = "myfirstname"
lastname = "mylastname"

first1 = len(firstname)
last1 = len(lastname)

#Check the data type of all your variables using type() built-in function
print(type("Python"))
print(type(26))
print(type(2.6))
print(type(True))
print(type(firstname))
print(type(5 + 7j))
print(type([2, 3, 4, 5, 6, 7, 8]))
print(type({'name': 'nameis'}))
print(type((3,6)))

#Using the len() built-in function, find the length of your first name
print(len(firstname))
print("Last name:", lastname)

#Compare the length of your first name and your last name
if first1 > last1:
    print("first name is longer")
elif last1 > first1:
    print("Last name is longer")
else:
    print("something wrong somewhere")
    
#Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4

total = num_one + num_two
print(total)
#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
exp = num_one ** num_two
print(exp)
#Calculate num_one to the power of num_two and assign the value to a variable exp
remainder = num_one % num_two
print(remainder)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

#The radius of a circle is 30 meters
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
r = 30
area_of_circle = math.pi * (r ** 2)
print("The area of the circle is:", area_of_circle)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * r
#Take radius as user input and calculate the area
radius = input("What is the radius?")
radiusint = int(radius)
area = math.pi * (radiusint ** 2)
print("The area of your circle is:", area)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
fnam = input("What is your first name?")
lnam = input("What is your last name?")
coun = input("What is your country?")
age = input("What is your age?")

print(fnam, lnam, coun, age)
