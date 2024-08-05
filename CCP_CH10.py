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
msg = ("Please input Guests name: ")
names = ['bill',]
while 'quit' not in names:
    mesg = input(msg)
    if mesg == 'quit':
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


