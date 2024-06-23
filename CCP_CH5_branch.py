#testing to see if this is the branch that i can then merge to the main CCP practice branch 
#starting with Chapter 5 practice so i dont need to review a massive file the whole time 
#  5.3 Alien Colors
alien_color = "green"
if alien_color == "green":
    print("player earned 5-pts")
if alien_color == "red":
    print("0 pts")

# 5.4 Alien Colors 2
alien_color = "green"
if alien_color == "green":
    print("you've earned 5 pts")
else:
    print("you've earned 10 pts")

#5.5 Alien Colors #3
alien_color = "green"
player_name = "Kilgore"
if alien_color == "green":
    print(f"{player_name} earned 5 pts")
elif alien_color == "yellow":
    print(f"{player_name} earned 10 pts")
else:
    print(f"{player_name} earned 15 pts")
    
# 5.6 Stages of life using if-elif-else chain
age = 65

if age <= 2:
    print("you are bby")
elif 2 < age <= 4:
    print("you are toddler")
elif 4 < age < 13:
    print("you is kid")
elif 13 <= age < 20:
    print("you is teenager")
elif 20 <= age < 65:
    print("you is adult")
elif age >= 65:
    print("you is elder")
else:
    print("you are unalive")
    
#5.7 Favorite Fruits 
fav_fruit = ["strawberry", "blueberry", "bananna", "mango", "apple", "avacado"]

if "apple" in fav_fruit:
    print(f"you really like {fav_fruit[4]}")
if "bean" in fav_fruit:
    print("you really like bean")
else:
    print("you dont like bean")
    

    
# 5.8 Hello Admin/ and 5.9 Checking for Username (empty list[] with if/else)
# adding 5.10 to the code as well______pause point at 5.10 new_user list
current_user = ['admin', 'liver_wurst', 'pooty_tang', 'Reginald', 'user']
new_user = ['rustabell', 'Liver_wurst', 'rap raplinger']

current_user_lower = [user.lower() for user in current_user]
print(current_user_lower)


for new in new_user:  #check to see if new user name is in current user
    if new.lower() in current_user_lower: # do not forget to check in list use keyword "in"
        print( new + " you need to find a new name")
    elif new not in current_user:
        print(f"{new} is avaliable")

if current_user:  # check on users with account, and special for admin
    for user in current_user:
        if user == 'admin':
            print("Hello Admin, \nwould you like status report?")
        if user != 'admin':
            print(f"Hello {user}, \nwhere may i direct you")
else:
    print("you do not have an account foo!")
    
    
#cool bit of code from Mimo app with user input
'''name = input("Hello! What is your name?  ")
print(f"Nice to meet you {name}!")
age_input = input("How old are you?:")
age = int(age_input)
bot_age=3
age_difference= age - bot_age
print(f"You are {age_difference} years older them me. I'm only {bot_age} years old!")
color = input("What's your favorite color?: ")
print(f"Oh, {color} really is a beautiful color")'''

# 5.11 ordinal numbers 
ord_num = list(range(1,10))

for num in ord_num:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    elif num >= 4:
        print(str(num) + "th")
#will it publish to main?
print(3)



