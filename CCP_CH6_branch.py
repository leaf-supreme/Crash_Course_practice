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