#_______________________________________________________________________________
#_______________________Chapter 8 - Functions Practice__________________________
# 8.1 Message 
def display_massage():
    """Displayes a what CCP_CH8 is about"""
    print('This Chapter is about defining functions')
    
display_massage()

# 8.2 Favorite Book
def favorite_book(title):  # the variable title is a 'parameter' for a function (def)
    """Displays favorite book using user input"""
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

# 8.3 T-shirt
def make_shirt(size='N/A', color='White', text="N/A"):
    """Displays shirt size and text on front"""
    print(f"You're shirt is size {size}, {color.title()} and willl display {text}")
make_shirt(12,'Blue', "Gimmie Dat $$Money$$")

#8.4 Large Shirt and 8.5 are completed with above code, this is easier to understand.....right now

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

# 8.6 City names
def city_country(city_name, country_name):
    """Returns a formatted name of your City and Country"""
    location = (city_name.title() + " , " + country_name.title())
    return location
san_jose = city_country('san jose', 'united states')
print(san_jose)

# also written -> return(city.title() + "," + country.title())

# 8.7 Album 
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

# 8.8 User Albums 

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
     
