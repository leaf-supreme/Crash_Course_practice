#_______________________________________________________________________________
#_______________________________________________________________________________
#________________________ CHAPTER 10 Files and Extensions_______________________

pi = 3.141592653589793238462643383279

from pathlib import Path

path = Path('pi_30dig.txt')
contents = path.read_text() # can also path.read_text().rstrip() which is called method chaining
contents = contents.rstrip()  # removes whitespace to the right side of data
print(contents)

# if we want do display pi as a bigass string
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

# Relative and Absolute Paths
# path = Path('text_files/filename.txt')   file needs to be inside the place were current file is
# Absolute: path = Path('C:\Users\kylem\OneDrive\Documents\Python_Code\Crash_Course_practice\Crash_Course_practice/pi_30dig.txt')
# Absolute is the most direct and will be something i need to learn! also add the file name at the end foo

#_________PI to 1 million digis :0___________________
path1 = Path('pi_million_digits.txt')
content1 = path1.read_text()
lines1 = content1.splitlines()
pi_string1 = ''
for liness in lines1:
    pi_string1 += liness.lstrip()
print(f'{pi_string1[:52]}...')
print(len(pi_string1))

#__________________________ 10.1 Learning Python 
learn = Path('Learning_python_kh.txt')
learnt = learn.read_text().splitlines() # splitlines is a useful function 
goals = []
for phrase in learnt:
    goals.append(phrase)
"""print(goals)"""

#___________________________ 10.2 Learning C
message = "I really like cats"
message.replace('cats', 'dogs')
for strn in learnt:                   # I tried several times,i was very close (splitlines is key)
    strn = strn.replace("Python", "C#")#i needed to assign strn to the strn.replace() otherwise fail
    """print(strn)"""
    
#_____________________________ 10.3 Simpler Code
path2 = Path('pi_30dig.txt')
contents2 = path2.read_text()
for line in contents2.splitlines(): # it said make more concise, i put next to read_text(), they dnt
    print(line) 
    
#_____________________________ 10.4 Guest (learn to write to a txt file, BE WEARY YOU CAN OVERWRITE)
msg = ("Please input Guests name")
msg += ("\nEnter 'q' to exit: ")
names = ['bill',]
while 'quit' not in names:
    mesg = input(msg)
    if mesg == 'q':
        break 
    names.append(mesg)
print(names)  # This worked but quit appears in list. i iwll need to sort that out. 
#all i had to do was move the append after the break statement. Fixed!!!

#________________________ 10.5 Guest Book (adding names to .txt)
name = Path('names_galore.txt')
name.write_text(str(names))  

##______________## How Author did it
'''path = Path('guest_book.txt')
prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)'''

#______________________________ 10.6 Addition (try and except) & 10.7 Addition Calculator

add_1 = "First number: "
add_2 = '"q" to quit'
add_2 += "\nSecond number: "
while True:
    num_1 = input(add_1)
    if num_1 == 'q':
        break
    
    num_2 = input(add_2)
    if num_2 == 'q': # all works well....except i have to input q twice and # or # == 'q' didnt work
        break 
    
    else:
        try:
            add_eq = int(num_1) + int(num_2)
        except ValueError:
            print("Use Numbers Dumbass")
        else:
            print (f' the sum of {num_1} and {num_2} is {add_eq}')
            
# The books version 
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
    
#________________________ 10.7 Cats and Dogs 
# below written to create a text files
'''from pathlib import Path
dog_name = ['Doggo', 'Buddy', 'Fido', 'Beau',]
cat_name = ['Gus', 'lady', 'puss', 'Simo']

dogs_name = Path('dog_names.txt')
dogs_name.write_text(str(dog_name))
cats_name = Path('cat_names.txt')
cats_name.write_text(str(cat_name))'''

try:
    read_dog = Path('dog_names.txt')
    read_dogs = read_dog.read_text().splitlines()
except FileNotFoundError:
    print('The file you are looking for is not in this directory')
else:
    print(read_dogs)

try:
    read_cat = Path('cat_names.txt')
    read_cats = read_cat.read_text().splitlines()
except FileNotFoundError:
    pass   # silent error passing
else:
    print(read_cats)
# The books version 

filenames = ['cat_names.txt', 'dog_names.txt']

for filename in filenames:
    path_a = Path(filename)
    try:
        contents_a = path_a.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents_a)
        
        
#______________________ 10.10 Common Words (Cool e-book site for all public domain books)
# _________ https://www.gutenberg.org/ ______________

e_book = ['Beaowulf.txt', 'Dracula.txt', 'Treasure_island_a.txt', 'War_and_Peace.txt',]

path_1 = Path('my_doc.txt')
reader = path_1.read_text()
the_s = reader.count('the')
print(the_s)

for book in e_book:
    path_b = Path(book)
    try:
        pathy = path_b.read_text()
    except FileNotFoundError:
        print('file not found')
    except UnicodeDecodeError:
        print('not a fuckin clue')
    else:
        count_the = pathy.lower().count('the')
        count_space_the = pathy.lower().count('the ')
        print(f'{book} has "the" {count_the} times')
        print(f'{book} has "the " {count_the} many times')
        
#_________________________ json file son (Java Script Object Notation )
#Pyton can output a data structured as a formatted string that can be read across many languages. 

#from pathlib import Path 
import json 
numbers = [2,4,5,2,7,2,6,9,4,9,6,8,]

path = Path('numbers.txt')
contents3 = json.dumps(numbers)
path.write_text(contents3) 
#then to read text 
pathy = Path('numbers.txt')
contents4 = path.read_text()
numbers = json.loads(contents4)
print(numbers)
        
#____________________ 10.11 Favotite Number and 10.12 (i did it in order)

def get_user_num(path):
    """Obtain Stored info on users favorite number"""
    if path.exists():
        contents6 = path.read_text()   #read text from Path we define
        nummy = json.loads(contents6) 
        return nummy
    else:
        return None 
    
def store_user_num(path):
    """Store input from users favorite number"""
    prompt = 'Please input your favorite number: '
    fav_num = input(prompt)  
    contents6 = json.dumps(fav_num)     
    path.write_text(contents6) 
    return fav_num

def user_num():
    """Show the users favorite number"""
    path = Path('user_number.json')
    nummy = get_user_num(path)
    if nummy:
        print(f'your favorite number is {nummy}')
    else: 
        store_user_num(path)
        print(f'well write down your favorite number')

user_num()   #it literally worked the first time i ran it!!! hells yes

# The books version is far more elegant
#10.11
'''path = Path('favorite_number.json')
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")

number = input("What's your favorite number? ")
#______________________________________________
path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print("Thanks! I'll remember that number.")

# 10.12 using the above code 
path = Path('favorite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I'll remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")'''

#_______________________________ 10.13 User Dictionary 
def get_stored_username(path):  #to call get_stored_...(path) <- you need to input path into fxn
    """Get Stored Username from json if avaliable"""
    if path.exists(): # .exsists() returns a Boolean value corrcect 
        contents5 = path.read_text()
        username = json.loads(contents5)
        return username 
    else:
        return None 
    
def get_new_username(path):
    """Promt for new user info"""
    user_dict = {'username':'',
                 'location': '',
                 'age': '',
                 }
    user_dict['username'] = input("What is your name? ")
    user_dict['location'] = input('Where are you located: ')
    user_dict['age'] = input('How old are you: ')
    contents5 = json.dumps(user_dict)
    path.write_text(contents5)
    return user_dict

def greet_user():
    """Greet User by Username"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        return_user = input(f'Are you {username}, y/n? ')
        if return_user == 'y':
            print(f'Welcome back {username}!')
        elif return_user == 'n':
            username = get_new_username(path)
            print(f"We'll rember you for next time, {username}! ")
    else:
        username = get_new_username(path)
        print(f"We'll rember you for next time, {username}! ")
        
greet_user() # Holy Shit Again 1st Try and no help from book or answer sheet, his answer even has
# user_dict...how funny. He did say i was supposed to call out each new feature in the greet_user :\

#_________________________10.14 uses the same file but check if user is correct user 
# IT IS TRIPPING ME OUT SO MUCH, HE ALMOST WROTE THE EXACT SAME CODE!!! THE ONLY DIFF IS
# HE USED CORRECT IN STEAD OF RETURN_USER.......DUDE ITS BLOWIN MY MIND. 
#_____________________________ END CHAPTER 10, ONTO CH11____________________________________________
#___________________________________________________________________________________________________
