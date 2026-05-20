import math

# 1. Declare your age as integer variable
age = 23
int(age)

# 2. Declare your height as a float variable
height = float(170)

# 3. Declare a variable that store a complex number
com = 4 + 4j
complex(com)

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Enter base: 20
# Enter height: 10
# The area of the triangle is 100
h = int(input("What is your triangle's height?"))
b = int(input("What is your triangle's base?"))
area = 0.5 * h * b
print(area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
a = int(input("What is your side A?"))
b = int(input("What is your side B"))
c = int(input("What is your side C?"))
peri = a + b + c
print(peri)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("Let's calculate the area and perimeter of a rectangle")
length = int(input("what is the length?"))
width = int(input("what is the width?"))
peri = 2 * (length + width)
area = length * width
print("Your area is: ", area, " and your perimeter is: ", peri)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("What is the radius of your circle?"))
area = math.pi * radius * radius
peri = 2 * math.pi * radius
print("Your area is: ", area, "Your perimeter is: ", peri)

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
p = "python" 
d = "dragon"
print("Dragon length: ", len(d), "and python length is: ", len(p))
print(len(d) != len(p))

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
dra = 'on' in 'dragon'
pyt = 'on' in 'python'
print(dra and pyt)

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

#15. There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#16. Find the length of the text python and convert the value to float and convert it to string
length = len("python")
flen = float(length)
slen = str(flen)
print(type(flen))
print(type(slen))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
a = int(input("What is your number?"))
remain = a % 2
if remain == 0:
    print("Your number is an even number.")
else:
    print("your number is not an even number")

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor = 7 // 3
print(floor)
divi = 7 / 3
divi = int(divi) 
print(divi)
print (divi == floor)

#19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#20. Check if int('9.8') is equal to 10
num1 = int('9.8')
num2 = 10
print(num1 == num2)
#It gives a value error: ValueError: invalid literal for int() with base 10: '9.8'

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = int(input("What are your hours?"))
pay = int(input("What is your hourly pay?"))
earning = hours * pay
print("Your weekly earning is", earning)

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
years = int(input("Enter the number of years you have lived: "))
live = years * 365 * 24 * 60 * 60
#365 - days in an year, 24 - hours in a day, 60 - minutes in an hour, 60 - seconds in a minute
print(live)

#23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
l1 = "1 1 1 1 1"
l2 = "2 1 2 4 8"
l3 = "3 1 3 9 27"
l4 = "4 1 4 16 64"
l5 = "5 1 5 25 125"
print(l1, l2, l3, l4, l5, sep='\n')