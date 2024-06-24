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
    

    