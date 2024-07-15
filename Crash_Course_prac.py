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
fav_numbs = {
    'ciena': [13,69,11,10],
    'kyle': [42,69,10,11,], 
    'jacob': [2112, 1, 69,],
    'kyle d': [11,12,13,14,],
    'arthur': [42,1,2,3,],
    }
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
        print('\n' + names.title() + ' you dont need to poll')
    else:
        print('\n' + names.title() + ', Please take this poll.')
        
# 6.7 People 
people = []
shire_folk = {'first_name': 'Bilbo', 
         'last_name': 'Baggins',
         'age': 74,
         'city': 'The Shire',
         }
people.append(shire_folk)
shire_folk = {'first_name': 'samwise', 
         'last_name': 'Gamgee',
         'age': 65,
         'city': 'The Shire',
         }
people.append(shire_folk)
shire_folk = {'first_name': 'meridoc', 
         'last_name': 'Took',
         'age': 54,
         'city': 'The Shire',
         }
people.append(shire_folk)
shire_folk = {'first_name': 'pippin', 
         'last_name': 'Brandybuck',
         'age': 55,
         'city': 'The Shire',
         }
people.append(shire_folk)
'''for  user, user_info in people:    # did not work
    name = user.title() + " " + user_info.title()
    print(name)'''
for shire_folk in people:
    namee = shire_folk['first_name'].title() + ' ' + shire_folk['last_name'].title()
    age = str(shire_folk['age'])
    loc = shire_folk['city'].title()
    print('\n' + namee + ' of ' + loc + ' is ' + age + ' years old')

# 6.8 Pets 
pets = []
pet = {
    'type': 'cat',
    'name': 'scromp',
    'age': 12,
    'owner_name': 'Butt Much'
}
pets.append(pet)
pet = {
    'type': 'dog',
    'name': 'ruffus',
    'age': 7,
    'owner_name': 'Rodger Evers' 
}
pets.append(pet)
pet = {
    'type': 'lizzard',
    'name': 'julius',
    'age': 23,
    'owner_name': 'Mr. Black'
}
pets.append(pet)
#my attempt at the for loop, could be much shorter
'''for pet in pets:  
    pet_type = pet['type'].lower() 
    pet_name = pet['name'].title()
    pet_age = str(pet['age'])
    pet_owner = pet['owner_name'].title()
    print('\n' + pet_name + ' is a ' + pet_type + ' at the age of ' + pet_age + 
          ' who is cared for by ' + pet_owner)'''
for pet in pets:          # much simpler to code and gives full list of info
    print('\nHere is what i know about ' + pet['name'].title())
    for key, info in pet.items():
        print('\t' + key + ": " + str(info))
        
# 6.9 Favorite Places 
fav_places = {
    'Jacob': ['Golf Course', 'Castle Rock', 'Shorline',],
    'Ciena': ['Hawaii', 'Santa Cruz', 'Monteray',],
    'Kyle_D': ['San Jose', 'Pismo',],
}
for name, places in fav_places.items():
    print('\n'+ name.title() + "'s favorite places are: ")
    for place in places:
        print('- ' + place)

# 6.10 Favorite numbers using excr6.2
for name, numb in fav_numbs.items():
    print('\n' + name.title() + "'s favorite numbers are:")
    for noomber in numb:
        print('\t-'+ str(noomber))
        
# 6.11 Cities a dictionary inside of a dicionary (tricky to call each piece)
cities = {
    'san jose':{
        'type': 'City',
        'pop': 2000000,
        'bird': 'seagul',
        'song': 'Macaframalama'
        },
    'Mt. View':{
        'type': 'city',
        'pop': 400000,
        'bird': 'duck',
        'song': 'apple bottom jeans',
        },
    'L.A.':{
        'type': 'City',
        'pop': 2500000,
        'bird': 'big bird',
        'song': 'Bay to L.A.',
        }
     }
for city, info in cities.items():
    typee = info['type'].title()
    pop = info['pop']
    bird = info['bird'].title()
    song = info['song'].title()
    print('\n' + city.title())
    print(f'\t-' + ' is a '+ typee + ' with a pop of ' + str(pop) + ' and the' 
        ' city song is ' + song)
    
# 6.12 Extensions (going to skip and move as its about improving older code)
# the one thing i dont like is appending info of a dict to an emprty list,
# i thought there might be a better way to add it to a blank list. 

#_______________________________________________________________________________
#_______________________________________________________________________________
#______________________________Chapter 7________________________________________
#CCP_CH7 Practice 
#7.1 Rental Car
'''rental_car = 'What kind of rental car would you like, we have many options '
rental_car += "please speficy the make only at this stage: "
car = input(rental_car)
print(f'Let me see if I can find a {car.title()} for you')

# 7.2 Resturant Seating 
seating = input('How many will there be in your party: ')
seating = int(seating)

if 6 >= seating > 4: 
    print(f'There will be a wait for your party of {seating}')
elif seating <= 4:
    print(f'We should have seating for your party of {seating}')
else:
    print(f'There is a 30 minute wait for parties greater then 6')
    
# 7.3 Multiples of Ten
mult_10 = input('Input number to see if its a mutliple of 10: ')
mult_10 = int(mult_10)
if mult_10 % 10 == 0:
    print(f'Yes, {mult_10} is a multiple of 10')
elif mult_10 % 10 == 2:
    print(f'{str(mult_10)} is not a mult of 10 but is even')
else:
    print(f'{str(mult_10)} is not a mult of 10 and is odd')

# Quick Dict practice 
food = {
    'meat':{
        'apatizer': 'fire cracker shrimp',
        'entree':'steak',
        'dessert': 'steak and kidney pie',
        },
    'vegitable': {
        'apatizer': 'fired atrichoke heart',
        'entree': 'quiche',
        'dessert': 'cheese cake',
        },
    'carbo': {
        'apatizer': 'macarroni balls',
        'entree': 'raviolli',
        'dessert': 'cake',
        }
}
for item, recipie in food.items():
    start = recipie['apatizer'].title()
    main = recipie['entree'].title()
    end = recipie['dessert'].title()
    print('\n From our menu, you can chose the ' + item.title() + ' option: ')
    print('To start, ' + start + ' For the main course ' + main + ' and for dessert ' + end) 
#The above code was very finiky and i re-wrote the same code and it worked after i re-typed it
# it was odd but i learned that a dict in a dict needs to have the same key's otherwise it wont
# read it correctly in a for loop
    
    # 6.11 Cities a dictionary inside of a dicionary (tricky to call each piece)
cities = {
    'san jose':{
        'type': 'City',
        'pop': 2000000,
        'bird': 'seagul',
        'song': 'Macaframalama'
        },
    'Mt. View':{
        'type': 'city',
        'pop': 400000,
        'bird': 'duck',
        'song': 'apple bottom jeans',
        },
    'L.A.':{
        'type': 'City',
        'pop': 2500000,
        'bird': 'big bird',
        'song': 'Bay to L.A.',
        }
     }
for city, info in cities.items():
    typee = info['type'].title()
    pop = info['pop']
    bird = info['bird'].title()
    song = info['song'].title()
    print('\n' + city.title())
    print(f'\t-' + ' is a '+ typee + ' with a pop of ' + str(pop) + ' and the' 
        ' city song is ' + song)
    
# 7.4 Pizza toppings (after a small hiatus and sidestep for dict prcatice)
wanted_top = "Please in put the pizza toppings you want: "
wanted_top += "\n please type 'quit' to exit: "
order = ''
while order != 'quit':
    order = input(wanted_top)
    print(f'\n We will add {order} to the order ')
    if order == 'quit':
        print(order)
        
#Their way using a break point for 7.4
while True:
    topping = input(wanted_top)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

# 7.5 Movie Tickets
ticket_price = 'Please enter your age for ticket prices'
ticket_price += '\n Enter "quit" to exit:  '
 
while True:
    person_age = input(ticket_price)
    if person_age == 'quit':
        break
    person_age = int(person_age)
   
    if person_age < 3:
        print('children under 3 are free')
    elif person_age <= 12:
        print('Children between 3 and 12 are 10$')
    elif person_age > 12:
        print('humans over that age of 12 are 15$')'''
# it kind of works but the if statement doesnt work
# I fixed it and learned that while loops can be broken at the very begninning of the script and 
# do not need to encompass the entire body of the code
# TO CLOSE AN ENDLESS LOOP YOU (CTRL+C)

# 7.8 Deli 
sandwhich_orders = ['veggie', 'tuna', 'itallian', 'turkey and cheese', 'ham and cheese', 'pastrami on rye', 'pastrami']
sandwhich_orders += ['sausage', 'pastrami', 'grilled cheese', 'pastrami']
finished_order = []
while sandwhich_orders:
    while 'pastrami' in sandwhich_orders:
        sandwhich_orders.remove('pastrami')
    orders = sandwhich_orders.pop()
    print(f'Your order of {orders.title()} is being made')
    finished_order.append(orders)
print('\n The orders have been completed')
for fin_order in finished_order:
    print(fin_order.title()) 

# 7.9 No Pastrami (editing 7.8 to say they're out of pastrami) Their way
sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("You're " + sandwich + " sandwich is finished.")
    
# 7.10 Dream Vacation
responses = {}       # setting a dictionary for responses to poll
vacay_promt = "\nIf you could go anywhere in the world where would you go: "

vacay_poll = True
while vacay_poll:
    name = input('\nWhat is your name?: ')
    response = input(vacay_promt)
    responses[name] = response   #storing responses in dictionary 
    
    repeat = input('Would you like anyone else to take poll (yes/no)?: ')
    if repeat == 'no':
        vacay_poll = False
print('______Poll Results______')
for name, response in responses.items():
    print( name.title() + ' would like to visit ' + response.title())    
    

