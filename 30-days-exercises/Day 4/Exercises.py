#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
a = "Thirty"
s = "Days"
d = "Of"
f = "Python"
space = " "
all = a + space + s + space + d + space + f
print(all)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
s = "Coding"
d = "For"
f = "All"
space = " "
all = s + space + d + space + f
print(all)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
com = "company" 
all = com

#4. Print the variable company using print().
print(all)

#5. Print the length of the company string using len() method and print().
print(len(all))

#6. Change all the characters to uppercase letters using upper() method.
up = all.upper() #flexiple.com

#7. Change all the characters to lowercase letters using lower() method.
low = up.lower()

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
coding = "Coding For All"
print(coding.capitalize())
print(coding.title())
print(coding.swapcase())

#9. Cut(slice) out the first word of Coding For All string.
coding = "Coding For All"
print(coding[7:])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
text1 = "Coding For All"
print(text1.find('Coding'))  #it will return 0 (no error) because it is returning the number(index) the first string wanted starts on is on. eg:: 0, 1, 2, 3 and so on. 

#11. Replace the word coding in the string 'Coding For All' to Python.
text1 = "Coding For All"
print(text1.replace('Coding for all', 'Python'))

#12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
text1 = "Coding For All"
print(text1.replace('Coding', 'Python'))

#13. Split the string 'Coding For All' using space as the separator (split())
text2 = "Coding For All"
print(text2.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
text3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text3.split(', '))

#15. What is the character at index 0 in the string Coding For All.
text2 = "Coding For All"
print(text2[0])

#16. What is the last index of the string Coding For All.
text2 = 'Coding For All'
print(text2.rfind('')) 

#17. What character is at index 10 in "Coding For All" string.
text2 = "Coding For All"
print(text2[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
language = 'Python For Everyone'
pfe = language[0] + language[7] + language[11]
print(pfe)

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
language = 'Coding For All'
cfa = language[0] + language[7] + language[11]
print(cfa)

#20. Use index to determine the position of the first occurrence of C in Coding For All.
text3 = "Coding For All"
pos = text3.index('C')
print(pos)

#21. Use index to determine the position of the first occurrence of F in Coding For All.
text3 = "Coding For All"
pos = text3.index('F')
print(pos)

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
txt = "Coding For All"
print(txt.rfind('l'))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
txt1 = "You cannot end a sentence with because because because is a conjunction"
print(txt1.find("because"))

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
txt1 = "You cannot end a sentence with because because because is a conjunction"
find = 'because'
print(txt1.rindex(find)) 

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
txt1 = "You cannot end a sentence with because because because is a conjunction"
slice = txt1[31:54] 
print(slice)

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
txt1 = "You cannot end a sentence with because because because is a conjunction"
find = 'because'
print(txt1.index(find))

 #27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
 #repeat of 25.

 #28. Does 'Coding For All' start with a substring Coding?
txt3 = "Coding for all"
print(txt3.startswith("Coding"))

#29. Does 'Coding For All' end with a substring coding?
txt3 = "Coding for all"
print(txt3.endswith("Coding"))

#30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
txt5 = "   Coding For All      "
print(txt5.strip())

#31. Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
txt6 = "30DaysOfPython"
txt7 = "thirty_days_of_python"
print(txt6.isidentifier())
print(txt7.isidentifier())

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(library))

#33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

#34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35. Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
r = "radius = 10"
a = "area = 3.14 * radius ** 2"
c = "The area of a circle with radius 10 is 314 meters square."
print("{} \n {} \n {}".format(r, a, c))

#36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
q = 8
w = 6
print("{} + {} = {}".format(q, w, q + w))
print("{} - {} = {}".format(q, w, q - w))
print("{} * {} = {}".format(q, w, q * w))
print("{} / {} = {:.2f}".format(q, w, q / w))
print("{} % {} = {}".format(q, w, q % w))
print("{} // {} = {}".format(q, w, q // w))
print("{} ** {} = {}".format(q, w, q ** w))