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
    
