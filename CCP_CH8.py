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
        
kyles_which = sandwhich_order('Large', 'titties','soup', 'tittie soup')

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
