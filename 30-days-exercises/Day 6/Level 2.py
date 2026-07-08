#Unpack siblings and parents from family_members
family_members = ('sister', 'brother', 'mother', 'father')
(sis, bro, mum, dad) = family_members
print(sis)
print(bro)
print(mum)
print(dad)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "mango")
veg = ("bean", "cabbage", "carrot")
ani = ("fish", "chicken", "Prawns")

food_stuff_tp = fruits + veg + ani

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
slice = food_stuff_tp[3:6]

print(slice)

#Slice out the first three items and the last three items from food_stuff_lt list
slice1 = food_stuff_lt[0:3]
slice2 = food_stuff_lt[6:9]

print(slice1)
print(slice2)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
#nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)