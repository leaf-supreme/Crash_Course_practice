#CCP_CH7 Practice 
#_______________________________________________________________________________
#_______________________________________________________________________________
#7.1 Rental Car
rental_car = 'What kind of rental car would you like, we have many options '
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
        'chicken': 'cord on blu',
        'Beef':'steak',
        'Sheep': 'shank',
        },
    'vegitable': 
        {'broccoli': 'pan-fried',
        'squash': 'patties',
        'potato': 'The Perfect food',
        },
    'carbo': 
        {'pasta': 'macarroni',
        'bread': 'Sourdough',
        'pastry': 'snail',
        }
}
for group, subgroup in food.items():
    
    print(f'The best {group['chicken'.title()]}')
    
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