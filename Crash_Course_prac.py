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
#_______________________________________________________________________________    
#_______________________________________________________________________________
#_______________________Chapter 8 - Functions Practice__________________________
# ___________________8.1 Message 
def display_massage():
    """Displayes a what CCP_CH8 is about"""
    print('This Chapter is about defining functions')
    
display_massage()

#________________ 8.2 Favorite Book
def favorite_book(titles):  # the variable title is a 'parameter' for a function (def)
    """Displays favorite book using user input"""
    for title in titles:
        print(f'My favorite books is {title.title()}')
    
favorite_book('Star Wars') # Star Wars is an 'argument' for the function favorite_book

# Example of positional Argument in which order matters
# assigning default values for year, make and model if no argument is used
def describe_car(year='N/A', make='N/A', model='N/A'): 
    """"Function asking for make and model of your car"""
    print(f'The car you drive is a: {year} {make.title()} {model.title()}')
    
describe_car(2012, 'mazda', '3 skyactiv') # the order you add the arguments matters

# The other version of a function is a Keyword Argument 
describe_car(make='honda', model='civic coupe', year=2012) 

# ______________8.3 T-shirt
def make_shirt(size='N/A', color='White', text="N/A"):
    """Displays shirt size and text on front"""
    print(f"You're shirt is size {size}, {color.title()} and willl display {text}")
make_shirt(12,'Blue', "Gimmie Dat $$Money$$")

#__8.4 Large Shirt and 8.5 are completed with above code, this is easier to understand.....right now

# Retrun values for a function 
#a return takes a value inside function and sends back to line that called fuction 
# example of return value 
def get_formatted_name(first_name, middle_name, last_name):
    """return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()          # the return sends back to function call
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# Setting a function with an optional parameter and returning a dictionary 
def build_person(first_name, last_name, age=None):
    """Return a dict of info about a person """
    person = {'first': first_name.title(), 'last': last_name.title(),}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#_______________________ 8.6 City names
def city_country(city_name, country_name):
    """Returns a formatted name of your City and Country"""
    location = (city_name.title() + " , " + country_name.title())
    return location
san_jose = city_country('san jose', 'united states')
print(san_jose)

# also written -> return(city.title() + "," + country.title())

#__________________ 8.7 Album 
def make_album(artist_name, album_title, number_song=None):
    """Makes a dictionary of artist song, album and potential number of song on album"""
    album = {
        'artist': artist_name.title(),
        'album': album_title.title(),
        }
    if number_song:       
        album['album_#_of_song'] = number_song
    return album

sting = make_album('sting', 'dessert rose', 12)
print(sting)
jimbo = make_album('jimi hendrix', 'watchtower', 9)
print(jimbo)
bon_iver = make_album('bon iver', 'holocerne')
print(bon_iver)

# ___________________8.8 User Albums 

while True:
    print('\nPlease help me document an album!')
    print('(enter "q" to quit)')
    art_name = input('Artist Name: ')
    if art_name == 'q':
        break
    album_name = input('Please enter the Album name: ')
    if album_name == 'q':
        break
    num_of_song = input('If you know the number of songs please record here: ')
    if num_of_song == 'q':
        break
    album_dict = make_album(art_name, album_name, num_of_song)
    print(album_dict)    
print('Thanks for the info')
    
# passing a list into  a function 
books = ['counte of monte cristo', 'star wars', 'captian blood']
favorite_book(books)    # i needed to add a for loop to the funciton 

# modifying a list in a function 
unprinted = ['cube', 'letters', 'flower pot']
printed = []
# simulate printing each design until none are left
'''while unprinted:
    current_print = unprinted.pop()
    print(f'Now Printing: {current_print}')
    printed.append(current_print)
# show what has been printed
print(f'\nThe Following models have been printed')
for pront in printed:
    print(f'{pront} has completed printing')'''
    
# rewriting the above code using a function to call on
def print_models(unprinted_1, printed_1):
    """Simulate Printing each model until none are left """
    while unprinted_1:
        current_print = unprinted_1.pop()
        print(f'Now Printing: {current_print}')
        printed_1.append(current_print)
def show_printed (printed_1):
    """Shows Models that have been printed"""
    print(f'\nThe Following models have been printed')
    for pront in printed_1:
        print(f'{pront} has completed printing')
unprinted_1 = ['seahorse', 'camera', 'gun', 'phone case']
printed_1 = []
# This is made of two functions that each do one specific job, if you combine them it will be 
# difficult to make changes effectivley later on. For now you just call on one fuction for each task

print_models(unprinted_1[:], printed_1) # take away [:] to see difference in list
show_printed(printed_1)
print(unprinted_1)
# if you want to keep the unprinted lisst unmodified you can pass a copy unprinted[:] which makes  a
# copy of the list and keeps the original, it is time and memory intensive to do this and should be
# done with caution as it can be computationally heavy with large lists if your not careful

#___________________ 8.9 Messages 
texts = ['hi', 'how', 'now', 'SMDAIWCOYT',]
def show_messages(text_msg):
    """Displays text messages"""
    for text in text_msg:
        print(f'You wrote this text: {text}')
show_messages(texts)

# __________________8.10 Sending Messages 
def send_messages(send_msgs, sent_msgs):
    """Shows sent message and moves to sent list"""
    while send_msgs:
        current_msg = send_msgs.pop()
        print(f'\n{current_msg} :has been sent')
        sent_msgs.append(current_msg)
#_________________ 8.11 Archived Messages 
sent_messages = []
send_messages(texts, sent_messages)
print(sent_messages)

# Adding an arbritary number of arguments *Argument (very useful) but must be placed at the end!!!
def make_pizza(size, *toppings):   
    """Summarize the pizza about to be made"""
    print(f'The {size} pizza requested with the following toppings is being made: ')
    for top in toppings:
        print(f' -{top}')
make_pizza('large', 'mushroom', 'salad', 'cheese only','anchovies')

# Using Arbitrary Keywork Arguments (the infamous *args), useful for unknown number of arguments 
# *args and *kwargs are used when an arbritary amount of info will be passed such as for user input
def build_profile(first, last, **user_info):
    """Build a dict contianing all we know aobut user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Brian', 'Ellis', location='Folsom, CA', age=42, hair_color='Platinum Blonde')
print(user_profile)

# ____________ 8.12 Sandwhiches 
def sandwhich_order(size, *innards):
    """Lists out a sandwhich order"""
    print(f'Your {size} Sandwhich is being made with the following items: ')
    for ingredients in innards:
        print(f'\t- {ingredients}')
    print('\n your Sandwhich is ready')
        
kyles_which = sandwhich_order('Large', 'onion','soup', 'soup', 'lemons')

# _____________ 8.13 User Profile _____I already did that with Brian ellis
kyle_profile = build_profile('Kyle', 'H', location='San Jose', age=30, Rizz=True)
print(kyle_profile)

# _______________ 8.14 Cars
def make_car(make, model, **options):
    options['Manufacturor'] = make
    options['Model'] = model 
    return options 
# the book has it written differntly, mine seems much more efficient but i dont know how it is 
# already in the format of a dictionary, it put it in proper order but thats all i can tell
def make_truck(make, model, **options):
    car_dict = {
         'manufacturer': make.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

mazda_3 = make_truck('Mazda', '3 i-touring', color='White', transmission="manual", tow_package = False)
print(mazda_3)

# Saving and using(importing) modules
# if you saved create_truck.py you would import creat_truck as ct (or just create_truck)
# then when you wanted to use it you would module_name.function_name()
# import create_truck 
# create_truck.make_truck('honda', 'civic', color=red,...)

# if you wanted a specific function you would import specifically 
# from CCP_CH8 import make_truck  (from module_name import funct_0, funct_1, funct_2...)
# you do not need dot(.) notation if you specify which funct to import you can use as is 

# you can import all functions from module with * e.g. from CCP_CH8 import * which allows the use
# of all functions and can call them without (.) notation but can be faulty if there are multiple
# functions or lines of code that share the same name. (.) is often more concise and descriptive

# Styling Functions def function_name(parameter_0, parameter_1='default value') no spaces after (=)
# def function_name(                                (Following PEP8 formatting)
#       parameter_0, parameter_1, parameter_2,    (two tabs or 8 spaces for fxn parameters)
#       parameter_3, parameter_4, parameter_5,):
#       """Docstring describing what it does"""    (docstring short and tells what fxn does)
#   Finction body                                  (fxn body 4 spaces or one tab)

#________________8.15 Printing models in file importing_modules_practice.py
# _______________8.16 Imports will also be done using ^^^ file
#________________8.17 styling which i was following aside from the over long parameters

#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________Chapter 9 Classes_______________________________________

class Dog:            # Class of Dog is capatilized to show it is a class
    """A Simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
        def sit(self):
            """Simulate a dog siting in response to a command."""
            print(f"{self.name} is now sitting")
            
        def roll_over(self):
            """simulate rolling over in response to a command."""
            print(f'{self.name} roll over!')
            
my_dog = Dog('Kobi', 13)
your_dog = Dog('Bill', 57)

print(f'{my_dog.name} is my pup')  # to call instnace of my_dog you need (.) notation 
print(f'{my_dog.name} is {my_dog.age} years old')#each isntace made is unique so long as variable is
print(f'{your_dog.name} is your dog')
print(f'{your_dog.name} is {your_dog.age} years old ')

#_________________9.1 Resturant 

'''class Resturant:
    """A simple model of a resturant showing the name and cuisine"""
    
    def __init__(self, resturant_name, cuisine_type):
        """Initilize the Resuturant (as the book wrote it)."""
        self.resturant_name = resturant_name.title()
        self.cuisine_type = cuisine_type
        
#    def describe_resturant(self):
#        print(f'\n{self.resturant_name} serves authentic {self.cuisine_type} style food')
    def describe_resturant(self):  # the books method for the script
        msg = msg = self.resturant_name + " serves wonderful " + self.cuisine_type + " cuisine."
        print(msg)
            
    def resturant_open(self):
        print(f'{self.resturant_name} is Open')
            
mai_thai = Resturant('Mai Thai', 'Thai')
print(f'my resturant is called {mai_thai.resturant_name}')
mai_thai.describe_resturant()
mai_thai.resturant_open()'''

#_____________________9.2 Three Resturants (i did two)
'''happy_hooligan = Resturant('Happy Hooligans', 'Vegitarian comfort food')
jonny_rocket = Resturant('Jonny Rockets', 'Classic American')

print(f'My favorite resturant {happy_hooligan.resturant_name} sadly went out of buisness')
happy_hooligan.describe_resturant()'''

#_____________________9.3 User 

'''class User:
    """Initilize a User profile."""
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email
        self.location = location
        
    def describe_user(self):   # i thought i could use a for loop to print each argument 
        """Displays a summary of the users info"""
        print(f' User info: {self.first_name} {self.last_name} ')
        print(f"{self.age} + {self.email} + {self.location}")
        
    def greet_user(self):
        """Prints a greeting to the user"""
        print('\nSuh bruh, nice to meed you' + self.first_name + self.last_name)
        
joe = User('joe', 'strong', 2, 'poop@poopmail.com', 'there')
joe.describe_user()
joe.greet_user()'''

#____________________ 9.4 Number Served (reuse excer from 9.1)
class Resturant:
    """A simple model of a resturant showing the name and cuisine"""
    
    def __init__(self, resturant_name, cuisine_type):
        """Initilize the Resuturant (as the book wrote it)."""
        self.resturant_name = resturant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0 #this is an attribute 
        
        
    def describe_resturant(self):  # this is a method
        """Returns a message about resturant name"""
        msg = msg = self.resturant_name + " serves wonderful " + self.cuisine_type + " cuisine."
        print(msg)
            
    def resturant_open(self): 
        """Returns a message about resturant being open"""
        print(f'{self.resturant_name} is Open')

    def set_num_serverd(self, num_serve):
        """Set the number of customers served"""
        if num_serve >= self.number_served:
            self.number_served = num_serve
        else: 
            print('you cant unserve folks')
        
    def increment_num_served(self,guest):
        """"Incriment the number of guests served """
        self.number_served += guest
        
        
happy_hooligans = Resturant('happy hooligans', 'Vegan comfort')
happy_hooligans.number_served = 200
print(happy_hooligans.number_served)

happy_hooligans.increment_num_served(3)
print(happy_hooligans.number_served)

#____________________ 9.5 Login Attemps (using excercise from 9.1)

class User:
    """Initilize a User profile."""
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0 
        
    def describe_user(self):   # i thought i could use a for loop to print each argument 
        """Displays a summary of the users info"""
        print(f' User info: {self.first_name} {self.last_name} ')
        print(f"{self.age} + {self.email} + {self.location}")
        
    def greet_user(self):
        """Prints a greeting to the user"""
        print('\nSuh bruh, nice to meed you' + self.first_name + self.last_name)
    
    def incriment_login_attempts(self):
        """Incriment login attempts by input amount"""
        self.login_attempts += 1
    
    def reset_login_attempts(self): # im proud of this bit of code extra
        """Reset the number of login attempts"""
        if self.login_attempts >= 3:
            print('reset login attepmts, max number reached')
            self.login_attempts = 0 
        else:
            print(f'you have {3 - self.login_attempts} remaining') # didnt know i could subtract
            
        
joe = User('joe', 'strong', 2, 'poop@poopmail.com', 'there')
joe.describe_user()
joe.greet_user()
joe.incriment_login_attempts()
print(joe.login_attempts)
joe.incriment_login_attempts()
joe.incriment_login_attempts()
print(joe.login_attempts)
joe.reset_login_attempts()
print(joe.login_attempts)

#_____________________ 9.6 Ice Cream Stand

class Ice_cream_stand(Resturant):
    """"Represents an Ice Cream Stand Resturant"""

    def __init__(self, resturant_name, cuisine_type='ice cream'):
        """Initilize the Resuturant (as the book wrote it).
        Then initilizes the Ice Cream Stand methods"""
        super().__init__(resturant_name, cuisine_type)
        self.flavors = []
        
    def show_flavors(self):
        """Shows flavors avaliable in Stand"""
        print('We have the following flavors: ')
        for flavor in self.flavors:
            print('\t -' + flavor)
            
chocotown = Ice_cream_stand('Chocotown', 'ice cream')
chocotown.flavors = ['Chocolate', 'Vanilla', 'Mint Chip', 'Peanut Butter Chocolate',]
chocotown.describe_resturant()
chocotown.show_flavors()
        
#________________________ 9.7 Admin (user Class)
class Admin(User):
    """Special Admin User Class"""
    def __init__(self, first_name, last_name, age, emial, location):
        """Initilize Admin User Class"""
        super().__init__(first_name, last_name, age, emial, location)
        self.privileges = Privileges()
         
class Privileges():
    """Class for User Privileges"""
    def __init__(self, privileges=[]):
        """Initializes Privileges Class"""
        self.privileges = privileges
    
    def show_privilegs(self):
        """Shows Privileges avaliable for User"""
        print("User has the following privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print("\t-" + privilege)
        else:
            print('User has no privileges')   
    
admin_leaf_supreme = Admin('leaf', 'supreme', 999, 'leaf_supreme@leaf.supreme', 'your mind')        
admin_leaf_supreme.privileges.show_privilegs()
admin_leaf_supreme.describe_user()
# NOTICE below privileges.privileges was called to referecene both Privilege class and User class
admin_leaf_supreme.privileges.privileges = ['can add post', 
                                            'can delete post', 
                                            'can ban use', 
                                            'can add user',
                                            ] 
admin_leaf_supreme.privileges.show_privilegs()
#__________________9.8 Privilege Class for Admin (needed to add it above in 9.7 )

#__________________ 9.9 Battery Upgrade (i could copy classes but i will type for praccy)
class Car():
    """Simple model of a Car"""
    def __init__(self, make, model, year):
        """Initilize Car"""
        self.make = make
        self.model = model
        self.year = model
        self.odometer_reading = 0
    
    def get_descritption(self):
        """Return a formatted discription of Car"""
        long_name = f'{self.year} {self.make.title()} {self.model.title()}'
        return long_name
    
    def read_odometer(self):
        """Read Current Odometer"""
        print(f' Your car has {self.odometer_reading} miles on it')
        
    def update_odometer(self, milage):
        """Updates Odometer reading of Car"""
        if self.odometer_reading <= milage:
            self.odometer_reading = milage
        else:
            print('You cant turn back the miles')
            
    def incement_odometer(self, miles):
        """Incirments miles on Odometer"""
        self.odometer_reading += miles
        
class Battery():
    """Composition of a Class for a Car Battery for electric car"""
    def __init__(self, battery_size=40):
        """Initilize class for Electric Car Battery"""
        self.battery_size = battery_size
        
    def describe_battery(self):
            """Describes battery size of electric car"""
            print(f"This car has a {self.battery_size}-kWhr battery.")
            
    def get_range(self):
        """Prints Information about battery size to distance avaliable"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
            print(f'With a {self.battery_size}-kWH battery you have a range of {range}-miles')
            
    def battery_upgrade(self):
        """Upgrade Battery size"""
        if self.battery_size == 40:
            self.battery_size = 65
        else:
            print('Your battery is already at the maximum allowable')
                         
class ElectricCar(Car):
    """Create Electric Car Class"""
    
    def __init__(self, make, model, year, battery_size=40):
        """Initilize Attributes of Parent Class
        Then initilize attributes specific to Electric Car"""
        super().__init__(make, model, year)
        self.battery_size = Battery()
            
my_polestar = ElectricCar('Polestar', '2', 2023)
my_polestar.battery_size.describe_battery()  #battery_size calls the Battery() class 

my_polestar.battery_size.battery_upgrade()
my_polestar.battery_size.describe_battery()
my_polestar.read_odometer()
my_polestar.incement_odometer(120_200)
my_polestar.read_odometer()

#___________________ 9.10 Imported Resturant, 9.11 and 9.12 done on seperate file
#importing modules e.g. from CCP_CH9 import Car, ElectricCar
#                      from CCP_CH9 import *   (imports all but not descriptive or helpful to read)
#                      from CCP_CH9 import ElectricCar as EC  

#_________________ 9.13 Dice (importing from Python Library Random and Choice)

'''from random import randint
random = randint(1,21)
print(random)'''

class Die():
    """Class for 6 side Dice Rolling"""
    def __init__(self, side=6):
        """Initilize Dice with standard 6 sides"""
        self.side = side
        
    def roll_die(self):
        """Rolls dice with random value"""
        from random import randint # you can import in a module (maybe only python native library)
        print(randint(1,self.side)) # you should import before Class, and return value not print
        
d_d = Die(side=10) # this works to generate random number for specified sides of dice 
d_d.roll_die() #I want to make a list and store the values made in a list then run a loop # of times
roll = 1
rolls = []
while roll < 10:
    d_d.roll_die()# i had print(d_d.roll_die()) which was retunring # then none then #, no print
    roll += 1
    
# as the book has it, we more or less has the same Class definition which i goto on my own!!! 
# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):  # i couldnt think of the range function, and my append was messing up
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(side=10) 

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result) 
print("\n10 rolls of a 10-sided die:")
print(results) # this wont work before i printed the randint not returned it as in the book
# i was still able to get mine to work well enough so ill leave it as it was completed with min help

#__________________________ 9.14 Lottery 9.15 Lottery Analysis (difficult!!)
from random import choice
# this was my attempt, it worked to pull the ticket but the analysis as hard
'''lotto = (1,'a',2,'b',3,'c',4,'d',5,'e',6,7,8,9,10,)
my_ticket = ['a',1,'b',2]
winning_nums = []
count = 0
while my_ticket != winning_nums:
    for i in range(4):
        winner = choice(lotto)
        winning_nums.append(winner)
        count += 1
    if winning_nums == my_ticket:
        break
print(count)'''

# 9.15 as the book has it. Very neat!
def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}") 
# addind small change to push sync

#_______________________________________________________________________________
#_______________________________________________________________________________
#________________________ CHAPTER 10 Files and Extensions_______________________

pi = 3.141592653589793238462643383279

from pathlib import Path

path = Path('pi_30dig.txt')
contents = path.read_text() # can also path.read_text().rstrip() which is called method chaining
contents = contents.rstrip()  # removes whitespace to the right side of data
print(contents)

# if we want do display pi as a bigass string
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

# Relative and Absolute Paths
# path = Path('text_files/filename.txt')   file needs to be inside the place were current file is
# Absolute: path = Path('C:\Users\kylem\OneDrive\Documents\Python_Code\Crash_Course_practice\Crash_Course_practice/pi_30dig.txt')
# Absolute is the most direct and will be something i need to learn! also add the file name at the end foo

#_________PI to 1 million digis :0___________________
path1 = Path('pi_million_digits.txt')
content1 = path1.read_text()
lines1 = content1.splitlines()
pi_string1 = ''
for liness in lines1:
    pi_string1 += liness.lstrip()
print(f'{pi_string1[:52]}...')
print(len(pi_string1))

#__________________________ 10.1 Learning Python 
learn = Path('Learning_python_kh.txt')
learnt = learn.read_text().splitlines() # splitlines is a useful function 
goals = []
for phrase in learnt:
    goals.append(phrase)
"""print(goals)"""

#___________________________ 10.2 Learning C
message = "I really like cats"
message.replace('cats', 'dogs')
for strn in learnt:                   # I tried several times,i was very close (splitlines is key)
    strn = strn.replace("Python", "C#")#i needed to assign strn to the strn.replace() otherwise fail
    """print(strn)"""
    
#_____________________________ 10.3 Simpler Code
path2 = Path('pi_30dig.txt')
contents2 = path2.read_text()
for line in contents2.splitlines(): # it said make more concise, i put next to read_text(), they dnt
    print(line) 
    
#_____________________________ 10.4 Guest (learn to write to a txt file, BE WEARY YOU CAN OVERWRITE)
msg = ("Please input Guests name")
msg += ("\nEnter 'q' to exit: ")
names = ['bill',]
while 'quit' not in names:
    mesg = input(msg)
    if mesg == 'q':
        break 
    names.append(mesg)
print(names)  # This worked but quit appears in list. i iwll need to sort that out. 
#all i had to do was move the append after the break statement. Fixed!!!

#________________________ 10.5 Guest Book (adding names to .txt)
name = Path('names_galore.txt')
name.write_text(str(names))  

##______________## How Author did it
'''path = Path('guest_book.txt')
prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)'''

#______________________________ 10.6 Addition (try and except) & 10.7 Addition Calculator

add_1 = "First number: "
add_2 = '"q" to quit'
add_2 += "\nSecond number: "
while True:
    num_1 = input(add_1)
    if num_1 == 'q':
        break
    
    num_2 = input(add_2)
    if num_2 == 'q': # all works well....except i have to input q twice and # or # == 'q' didnt work
        break 
    
    else:
        try:
            add_eq = int(num_1) + int(num_2)
        except ValueError:
            print("Use Numbers Dumbass")
        else:
            print (f' the sum of {num_1} and {num_2} is {add_eq}')
            
# The books version 
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
    
#________________________ 10.7 Cats and Dogs 
# below written to create a text files
'''from pathlib import Path
dog_name = ['Doggo', 'Buddy', 'Fido', 'Beau',]
cat_name = ['Gus', 'lady', 'puss', 'Simo']

dogs_name = Path('dog_names.txt')
dogs_name.write_text(str(dog_name))
cats_name = Path('cat_names.txt')
cats_name.write_text(str(cat_name))'''

try:
    read_dog = Path('dog_names.txt')
    read_dogs = read_dog.read_text().splitlines()
except FileNotFoundError:
    print('The file you are looking for is not in this directory')
else:
    print(read_dogs)

try:
    read_cat = Path('cat_names.txt')
    read_cats = read_cat.read_text().splitlines()
except FileNotFoundError:
    pass   # silent error passing
else:
    print(read_cats)
# The books version 

filenames = ['cat_names.txt', 'dog_names.txt']

for filename in filenames:
    path_a = Path(filename)
    try:
        contents_a = path_a.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents_a)
        
        
#______________________ 10.10 Common Words (Cool e-book site for all public domain books)
# _________ https://www.gutenberg.org/ ______________

e_book = ['Beaowulf.txt', 'Dracula.txt', 'Treasure_island_a.txt', 'War_and_Peace.txt',]

path_1 = Path('my_doc.txt')
reader = path_1.read_text()
the_s = reader.count('the')
print(the_s)

for book in e_book:
    path_b = Path(book)
    try:
        pathy = path_b.read_text()
    except FileNotFoundError:
        print('file not found')
    except UnicodeDecodeError:
        print('not a fuckin clue')
    else:
        count_the = pathy.lower().count('the')
        count_space_the = pathy.lower().count('the ')
        print(f'{book} has "the" {count_the} times')
        print(f'{book} has "the " {count_the} many times')
        
#_________________________ json file son (Java Script Object Notation )
#Pyton can output a data structured as a formatted string that can be read across many languages. 

#from pathlib import Path 
import json 
numbers = [2,4,5,2,7,2,6,9,4,9,6,8,]

path = Path('numbers.txt')
contents3 = json.dumps(numbers)
path.write_text(contents3) 
#then to read text 
pathy = Path('numbers.txt')
contents4 = path.read_text()
numbers = json.loads(contents4)
print(numbers)
        
#____________________ 10.11 Favotite Number and 10.12 (i did it in order)

def get_user_num(path):
    """Obtain Stored info on users favorite number"""
    if path.exists():
        contents6 = path.read_text()   #read text from Path we define
        nummy = json.loads(contents6) 
        return nummy
    else:
        return None 
    
def store_user_num(path):
    """Store input from users favorite number"""
    prompt = 'Please input your favorite number: '
    fav_num = input(prompt)  
    contents6 = json.dumps(fav_num)     
    path.write_text(contents6) 
    return fav_num

def user_num():
    """Show the users favorite number"""
    path = Path('user_number.json')
    nummy = get_user_num(path)
    if nummy:
        print(f'your favorite number is {nummy}')
    else: 
        store_user_num(path)
        print(f'well write down your favorite number')

user_num()   #it literally worked the first time i ran it!!! hells yes

# The books version is far more elegant
#10.11
'''path = Path('favorite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")

number = input("What's your favorite number? ")
#______________________________________________
path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember that number.")

# 10.12 using the above code 
path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")'''

#_______________________________ 10.13 User Dictionary 
def get_stored_username(path):  #to call get_stored_...(path) <- you need to input path into fxn
    """Get Stored Username from json if avaliable"""
    if path.exists(): # .exsists() returns a Boolean value corrcect 
        contents5 = path.read_text()
        username = json.loads(contents5)
        return username 
    else:
        return None 
    
def get_new_username(path):
    """Promt for new user info"""
    user_dict = {'username':'',
                 'location': '',
                 'age': '',
                 }
    user_dict['username'] = input("What is your name? ")
    user_dict['location'] = input('Where are you located: ')
    user_dict['age'] = input('How old are you: ')
    contents5 = json.dumps(user_dict)
    path.write_text(contents5)
    return user_dict

def greet_user():
    """Greet User by Username"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        return_user = input(f'Are you {username}, y/n? ')
        if return_user == 'y':
            print(f'Welcome back {username}!')
        elif return_user == 'n':
            username = get_new_username(path)
            print(f"We'll rember you for next time, {username}! ")
    else:
        username = get_new_username(path)
        print(f"We'll rember you for next time, {username}! ")
        
greet_user() # Holy Shit Again 1st Try and no help from book or answer sheet, his answer even has
# user_dict...how funny. He did say i was supposed to call out each new feature in the greet_user :\

#_________________________10.14 uses the same file but check if user is correct user 
# IT IS TRIPPING ME OUT SO MUCH, HE ALMOST WROTE THE EXACT SAME CODE!!! THE ONLY DIFF IS
# HE USED CORRECT IN STEAD OF RETURN_USER.......DUDE ITS BLOWIN MY MIND. 
#_____________________________ END CHAPTER 10, ONTO CH11____________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#___________________________________________________________________________________________________
#_______________________ CHAPTER 11 Testing Your Code_______________________________________________

# firstly make sure pip is upgraded ($ python -m pip install --upgrade pip)
# You can use this to install an upgrade on any  ($ python -m pip install --upgrade package_name)
# the same goes for installing   ($ python -m pip install --user package_name)
# e.g. $ python -m pip install --user pytest   

from name_fxn import get_formatted_name

print('Enter "q" at any time to quit')
while True:
    first = input(f'\nPlease input your first name: ')
    if first == 'q':
        break
    last = input(f'\nInput your last name: ')
    if last =='q':
        break
    
    formated_name = get_formatted_name(first, last)
    print(f"\n Neatly Formatted name: {formated_name}")
# in order to run pytest from terminal i needed to run $ python -m pytest and it worked. 
# the terminal is running from same location as where pytest is i think...not sure why its an issue
    
#____________________________________ 11.1 City Country 
#making a new fuction and adding code written in different files just to sum up what was done

'''def get_formatted_name(first, last):
    """Return a neatly formatted name"""
    full_name = f'{first} {last}'
    return full_name.title()


from name_fxn import get_formatted_name

def test_first_last_name():
    """Test if First and Last Name will format correctly"""
    formatted_name = get_formatted_name('jimi', 'hendrix',)
    assert formatted_name == "Jimi Hendrix"
    
    
def city_functions(city, country, population=None):
    """Return formatted name of city and coutry"""
    if population: 
        return (f'{city.title()}, {country.title()} has a population of -{population}')
    else:
        city_country = (f'{city.title()}, {country.title()}')
        return city_country

san = city_functions('san jose', 'california')
print(san)

saratoga = city_functions('Saratoga','CA', 90000)
print(saratoga)

from city_fxns import city_functions

def test_city_country_name():
    """Test is City and Country are formatted correctly """
    city_country = city_functions('san jose', 'california')
    assert city_country == 'San Jose, California'
    
def test_city_country_pop_size():
    "Test if City, Country, and pop size are formatted"
    saratoga = city_functions('saratoga', 'california', 180000)
    assert saratoga == ('Saratoga, California has a population of -180000')'''

#Common uses and assertions for test classes
# assert a == b
# assert a != b
# assert a  (True or False)
# assert not a
# assert element in/not in list 

# Fixtures esentially set up a test env.
# they require a decerator which goes at the front of a function
# @pytest.fixture
# def language_survey(): and so on ->
# you are building am object or function that other tests can call upon 

class AnonymousSurvey:
    """Collect anonamous answers to survey questions"""
    def __init__(self,question):
        """Store a question and prepair to store responses"""
        self.question = question 
        self.responses = []
        
    def show_question():
        """Show survey question"""
        print(self.question)
        
    def store_response(self, new_response):
        """store a single new response"""
        self.responses.append(new_response) 
        
    def show_results(self):
        """Show all responses"""
        print("Survey Results: ")
        for response in self.responses:
            print(f" - {response}")
            
'''from CCP_CH11 import AnonymousSurvey

# define question
question = "What languages did you first learn to speak? "
language_survey = AnonymousSurvey(question)

# show questions and response
language_survey.show_question()
print("Enter 'q' to quit at any time \n")
while True:
    response = input('Language ')
    if response == 'q':
        break 
    language_survey.store_response(response)
    
#Show results of survey
print(f"\nThank you to everyone who participated in the survey!")
language_survey.show_question()'''

# To test the survery reposnse 
# 1 single test for multiple resposes 

'''def test_store_three_responses():
    """Test three responses"""
    question = "What languages did you first first learn to speak? "
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Mandrin', 'Spanish',]
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses'''
        
# testing using a fixture
# @pytest.fixture
# def language_survey():
# """A Survey that will be avalaible to all test functions"""
#    question = "What languages did you first first learn to speak? "
#    language_survey = AnonymousSurvey(question)
#    return language_survey
# def test_store_single_response():
#     """Test single response stored"""
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses
#