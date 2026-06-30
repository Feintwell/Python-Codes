#1. Declare an empty list
empty = []

#2. Declare a list with more than 5 items
fruits = ["Banana", "Apple", "Pear", "Grape", "Orange", "Passion Fruit", "Watermelon", "Pineapples"] 

#3. Find the length of your list
Bears = ["Bear", "Polar Bear", "Black Bear", "Brown Bear"]
length = len(Bears)
print(length)

#4. Get the first item, the middle item and the last item of the list
cake = ["Vanilla", "Chocolate", "Red Velvet", "Lemon", "Strawberry"]
first = cake[0]
middle = cake[2]
last = cake[4]

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Name", 100, 200, "Witch", "Barbie World"]

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first = it_companies[0]
middle = it_companies[3]
last = it_companies[6]
print("First company is: %s. \n The middle company is: %s. \n The last company is: %s" %(first, middle, last))

#10. Print the list after modifying one of the companies
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
companies[0] = "Meta"
print(companies[0])

#11. Add an IT company to it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Accenture")
print(it_companies)

#12. Insert an IT company in the middle of the companies list
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
companies.insert(1, "IT Companies")
print(companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper() 
print(it_companies)

#14. Join the it_companies with a string '#;  '
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("#, ".join(it_companies))

#15. Check if a certain company exists in the it_companies list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
yesss = "Google" in it_companies
print(yesss)

#16. Sort the list using sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
out = it_companies[0:3]
print(out)

#19. Slice out the last 3 companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
out = it_companies[4:7]
print(out)

#20. Slice out the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
out = it_companies[3:4]
print(out)

#21. Remove the first IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("Facebook")
print(it_companies)

#22. Remove the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(3)
print(it_companies)

#23. Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop()
print(it_companies)

#24. Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies
print(it_companies)

#26. Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
together = front_end + back_end
print(together)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
together = front_end + back_end

full_stack = together
full_stack.insert(5, 'Python')  
full_stack.insert(6, 'SQL')  
print(full_stack)