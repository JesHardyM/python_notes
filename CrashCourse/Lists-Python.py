Lists Python

x = ["Now", "we", "are", "cooking!"]
type(x)

#returns: <class 'list'>

x = ["Now", "we", "are", "cooking!"]
print(x)

#returns: ['Now', 'we', 'are', 'cooking!']

len(x)
#Returns: 4


x = ["Now", "we", "are", "cooking!"]
print(x[0])
print(x[3])

#returns: Now
#cooking!

x = ["Now", "we", "are", "cooking!"]
x[1:3]

#returns: ['we', 'are']


x = ["Now", "we", "are", "cooking!"]
x[:2]
x[2:]

#returns: ['are', 'cooking!']

----------------------------------------------------

Modifying a List

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)
#Returns: ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
#Added kiwi using .append to add it to the list.


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)
#Returns: ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon']
#By using .insert and indicating position 0 for Orange it was inserted in the 0 position.


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)
#Returns: ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Peach']
#There is no 25th position, so it is inserted at the end of the list.


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)
#Returns: ['Orange', 'Pineapple', 'Banana', 'Apple', 'Peach']
#The .remove keyword has removed Melon.


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
print(fruits)
#Returns: ['Orange', 'Pineapple', 'Banana', 'Peach']
# Orange is added at 0 and then .pop(3) has removed "popped out" Apple from the 3rd position.


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)
#Returns: ['Orange', 'Pineapple', 'Strawberry', 'Peach']

--------------------------------------------------------------

Lists and Tupels
#Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. 
#They’re specified using parentheses instead of square brackets.


def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
type(result)
#Returns:  <class 'tuple'>


def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(result)
#Returns: (1, 23, 20)


def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
hours, minutes, seconds = result
print(hours, minutes, seconds)
#Returns: 1 23 20

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
#Returns: 0 16 40


def file_size(file_info):
	name, type, size = file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

------------------------------------

 Iterating over lists and tuples


animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
#Returns: Total characters: 22, Average length: 5.5

 ##The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

#Returns: 1 - Ashley
#	  2 - Dylan
#	  3 - Reese
#The enumerate function will number each item in the sequence and return a tupel for each.



def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

#Returns: ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']

----------------------------------------------------------

##Using the enumerate function:


Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is in an even position or an odd position.

def skip_elements(elements):
	return [element for index, element in enumerate(elements) if index % 2 == 0]


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) #Returns ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) #Returns ['Orange', 'Strawberry', 'Peach']


---------------------------------------------------------
Iterating over Lists
LIST COMPREHENSION

##Here using a For Loop:
multiples = []
for x in range(1,11):
  multiples.append(x*7)
print(multiples)
#Returns  [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

##Easier way using list comprehension in one line of code:
multiples = [x*7 for x in range(1,11)]
print(multiples)
#Returns  [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]


languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
#Returns  [6, 4, 4, 2, 4, 1]



z = [x for x in range(0,101) if x % 3 == 0]
print(z)
#Returns  [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]



----------------------------------------

LOOP VS LIST COMPREHENSION

### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])
#List comprehension result:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)
#Long form code result:
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

-----------------------------------------

List comprehension with conditional statement
You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the list comprehension. For example, [ x for x in range(1,101) if x % 10 == 0 ] generates a new list containing all the integers divisible by 10 from 1 to 100. The if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, the number is added to a new list.

print("List comprehension result:")
print([ x for x in range(1,101) if x % 10 == 0 ])
#List comprehension result:
#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



# The list comprehension above accomplishes the same result as# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)
#Long form code result:  
#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


-------------------------------------------------
Squaring

def squares(start, end):
    return [i**2 for i in range(start, end+1)]


print(squares(2, 3))    # Should print [4, 9]
print(squares(1, 5))    # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))   # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

_____________________________________________________

Common sequence operations
Lists and tuples are both sequences and they share a number of sequence operations. The following common sequence operations are used by both lists and tuples:

len(sequence) - Returns the length of the sequence.

for element in sequence - Iterates over each element in the sequence.

if element in sequence - Checks whether the element is part of the sequence.

sequence[x] - Accesses the element at index [x] of the sequence, starting at zero

sequence[x:y] - Accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default.

for index, element in enumerate(sequence) - Iterates over both the indices and the elements in the sequence at the same time.

List-specific operations and methods
One major difference between lists and tuples is that lists are mutable (changeable) and tuples are immutable (not changeable). There are a few operations and methods that are specific to changing data within lists:

list[index] = x - Replaces the element at index [n] with x.

list.append(x) - Appends x to the end of the list.

list.insert(index, x) - Inserts x at index position [index].

list.pop(index) - Returns the element at [index] and removes it from the list. If [index] position is not in the list, the last element in the list is returned and removed.

list.remove(x) - Removes the first occurrence of x in the list.

list.sort() - Sorts the items in the list.

list.reverse() - Reverses the order of items of the list.

list.clear() - Deletes all items in the list.

list.copy() - Creates a copy of the list.

list.extend(other_list) - Appends all the elements of other_list at the end of list

map(function, iterable) - Applies a given function to each item of an iterable (such as a list) and returns a map object with the results

zip(*iterables) - Takes in iterables as arguments and returns an iterator that generates tuples, where the i-th tuple contains the i-th element from each of the argument iterables.

Tuple use cases
Remember, there are a number of cases where using a tuple might be more suitable than other data types:

Protecting data: Because tuples are immutable, they can be used in situations where you want to ensure the data you have cannot be changed. This can be particularly helpful when dealing with sensitive or important information that should remain constant throughout the execution of a program.

Hashable keys: Because they're immutable, tuples can be used as keys on dictionaries, which can be useful for complex keys.

Efficiency: Tuples are generally more memory-efficient than lists, making them advantageous when dealing with large datasets.

The tuple() operator
The tuple() operator is used to convert an iterable (like a list, string, or set) into a tuple.

Example:

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple, 
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)


Tuples with mutable objects
Although tuples themselves are immutable, they can contain mutable objects, such as lists. This means that although the tuple cannot be modified (for example, you can't add or remove elements), the mutable elements within the tuple can be changed. Example:

# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])


Returning multiple values from functions
One of the most useful aspects of tuples in Python is their ability to return multiple values from a function. This allows a function to produce more than one result, providing flexibility and improving code readability.

Here's an example:

def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)

In the above function, the four arithmetic calculations are returned as a tuple, which can be assigned to a single variable (result), or "unpacked" into multiple variables:

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8

This is a powerful feature that makes Python functions extremely versatile.
___________________________________________________________________________________________-

List comprehensions
A list comprehension is an efficient method for creating a new list from a sequence or a range in a single line of code. It is a best practice to add descriptive comments about any list comprehensions used in your code, as their purpose can be difficult to interpret by other coders.

[expression for variable in sequence] - Creates a new list based on the given sequence. Each element in the new list is the result of the given expression.

Example: my_list = [ x*2 for x in range(1,11) ]

[expression for variable in sequence if condition] - Creates a new list based on a specified sequence. Each element is the result of the given expression; elements are added only if the specified condition is true. 

 Example: my_list = [ x for x in range(1,101) if x % 10 == 0 ] 

Note that tuples do not have comprehensions but a similar functionality can be achieved with: 

tuple(i for i in (1, 2, 3))

When to use for loops or list comprehensions
In Python, list comprehensions are generally used for creating new lists from existing ones in a concise and readable manner, especially when the task involves simple transformations or filtering of elements. 

for loops are more versatile and are preferred when the operation is more complex, requires multiple lines of code, involves statements other than expression (like print, pass, continue, break), or when you need to iterate over a list without creating a new one.

CODING SKILLS

Use a for loop to modify elements of a list.
Use the list.append(old,new) method.
Use the string.endswith() and string.replace() methods to modify the elements within a list.

# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The variable "updated_years" is initialized as a list data type 
# using empty square brackets []. This list will hold the new list
# with the updated years. 
updated_years = []
# The for loop checks each "year" element in the list "years".
for year in years:
    # The if-statement checks if the "year" element ends with the 
    # substring "2023". 
    if year.endswith("2023"):
        # If True, then a temporary variable "new" will hold the 
        # modified "year" element where the "2023" substring is 
        # replaced with the substring "2024".
        new = year.replace("2023","2024")
        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
    # If False, the original "year" element will be appended to the 
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

_______________________________________________________________________

SKILL2

Use a List Comprehension to return values:

# This list comprehension creates a list of squared numbers (n*n). It
# accepts two integer variables through the function’s parameters.
def squares(start, end):
    # The list comprehension calculates the square of a variable integer 
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n*n for n in range(start,end+1)] 

print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

____________________________________________________________________________
SKILL3

Use a list comprehension to modify elements of a list.
Use the string.replace() method within a list comprehension.
Use the string[index] method within a list comprehension.

# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block. 

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

________________________________________________________________________________




Skill Group 4
Use the string.split() method to separate a string into a list of individual words.
Iterate over the new list using a for loop.
Modify each element in the list by slicing the element’s string at a given [1:] index position and appending the substring to the end of the element.
Convert a list back into a string.

# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the 
# element and adds a dash between the element and the moved character. 
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

    # Initialize "new_string" as a string data type by using empty quotes.`
    new_string = ""

   # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:
        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items: 
        # + Each list "element" (starting at index position [1:]), 
        # + a dash "-", 
        # + append the first character of the "element" (using the index 
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-" + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string

print(change_string("1one 2two 3three 4four 5five")) # Should print "one-1 two-2 three-3 four-4 five-5" 



 __________________________________________________________________________________
 
 
Skill Group 5
Use the string.join() method to concatenate a string that provides a list name and its elements.


# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1, 
# element2, element3". 
def list_elements(list_name, elements):
    # This task can be completed in a single line of code. The 
    # concatenation of strings, "list_name", and the list "elements" can
    # occur on the return line. In this case, the string "The " is added 
    # to the "list_name", plus the string " list includes: ", then the
    # "elements" are joined using a comma to separate each element of the 
    # list.
    return "The " + list_name + " list includes: " + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"

_____________________________________________________________________


Skill Group 6

Use map() and convert the map object to a list so we can print all the results at once.

# A simple function to add 1 to a given number
def add_one(number):
    return number + 1

# A list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = map(add_one, numbers)

# Convert the map object to a list to print the result
print(list(result))

# Outputs: [2, 3, 4, 5, 6]
____________________________________________________________________

Skill Group 7
Use zip() to combine a list of names and ages into a list of tuples, and print all the tuples at once.

# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip to combine the lists
combined = zip(names, ages)

# Convert the zip object to a list to print the result
print(list(combined))

# Outputs: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

________________________________________________________________________




























