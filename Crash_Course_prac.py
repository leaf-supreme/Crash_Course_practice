#CCP_Google_Collab

print("This is where the world ends")
print("If i say hello world one more time, I may just take it over")
#import this # this is a poem by tim peters for code edequite, kind of fun
name = "hello to all!"
name.title() # upper and lower as well

#insert a variable into a string, f variable
first_name = " 'bob' "
last_name = " dole "
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#white spaces you can add whitespace or strip it
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#first_name.rstrip(), first_name.lstrip(), first_name.strip(), 
# first_name.removesuffix(), first_name.removeprefix()

# simple data set 
bicycles = ['trek', 'cannondale', 'santa cruz', 'fuji', 'look', 'pinarello', 'specalized', 'surley', 'all-city', 'giant']
first_bike = (f"My First Bicycle was a {bicycles[6]}")
print(first_bike)
bicycles[0] = 'trekk'
bicycles.append('canyon') # always adds it to the end
bicycles.insert(2, 'fairlight')
last_item = bicycles.pop() #removes last item on list but lets you use it first, you can also specify .pop(2)...
print(f"The last bike i will not own is a {last_item}")
to_expensive = bicycles.remove('pinarello') # doesnt remove all instances of item, use loop to remove
sorted_bikes = bicycles.sort()  # bicycles.sort(reverse=TRUE), displays sorted but not permanent, bicycles.reverse() is permanent



