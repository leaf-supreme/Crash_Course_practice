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
=======
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
=======

# 6.7 People using bilbo and makin two others
samwise = {'first_name': 'Samwise',
           'last_name': 'Gamgee',
           'age': '65',
           'city': 'The Shire',
           }
meri = {'first_name': 'Meridoc',
        'last_name': 'Took',
        'age': '54',
        'city': 'The Shire',
        }
pippin = {'first_name': 'Pippin',
          'last_name': 'Brandybuck',
        'age': '55',
        'city': 'The Shire',
        }
people = [bilbo,  samwise, meri, pippin]
for keys, values in people.items():
    print(value.title())


