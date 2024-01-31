Study Guide: Strings
This study guide provides a quick-reference summary of what you learned in this lesson and serves as a guide for the upcoming practice quiz. The string readings in this section are great syntax guides to help you on the Strings Practice Quiz.

In the Strings segment, you learned about the parts of a string, string indexing and slicing, creating new strings, string methods and operations, and formatting strings. 


Knowledge
String Operations and Methods
	.format() - String method that can be used to concatenate and format strings. 

	{:.2f} - Within the .format() method, limits a floating point variable to 2 decimal places. The number of decimal places can be customized.

	len(string) - String operation that returns the length of the string.

	string[x] - String operation that accesses the character at index [x] of the string, where indexing starts at zero.

	string[x:y] - String operation that accesses a substring starting at index [x] and ending at index [y-1]. If x is omitted, its value defaults to 0. If y is omitted, the value will default to len(string).

	string.replace(old, new) - String method that returns a new string where all occurrences of an old substring have been replaced by a new substring.

	string.lower() - String method that returns a copy of the string with all lowercase characters.

    

CODING SKILLS 1

	Use a for loop to iterate through each letter of a string.
	Add a character to the front of a string.	
	Add a character to the end of a string.

#Use the .lower() string method to convert the case (uppercase/lowercase) of the letters within a string variable. This method is often used to eliminate cases as a factor when comparing two strings. For example, all lowercase “cat” is not equal to “Cat” because “Cat” contains an uppercase letter. To be able to compare the two strings to see if they are the same word, you can use the .lower() string method to remove capitalization as a factor in the string comparison.


# This function accepts a given string and checks each character of 
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
	def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty 
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backward

  

Skill Group 2

Use the format() method, with {} placeholders for variable data, to create a new string.
Use a formatting expression, like {:.2f}, to format a float variable and configure the number of decimal places to display for the float. 


# This function converts measurement equivalents. Output is formatted 
# as, "x ounces equals y pounds", with y limited to 2 decimal places. 
	def convert_weight(ounces):

    # Conversion formula: 1 pound = 16 ounces
    	pounds = ounces/16 
    
    # The result is composed using the .format() method. There are two
    # placeholders in the string: the first is for the "ounces" 
    # variable and the second is for the "pounds" variable. The second



Skill Group 3  

Within the format() parameters, select characters at specific index [ ] positions from a variable string.  
Use the format() method, with {} placeholders for variable data, to create a new string.

# This function generates a username using the first 3 letters of a
# user’s last name plus their birth year. 
	def username(last_name, birth_year):
    
    # The .format() method will use the first 3 letters at index 
    # positions [0,1,2] of the "last_name" variable for the first
    # {} placeholder. The second {} placeholder concatenates the user’s
    #  "birth_year" to that string to form a new string username.
    	return("{}{}".format(last_name[0:3],birth_year))

	# Returns:
	Iva1985
	Rod2000
	Den1991

Skill Group 4  
Use the .replace() method to replace part of a string.  
Use the len() function to get the number of index positions in a string.

Slice a string at a specific index position.

# This function checks a given schedule entry for an old date and, if 
# found, the function replaces it with a new date. 
	def replace_date(schedule, old_date, new_date):

    # Check if the given "old_date" appears at the end of the given 
    # string variable "schedule". 
    	if schedule.endswith(old_date):

        # If True, the body of the if-block will run. The variable "p" is
        # used to hold the slicing index position. The len() function


String Indexing and Slicing
String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index [-1] would access the last character of the string, and the index [-2] would access the second-to-last character.

You can also access a portion of a string, called a slice or a substring. This allows you to access multiple characters of a string. You can do this by creating a range, using a colon as a separator between the start and end of the range, like [2:5]. 

This range is similar to the range() function we saw previously. It includes the first number, but goes to one less than the last number. For example:

	fruit = "Mangosteen"
	fruit[1:4]
	'ang'

The slice includes the character at index 1, and excludes the character at index 4. You can also easily reference a substring at the start or end of the string by only specifying one end of the range. For example, only giving the end of the range:

	fruit[:5]
	'Mango'

This gave us the characters from the start of the string through index 4, excluding index 5. On the other hand this example gives is the characters including index 5, through the end of the string:

	fruit[5:]
	'steen'

You might have noticed that if you put both of those results together, you get the original string back!

	fruit[:5] + fruit[5:]
	'Mangosteen'


	
Review: Creating new strings



	message = "A kong string with a silly typo"
	message[2] = "l"
		#This will throw an error
		Error on line 2:
    		message[2] = "l"
		TypeError: 'str' object does not support item assignment

	message = "A kong string with a silly typo"
	new_message = message[0:2] + "l" + message[3:]
	print(new_message)

	A long string with a silly typo
---------------------------------------

	message = "This is a new message"
	print(message)
	message = "And another one"
	print(message)

	This is a new message
	And another one
	
------------------------------------

	pets="Cats & Dogs"
	pets.index("&")
	pets.index("C")
	pets.index("Dog")
	pets.index("s")
	3


	pets="Cats & Dogs"
	pets.index("x")
	#This will throw an error

	pets="Cats & Dogs"
	"Dragons" in pets
		False
	"Cats" in pets
		True
----------------------------------

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

----------------------------------


Basic String Methods
In Python, strings are immutable. This means that they can't be modified. So if we wanted to fix a typo in a string, we can't simply modify the wrong character. We would have to create a new string with the typo corrected. We can also assign a new value to the variable holding our string.

If we aren't sure what the index of our typo is, we can use the string method index to locate it and return the index. Let's imagine we have the string "lions tigers and bears" in the variable animals. We can locate the index that contains the letter g using animals.index("g"), which will return the index; in this case 8. We can also use substrings to locate the index where the substring begins. animals.index("bears") would return 17, since that’s the start of the substring. If there’s more than one match for a substring, the index method will return the first match. If we try to locate a substring that doesn't exist in the string, we’ll receive a ValueError explaining that the substring was not found.

21
animals = "lions tigers and bears"
animals.index("g")
12
animals = "lions tigers and bears"
animals.index("bears")
We can avoid a ValueError by first checking if the substring exists in the string. This can be done using the in keyword. We saw this keyword earlier when we covered for loops. In this case, it's a conditional that will be either True or False. If the substring is found in the string, it will be True. If the substring is not found in the string, it will be False. Using our previous variable animals, we can do "horses" in animals to check if the substring "horses" is found in our variable. In this case, it would evaluate to False, since horses aren’t included in our example string. If we did "tigers" in animals, we'd get True, since this substring is contained in our string.

12
animals = "lions tigers and bears"
"horses" in animals
12
animals = "lions tigers and bears"
"tigers" in animals

---------------------------------
The string method lower will return the string with all characters changed to lowercase. The inverse of this is the upper
method, which will return the string all in uppercase. Just like with previous methods, we call these on a string using
dot notation, like "this is a string".upper(). This would return the string "THIS IS A STRING". This can be super handy
when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.


"Mountains".upper()
MOUNTAINS

"Mountains".lower()
mountains


answer = "YES"
if answer.lower() == "yes":
  print("User said yes")
  
 User said yes
 
 -------------------------------
You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods  lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively.

 " yes ".strip()
 yes
" yes ".lstrip()
" yes ".rstrip()


----------------------------------
The method count can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph.

"The number of times e occurs in this string is 4".count("e")

4

---------------------------------
If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.

"Forest".endswith("rest")

True

--------------------------------
The isnumeric method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful!

"Forest".isnumeric()
False

"12345".isnumeric()

True

-------------------------------

int("12345") + int("54321")

66666

------------------------------

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
This is a string joined by spaces


"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
This...is...a...phrase...joined...by...triple...dots


"This is another example".split()

'This', 'is', 'another', 'example'

-----------------------------

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

Hello Manny, your lucky number is 15


name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
 Your lucky number is 15, Manny.
 
 

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

Output:
Reed received 80% on the exam
Paige received 92% on the exam
Jesse received 85% on the exam 
 ---------------------------
 
 price = 7.5
with_tax = price * 1.09
print(price, with_tax)
7.5 8.175

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
Base price: $7.50. With Tax: $8.18
		The formatting expression limits the output to format a float number with two decimal places.
		
A formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. 

-----------------------------

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

  0 F | -17.78 C
 10 F | -12.22 C
 20 F |  -6.67 C
 30 F |  -1.11 C
 40 F |   4.44 C
 50 F |  10.00 C
 60 F |  15.56 C
 70 F |  21.11 C
 80 F |  26.67 C
 90 F |  32.22 C
100 F |  37.78 C

-----------------------------  
String operations


len(string) - Returns the length of the string
print(len("abcde"))            # prints 5


for character in string - Iterates over each character in the string
for c in "abcde":  print(c)    # prints "a", then "b", then "c", etc.


if substring in string - Checks whether the substring is part of the string
print("abc" in "abcde")     # prints True
print("def" in "abcde")     # prints False


string[i] - Accesses the character at index i of the string, starting at zero
print("abcde"[2])           # prints "c"
print("abcde"[-1])          # prints "e"


string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. 
If i is omitted, its value defaults to 0. If j is omitted, 
Python returns everything from i to the end of the string.

print("abcde"[0:2])         # prints "ab"
print("abcde"[2:])          # prints "cde"

-----------------------------
String methods


string.lower() - Returns a copy of the string with all lowercase characters
print("AaBbCcDdEe".lower())             # prints "aabbccddee"
string.upper() - Returns a copy of the string with all uppercase characters
print("AaBbCcDdEe".upper())             # prints "AABBCCDDEE"


string.lstrip() - Returns a copy of the string with the left-side whitespace removed
print("   Hello   ".lstrip())           # prints "Hello   "
string.rstrip() - Returns a copy of the string with the right-side whitespace removed
print("   Hello   ".rstrip())           # prints "   Hello"
string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
print("   Hello   ".strip())            # prints "Hello"


string.count(substring)- Returns the number of times substring is present in the string
test = "How much wood would a woodchuck chuck"
print(test.count("wood"))               # prints 2



string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
print("12345".isnumeric())              # prints True
print("-123.45".isnumeric())            # prints False


string.isalpha() - Returns True if there are only letters in the string. If not, returns False.
print("xyzzy".isalpha())                # prints True

string.split() -Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)
print(test.split())    # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']


string.split(delimiter) - Returns a list of substrings that were separated by whitespace or another string
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))                  # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']


string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
print(test.replace("wood", "plastic"))  # prints "How much plastic would a plasticchuck chuck"


delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter
print("-".join(test.split()))           # prints "How-much-wood-would-a-woodchuck-chuck"

--------------------------------------

Formatting strings reference guide

For example, imagine you are working in a farmer’s market and need to generate receipts for your customers. You need to weigh the items, calculate the total price for each item (weight times the price per pound), and then add sales tax to the subtotal. Your first attempt might look like this:

# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
  fruit, weight, unit_price = item
  subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625  # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)

Subtotal: 27.245 
Sales Tax: 1.8049812500000002 
Total: 29.049981250000002

#We’d much prefer the output to look like a real register receipt:
#Subtotal:     $27.25 
#Sales Tax:    $ 1.80
#Total:        $29.05


The format() method takes a string containing special placeholders, called the format string, and replaces the special placeholder characters {} with the value of the arguments you pass. The arguments are converted to strings if they weren’t already. The number of arguments you pass must exactly match the number of placeholders in the format string:

fruit = "peaches"
weight = 3.0
per_pound = 2.99

output = "You are buying {} pounds of {} at {} per pound.".format(weight, fruit, per_pound)
print(output)
#prints: You are buying 3.0 pounds of peaches at 2.99 per pound.

You can also consume the arguments to format() in any order you want by specifying the index inside the placeholder. As with lists and arrays, the index always starts with 0. You can even use an index more than once. Here you can see we’re using the second argument twice. 

output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)
#prints: Peaches are 2.99 per pound, and you have 3.0 pounds of peaches.

A third option for the placeholders is to use field names instead of indexes. This can make your code much more readable.
output = "{fruit} are {price} per pound, and you have {weight} pounds of {fruit}.".format(weight=weight, fruit=fruit, price=per_pound)
print(output)
#prints: Peaches are 2.99 per pound, and you have 3.0 pounds of peaches.


Python also gives you many options to control the appearance of the output. Remember the messy output from the first example? You can have Python automatically round things up to the nearest penny and produce nice output by using a formatting expression. In the example below, the code tells Python to round up the numbers to two decimal places.

# Print the receipt for the customer. The format string ":10,.2f" 
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))

Subtotal:     $    27.25 
Sales Tax:    $     1.80 
Total:        $    29.05

Everything inside the placeholder after the “:” colon is part of the formatting expression. The expression “:10,.2f” means “make the output 10 characters wide, use digit separators if the amount is over 1000, output no more than 2 digits after the decimal, and expect the input to be a floating-point decimal number”. 

The following table gives you some more examples of formatting expressions:
Formatting expressions

Expr			Meaning					Example
{:d}		integer value					"{0:.0f}".format(10.5) → '10'

{:.2f}		floating point with that many decimals	'{:.2f}'.format(0.5) → '0.50'

{:.2s}		string with that many characters		'{:.2s}'.format('Python') → 'Py'

{:<6s}		string aligned to the left that many spaces	'{:<6s}'.format('Py') → 'Py    '

{:>6s}		string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'

{:^6s}		string centered in that many spaces		'{:^6s}'.format('Py') → '  Py  '

Check out the official documentation for all available expressions


Formatted string literals (Optional)
The formatted string literal feature, added in Python 3.6, isn’t used a lot yet. Again, it's included here in case you run into it in the future, but it's not needed for this or any upcoming courses.

A formatted string literal or f-string is a string that starts with 'f' or 'F' before the quotes. These strings might contain {} placeholders using expressions like the ones used for format() method strings.

The important difference between f-strings and the format() method is that f-strings take the value of the variables from the current context, instead of taking the values from parameters.

Examples:

>>> name = "Micah"

>>> print(f'Hello {name}')

Hello Micah

>>> item = "Purple Cup"
>>> amount = 5
>>> price = amount * 3.25

>>> print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')

Item: Purple Cup - Amount: 5 - Price: 16.25

-------------------------------------



  
