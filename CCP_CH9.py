#_______________________________________________________________________________
#_______________________________________________________________________________
#_______________________Chapter 9 Classes_______________________________________

class Dog:
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
            
