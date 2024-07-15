#CCP_CH7 Practice 
#_______________________________________________________________________________
#_______________________________________________________________________________
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
    