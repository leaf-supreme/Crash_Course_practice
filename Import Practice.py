#__________________________9.10 Imported Resturant
from CCP_CH9 import ElectricCar
my_mazda = ElectricCar('mazda', '3 Skyactiv', '2012')
my_mazda.battery_size.describe_battery()
my_mazda.battery_size.battery_upgrade()
my_mazda.battery_size.describe_battery()

#_______________________9.11 Imported Admin & 9.12 Multiple modules (by accident)
from CCP_CH9 import User, Admin, Privileges
admin_ciena = Admin('ciena','unicorn', 100, 'unicorn@uni.corn', 'rhode island')
admin_ciena.privileges.show_privilegs()
admin_ciena.privileges.privileges = ['ban users',
                                  'create users',
                                  'ban user to shadow realm',
                                  'allow user to draw 3 cards from the top of their deck',
                                  ]
admin_ciena.privileges.show_privilegs()