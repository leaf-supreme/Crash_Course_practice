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
    
    def read_odometer():
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
my_polestar.describe_battery()

my_polestar.upgrade_battery()
my_polestar.describe_battery()
        