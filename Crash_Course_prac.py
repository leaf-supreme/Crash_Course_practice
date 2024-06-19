#Crash_Course_in_Python_Practice_Code

#Helpful links can be found here

# https://ehmatthes.github.io/pcc_3e/ (solutions and updates)
# https://github.com/ehmatthes/pcc_3e/ (github zip file)
# to read an excel file at work i needed to pip install openpyxl
# answeres to excercises (https://ehmatthes.github.io/pcc/solutions/chapter_4.html#4-3-counting-to-twenty)
# I may try to learn how to host my own server and upload versions to github and git but it will take time.

print("\tThis is where the world ends")
print("If i say hello world one more time, \nI may just take it over")
#import this # this is a poem by tim peters for code edequite, kind of fun
name = "hello to all!"
name.title() # upper and lower as well

#insert a variable into a string, f variable
first_name = " 'bob' "
last_name = " dole "
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#white spaces you can add whitespace or strip it
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#first_name.rstrip(), first_name.lstrip(), first_name.strip(), 
# first_name.removesuffix(), first_name.removeprefix()

# simple data set 
bicycles = ['trek', 'cannondale', 'santa cruz', 'fuji', 'look', 'pinarello', 'specalized', 'surley', 'all-city', 'giant']
first_bike = (f"My First Bicycle was a {bicycles[6]}")
print(first_bike)
bicycles[0] = 'trekk'
bicycles.append('canyon')# always adds it to the end
bicycles.append('huffy')
bicycles.insert(2, 'fairlight')
last_item = bicycles.pop() #removes last item on list but lets you use it first, you can also specify .pop(2)...
print(f"The last bike i will not own is a {last_item}")
to_expensive = bicycles.remove('pinarello') # doesnt remove all instances of item, use loop to remove
sorted_bikes = bicycles.sort()  # bicycles.sort(reverse=TRUE), displays sorted but not permanent, bicycles.reverse() is permanent

# For loops practice 
print("Lets look at all the bike brands")
for bikes in bicycles:  # remember bikes is the variable for the bicycles list in this loop
    print(f"{bikes.title()} makes a good bike")
    print(f"{bikes.title()} would make a great compnaion")
print("That was a long list of bikes")

# range function is useful for numbers
numbers = range(1,5) # range(6) is 0-5, 6 not displayed
even_list = list(range(2,11,2))

squares = []
for value in range(1,6):
    square = value**2
    squares.append(square) #both lines can be replaced by square.append(value**2)
print(squares)

# List comprehensions (somewhat advanced), can do the same as the 4 lines above (no colon used)
# combines a for loop and creation of new elements to fill an empty list that appends it each time
squarez = [value**2 for value in range(1,11)] 
print(squarez)

# hopefully a place to do some of the Crash Course Python Practice modules
# 4.3
numbers = list(range(0, 21)) # i had to look this up
for value in numbers:
    print(value)

#4.4 on million
million = list(range(0,1000001))
#for value in million:
    #print(value)   # crazy long use Ctrl+C in terminal to close

#4.5 summin a million
print(min(million))
print(max(million))
print(sum(million))  # did that in the blink of an eye 8)

#4.6 odd numbers
noomber = list(range(1,20,2))
for value in noomber:
    print(value)

#4.7 Threes
normber = list(range(0,30,3))
for value in normber:
    print(value)

#4.8 cubes
number = list(range(0,11))
for value in number:
    print(value**3)
#The way they did it with an empty list VVV
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

#4.9 cube comprehension
cube = [x**3 for x in range(1,11)]  #found similar online but got it first try
print(cube)
for cube in cubes:
    print(cube)
    
# 4.10 Slices using the bicycles list
print(f'the first three items of the bicycles list are : {bicycles[:3]}')

#done their way to show each line
print("\nThe first three bikes \nin bicycles are:")
for value in bicycles[:3]:
    print(value)    
print("The Last three items in bicycles are:")
for value in bicycles[-3:]:
    print(value.title())
print(bicycles)   # i do not understand why it is sorted now, bicycles.sort() shouldnt be permanent 

#4.11 My Pizzas, your Pizzas
pizzas = ["pepperoni", "Cheese", "Combo", "Vegan", "Pesto", "Mushroom and Olive"]
friends_pizza = pizzas[:] # this is an individual copy of the list that is now its own 
friends_pizza.append("Veggie")
friends_pizza.remove("Cheese")

print("These are my favorite pizzas")
for value in pizzas:
    print(value)
print("These are my friends favorite pizzas")
for value in friends_pizza:
    print(value)
#skipping 4.12 for foods.py for now

#4.13 Buffet 
basic_buffet = ("breadsticks", "pizza", "chicken", "soda", "ice cream")
for value in basic_buffet:
    print(value)
# basic_buffet(1) = "orange" cant modufy things in a tuple
basic_buffet_replace = ("rolls", "pizza", "ribs", "soda", "ice cream")
for value in basic_buffet_replace:
    print(value)
