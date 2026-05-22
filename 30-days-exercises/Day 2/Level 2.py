import math

firstname = "myfirstname"
lastname = "mylastname"

first1 = len(firstname)
last1 = len(lastname)

num_one = 5
num_two = 4

print(type("Python"))
print(type(26))
print(type(2.6))
print(type(True))
print(type(firstname))
print(type(5 + 7j))
print(type([2, 3, 4, 5, 6, 7, 8]))
print(type({'name': 'nameis'}))
print(type((3,6)))

print(len(firstname))
print("Last name:", lastname)

if first1 > last1:
    print("first name is longer")
elif last1 > first1:
    print("Last name is longer")
else:
    print("something wrong somewhere")
    
total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

exp = num_one ** num_two
print(exp)

remainder = num_one % num_two
print(remainder)

floor_division = num_one // num_two
print(floor_division)

r = 30
area_of_circle = math.pi * (r ** 2)
print("The area of the circle is:", area_of_circle)

circum_of_circle = 2 * math.pi * r
radius = input("What is the radius?")
radiusint = int(radius)
area = math.pi * (radiusint ** 2)
print("The area of your circle is:", area)

fnam = input("What is your first name?")
lnam = input("What is your last name?")
coun = input("What is your country?")
age = input("What is your age?")

print(fnam, lnam, coun, age)
