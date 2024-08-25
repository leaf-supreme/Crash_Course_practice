#Employee Class

class Employee():
    """Initilize a class to define an employee"""
    def __init__(self,first_name, last_name, year_money):
        self.first_name = first_name
        self.last_name = last_name
        self.year_money = year_money
        
    def employee_info(self):
        """Shows Employees formatted name and salary"""
        employee = (f'Name : {self.first_name.title()} {self.last_name.title()} \nSalary: {self.year_money}')
        return employee
    
    def give_raise(self, payraise=5000):
        self.year_money += payraise
        
#    def give_raise(self):
#        standard_raise = input("will this be a standard 5000$ raise, y/n? ")
#        if standard_raise == 'y':
#            self.year_money += 5000    # self.year_money needed to be variable to update original,+=
#        else:
#            non_std_raise = int(input('Please specify raise amount?  '))
#            self.year_money += non_std_raise
#_____The above code works well but i dont know how to test user input well (maybe monkeypatch)_____  
   
bill = Employee('bill', 'liib', 98_000)
billy = bill.employee_info()
print(billy)

robin = Employee('robin', 'everet', 88_000)
print(robin.employee_info())
robin_raise = robin.give_raise(4999)
robin_info = robin.employee_info()
print(robin_info)