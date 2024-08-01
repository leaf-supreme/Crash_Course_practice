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