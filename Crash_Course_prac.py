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
last_item = bicycles.pop() #removes last item on list but is usable, you can also specify .pop(2)...
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
print(bicycles)  #I do not understand why it is sorted now, bicycles.sort() shouldnt be permanent 

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
#did it work? YES IT DID!
# 4.14 PEP 8 Code style and style guide https://python.org/dev/peps/pep-0008

# 4.15 Code Review 
#to add ruler to vscode -> setting->rulers->edit.json file
#"editor.rulers": [80, 99] to add lines at 80 and 99

#_______________________________________________________________________________
#_______________________________________________________________________________
#_____________________CHAPTER 5 IF STATEMENTS___________________________________
#5.1 Conditional Tests 
car = "Mazda"
print(car == "Mazda")

num = 42
print(num>=43)

nom = 34
print(nom<=34)
x = 12
print(x != 13)

age = 16
age == 16
age >= 12
age <= 14 
age == 16 or age >= 14 
age != 15 and age == 16
can_drive = 17
if can_drive >= 17  and age >= 17:
    print("you are able to drive")
else:
    print("you cannot drive")

first_car = "Ford Truck"
first_auto = "Acura"
current_car = "Mazda"
print(f"my first car was a {first_car == "Mazda"}")
if first_car == "Ford Truck" or first_auto == "Ford":
    print(f"my first car was a {first_car}")

#5.2 More Contitional Tests 
hobbies = ["Whittle", "bike", "sew", "make"]
if hobbies[0] == "whittle":
    print(f"you enjoy {hobbies[0]}ing as a hobby.")
elif hobbies[2] == "sew":
    print(f"you enjoy {hobbies[2]}ing as a hobby.")
else:
    print("you have no hobbies")

if first_car.lower() == "ford truck":
    print("cool")
if "bike" in hobbies:
    print("yes")

hobbies_lower = [u.lower() for u in hobbies]
print(hobbies_lower)
if hobbies_lower == "sew":
    print("you got it")

if "sew"  in  hobbies:
    print("you like to sew")
if "eat" not in hobbies:
    print("you dont like to eat")
    
#does this appear in the branch or on the main?
#5-3 Alien Colors 
alien_color = "red"
print(alien_color)

#testing to see if this is the branch that i can then merge to the main CCP practice branch 
#starting with Chapter 5 practice so i dont need to review a massive file the whole time 
#  5.3 Alien Colors
alien_color = "green"
if alien_color == "green":
    print("player earned 5-pts")
if alien_color == "red":
    print("0 pts")

# 5.4 Alien Colors 2
alien_color = "green"
if alien_color == "green":
    print("you've earned 5 pts")
else:
    print("you've earned 10 pts")

#5.5 Alien Colors #3
alien_color = "green"
player_name = "Kilgore"
if alien_color == "green":
    print(f"{player_name} earned 5 pts")
elif alien_color == "yellow":
    print(f"{player_name} earned 10 pts")
else:
    print(f"{player_name} earned 15 pts")
    
# 5.6 Stages of life using if-elif-else chain
age = 65

if age <= 2:
    print("you are bby")
elif 2 < age <= 4:
    print("you are toddler")
elif 4 < age < 13:
    print("you is kid")
elif 13 <= age < 20:
    print("you is teenager")
elif 20 <= age < 65:
    print("you is adult")
elif age >= 65:
    print("you is elder")
else:
    print("you are unalive")
    
#5.7 Favorite Fruits 
fav_fruit = ["strawberry", "blueberry", "bananna", "mango", "apple", "avacado"]

if "apple" in fav_fruit:
    print(f"you really like {fav_fruit[4]}")
if "bean" in fav_fruit:
    print("you really like bean")
else:
    print("you dont like bean")
    

    
# 5.8 Hello Admin/ and 5.9 Checking for Username (empty list[] with if/else)
# adding 5.10 to the code as well______pause point at 5.10 new_user list
current_user = ['admin', 'liver_wurst', 'pooty_tang', 'Reginald', 'user']
new_user = ['rustabell', 'Liver_wurst', 'rap raplinger']

current_user_lower = [user.lower() for user in current_user]
print(current_user_lower)


for new in new_user:  #check to see if new user name is in current user
    if new.lower() in current_user_lower: # do not forget to check in list use keyword "in"
        print( new + " you need to find a new name")
    elif new not in current_user:
        print(f"{new} is avaliable")

if current_user:  # check on users with account, and special for admin
    for user in current_user:
        if user == 'admin':
            print("Hello Admin, \nwould you like status report?")
        if user != 'admin':
            print(f"Hello {user}, \nwhere may i direct you")
else:
    print("you do not have an account foo!")
    
    
#cool bit of code from Mimo app with user input
'''name = input("Hello! What is your name?  ")
print(f"Nice to meet you {name}!")
age_input = input("How old are you?:")
age = int(age_input)
bot_age=3
age_difference= age - bot_age
print(f"You are {age_difference} years older them me. I'm only {bot_age} years old!")
color = input("What's your favorite color?: ")
print(f"Oh, {color} really is a beautiful color")'''

# 5.11 ordinal numbers 
ord_num = list(range(1,10))

for num in ord_num:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    elif num >= 4:
        print(str(num) + "th")
#will it publish to main?
print(3)
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
# Chapter 6 Dictionaries 
#I think i deleted this branch on accident, still uncertain on how to deal with branchs and main

# dictionaries{'key': value,..} use key-value pairs, a kep point to the value which can be anything
# such as a list, number, even another dictionary 

# example dictionary 
alien_0 = {'color': 'green', 'points': 5 }
alien_0['x-position'] = 0 # the left most part of the screen in pixels
alien_0['y-position'] = 25 #the supposed top of the screen in pixels
# del alien_0['points']     # used to delete the key:value pair
print(alien_0['color'])

# more indepth sample 

alien_0['speed'] = 'medium'

#move alien to right 
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3
    
# new position 
alien_0['x-position'] = alien_0['x-position'] + x_increment
print (f"New position: {alien_0['x-position']}")

# using .get() for dict values that may not exsist
del alien_0['points']
# del() keyword will show NONE if nothing assigned, you can tell what to say with second statement
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)

# 6.1 Person
bilbo = {'first_name': 'Bilbo', 
         'last_name': 'Baggins',
         'age': '74',
         'city': 'The Shire',
         }
for key, value in bilbo.items():  # for loops for dict need the items() keyword to pull key:values
    print(f'\nKey: {key}')
    print(f'Value: {value}')
    
# 6.2 Favorite Numbers
fav_numbs = {'ciena': 13, 'kyle': 42, 'jacob': 2112, 'kyle d': 11, 'arthur': 42}
for key, value in fav_numbs.items():
    print("\n", key)
    print('', value)
    
#6.3 Glossary 
glossary = {'if': 'conditional statment',
            'print': 'displays test in console',
            'for': ' for loops allow for itterations',
            'True': 'reads as 1, and is a conditional value',
            'False': 'reads as 0, and is a conditional value',
            'elif': 'else if statement, can use as many as needed',
            'else': 'final statement, runs at end if if condition not met',
            'where': 'is used for infinte loops and will loop until False',
            'items()': 'is a method which return a sequence of key:value pairs',
            'string': 'A series of characters.',
            'comment': 'A note in a program that the Python interpreter ignores.',
            'list': 'A collection of items in a particular order.',
            'loop': 'Work through a collection of items, one at a time.',
            'dictionary': "A collection of key-value pairs.",
            'key': 'The first item in a key-value pair in a dictionary.',
            'value': 'An item associated with a key in a dictionary.',
            'conditional test': 'A comparison between two values.',
            'float': 'A numerical value with a decimal component.',
            'boolean expression': 'An expression that evaluates to True or False.',
            }
for key, value in glossary.items():   # items can be replced with .key(), or .value()
    print(f'\n The {key} statment:')  # keys is the default value so its not necessarily needed
    print(value)
for word, meaning in glossary.items():
    print(f"\n{word.title()} has the meaning : {meaning.lower()}")

fav_games = {'kyle': "Doom", 
             'Ciena': "Baldurs Gate",
             'D': 'castlevaiena',
             'jacob': 'Doom',}
for value in set(fav_games.values()):  # set fxn shows single instance of key or value, no duplicate
    print(value)
# skip 6.4 which is glossary with loops as shown above
# 6.5 Rivers (ill use my fav_games)
for name, game in fav_games.items():
    print(f"{name.title()}'s favorite game is {game.title()}")
print('\n')
#6.6 Polling using fav_games
name_gamers = ['ciena', 'jacob', 'D', 'kyle', 'zach', 'daniel',]
for names in name_gamers:
    '''if names != fav_games.keys():
        print(f"Hello {fav_games.keys()}, you dont need to take the poll")
    elif names == fav_games.keys():
        print(f"Hello {names}, you should take a poll")'''
    if names in fav_games.keys():
        print(names.title() + 'you dont need to poll')
    else:
        print(names.title() + ', Please take this poll.')
    

    

