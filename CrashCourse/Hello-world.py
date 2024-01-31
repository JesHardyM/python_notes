print ("Hello, world.")

You can follow along in the reading as the instructor discusses the code or review the code after watching the video.


	for x in 25:
    	print(x)
#this will produce an error because we have not declared a range and the interpreter will not iterate a single element

#if we need a single element we have to call it as though it were a list using the []
	for x in [25]:
	print(x)

##or call for all of the items inside a certain range in this case 0-24 aka 25 characters
	for x in range(25):
    	print(x)



LOOP FOR GRETTING FRIENDS INDIVIDUALLY
	def greet_friends(friends):
	    for friend in friends:
	        print("Hi " + friend)

	greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

	Hi Taylor
	Hi Luisa
	Hi Jamaal
	Hi Eli

##in this example it is iterating on each character in the string because 
##we did not define the single element Barry as a string by adding [] inside the ().
	def greet_friends(friends):
	    for friend in friends:
        	print("Hi " + friend)

	greet_friends("Barry")

	Hi B
	Hi a
	Hi r
	Hi r
	Hi y

LOOPING OVER A STRING

for Loop
The most direct—and common—way to loop over a string is to use the for loop. Let’s look at an example:

	greeting = ‘Hello’
	for char in greeting:
		print(char)

This loop begins with char = 0, which is the first element in the string. It directly calls the elements of the string and prints each element on a new line, resulting in the output below:

	H	e 	l 	l 	o 

	
	What if you want the position of the string instead?

	for i in range(len(greeting)):
		print(i)

len(greeting) is an integer that tells Python how many characters are in the string. But because it’s an integer, you need to convert it to an iterable sequence by using the range() function. This loop does the same thing as the loop above, but instead of printing elements, it prints integers resulting in the output below:

	0	1	2	3	4



while loop with indexing
This while loop is the more “common” while loop that programmers often use. This type of loop involves an index variable
to represent the current position within the sequence. Most of the time, this will start with 0 for the initial iteration. Let’s take a look at an example:

	greeting= ‘Hello’
	index = 0
	while index < len(greeting):
		print(greeting[index])
		index += 1
 
 The initial index value is 0, and the while loop continues to execute as long as the index variable is less than the
 length of the len(greeting). At each iteration, Python prints the value at the current index position (greeting[index]).
 Then, Python increments the index by 1 (index += 1) to move to the next position. The output of this example is:

	H

	e

	l 

	l 

	o


while loop with slicing
Using a while loop with slicing accomplishes the same thing that a while loop with indexing does—like the example you explored above—this is just another way to write a while loop. You use this while loop in combination with string slicing to iterate over a portion of a sequence. Remember, it’s up to you to choose the method for looping over a string based on your level of comfort. There are multiple ways to write lines of code to execute the same result. Let’s explore how a while loop with slicing results in the same output.

	greeting= ‘Hello’
	index = 0
	while index < len(greeting):
    		print(greeting[index:index+1])
    		index += 1

This while loop continues to run as long as the index variable is less than the length of the string, which is determined
by using len(greeting). With each iteration, a substring of length 1 is extracted using (greeting[index:index+1]) and
printed. Then, the index is incremented by 1 (index += 1) to move to the next position. The output is:

	H

	e

	l 

	l 

	o 



LIST COMPREHENSIONS
  List comprehensions are a concise way to create lists in Python. This example starts with a list of numbers. 
  The second  line of code defines the type of transformation you want to execute on each element in the original list. 
  In this case, you’re using this line of code to create a new list called squared_numbers and apply x ** 2 to square each
   element in the numbers list. The result of each squared element is then printed in a new list:

	Let’s look at an example:

	numbers = [1, 2, 3, 4, 5]
	squared_numbers = [x ** 2 for x in numbers]
	print(squared_numbers)
		[1, 4, 9, 16, 25]


MAP FUNCTION

	numbers=[1, 2, 3, 4, 5] 
	sqrs_of_numbers=map(square, numbers)
 	next(sqrs_of_numbers)                
		1                                         
	next(sqrs_of_numbers)                
		4                                         
	next(sqrs_of_numbers)                
		9                                         
	next(sqrs_of_numbers)                
		16                                        
	next(sqrs_of_numbers)                
		25
		
Map with Built-in Function
 In the following example, a built-in function pow() is given to map two list objects, one for each base and index parameter.
 The result is a list containing the power of each number in bases raised to the corresponding number in the index.
 
	bases=[10, 20, 30, 40, 50]
	index=[1, 2, 3, 4, 5]
	powers=list(map(pow, bases, index))
	powers 
		[10, 400, 27000, 2560000, 312500000]
------------------------------------------------------------------------------------------------		
		

SLICE and JOIN STRINGS

Now it’s time to learn how to extract parts of a string—what we call “slicing” a string—or create a longer string by joining two or more strings together. 

Slicing a string is just like taking a slice out of a homemade apple pie. When it comes to strings, slices can be as small or as big as you want. If you want to put two or more of those slices back together, you join them together end-to-end—in Python speak, you “concatenate” them—to make one bigger, single string.

In this reading, you will learn when to slice and join strings, how to do it, and see some examples along the way.

What is slicing and joining strings?  
When you slice a string, you extract a subset of the original string—sometimes referred to as indexing a string. Joining strings is the process of linking two or more strings together to create a bigger string.

How to slice strings 
Bracket notation, [ ], is used to specify the start of the index, ending index, or both. If you do not include the starting index, then the slice contains everything from the beginning of the string to the ending index. This is the same if you do not include the ending index. Let’s look at a couple of examples:

Pro tip: Remember that the indexes in Python start with 0, and not 1.


	string1 = "Greetings, Earthlings"
	print(string1[0])   # Prints “G”
	print(string1[4:8]) # Prints “ting”
	print(string1[11:]) # Prints “Earthlings”
	print(string1[:5])  # Prints “Greet”


Note: When you specify an ending index, Python slices everything up to, but not including the ending index. Notice in the second example the ending index is 8, but the characters sliced are 4–7.

If your index is negative, Python counts back from the end of the string instead of the beginning.


	print(string1[-10:])     # Prints “Earthlings” again

If your index is beyond the end of the string, Python returns an empty string.

	print(string1[55:])     # Prints “” 

An optional way to slice an index is by the stride argument, indicated by using a double colon. This allows you to skip over the corresponding number of characters in your index, or if you’re using a negative stride, the string prints backwards.

		print(string1[0::2])    # Prints “Getns atlns”
		print(string1[::-1])    # Prints “sgnilhtraE ,sgniteerG”

-----------------------------------
JOIN STRINGS
		
How to join strings 
To join strings in Python, you use the plus operator, + , just as if you were adding two numbers together. The following example joins three strings together.


	print("Hello" + " " + "world") #Prints “Hello world”

You can also use the join() function, which is very useful when you want to concatenate elements from a list of strings with a specific delimiter. In the following example, we have a list of strings called greetings and we join them with a space using .join(greetings). The join() function concatenates all the strings in the list greetings, and places a space between each string.

	greetings = ["Hello", "world"]
	print(" ".join(greetings))  # Prints "Hello world"

You can also concatenate a combination of strings and variables like in the following example.
		name = "Alice"
		print("Hello, " + name + "!")  # Prints "Hello, Alice!"


How to combine slicing and joining strings
Now you know how to slice strings and join strings. Now, let’s put the two operations together by taking an unformatted phone number, 2025551212, and return it as a properly formatted U.S. number. In this example, we’ll use phonenum to refer to the unformatted phone number.


# The first 3 digits are the area code:
  	area_code = "(" + phonenum[:3] + ")"
		This function slices the first three numbers from the list.


# The next 3 digits are called the “exchange”:
  	exchange = phonenum[3:6]
		This function slices the numbers 4–6 from the list.


# The next 3 digits are the line number:
  	line = phonenum[-4:]
 		This negative index function counts backwards from the end of the numbers, 
 		slicing the last four numbers in the list.


# Put the pieces back together into a nicely formatted string:
  	return area_code + " " + exchange + "-" + line
	
	When you’re done, your code will look like this:


	def format_phone(phonenum):
    	area_code = "(" + phonenum[:3] + ")"
    	exchange = phonenum[3:6]
	    line = phonenum[-4:]
	    return area_code + " " + exchange + "-" + line
Finally, we’ll use the print function to join the three previously sliced numbers together in the correct format. With this function definition, when you call print(format_phone("2025551212")), it will print (202) 555-1212. 


	print(format_phone("2025551212")) # Outputs: (202) 555-1212
	
	
	
STUDY GUIDE: for LOOPS

This study guide provides a summary of what you learned in this segment and serves as a guide for the upcoming practice quiz.  

In the for Loops segment, you learned about the logical structure and syntax of for loops. You took a closer look at the range() function. You learned about nested for loops and complex nested for loops with if statements. You also learned how to fix common errors in for loops.

for Loops vs. while Loops
for loops and while loops share several characteristics. Both loops can be used with a variety of data types, both can be nested, and both can be used with the keywords break and continue. However, there are important differences between the two types of loops: 

while loops are used when a segment of code needs to execute repeatedly while a condition is true

for loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence

An important distinction is that for loops are suited for objects that have iterable structures. So lists, strings, ranges of integers. Individual integers are not iterable, but can be looped over by the use of the range() function, which is covered below. While loops do not iterate per se, rather they watch a truth condition 

Syntax 
The syntax of a for loop with the in keyword:


for variable in sequence:
    body of loop

Common for Loop Structures 
	for Loop with range()

The in keyword with the range() function generates a sequence of integer numbers, which can be used with a for loop to configure the iterations of the code. The range of numbers [0, 1, 2] correlates to ordinal index positions (1st, 2nd, 3rd), rather than the cardinal (quantity) values of the numbers 0, 1, and 2. For example, range(5) means the five index positions in the range [0, 1, 2, 3, 4]. 

The range() function can take up to three parameters. The roles of the three possible range(x,y,z) parameters are:

	x = Start - Starting index position of the range 

Default index position is 0.
The starting index position is included in the range.

	Example syntax: range(2, y, z) or range(x+3, y, z) 

	y = Stop - Ending index position of range
	ending has no default index position. Must include the ending index position in the range() parameters.

	Example syntax: range(y)

The value of the ending index position is excluded from the range.
	To include the ending index number, use the expression: y+1 (index + 1)

	Example syntax: range(x, y+1, z)

Alternatively, if y = 10, you can write: range(x, 11, z)

	z = Step - Incremental value

Example of a for loop with the in keyword and the range() function:

# This loop iterates on the value of the "number" variable in a range
# of 1 to 6+1 (the upper range limit of 6 is excluded, so +1 has
# been added to it to include 6 in the range). The incremental value
# for the loop is 2 (number+2). The print() function will output the
# resulting value of "number" multiplied by 3.

for number in range(1, 6+1, 2):
    print(number * 3)

# The loop should print 3, 9, 15
Restablecer

Common pitfalls when using the range() function:
Forgetting that the upper limit of a range() isn’t included in the range.

Iterating over non-sequences. For example, strings are iterable letter by letter, but not word by word. 

Example of a range() function where the value of the upper limit of the range is excluded:


# This loop iterates on the value of the "number" variable in a range
# of 2 to 7 (the upper range limit of 8 is excluded). The print() 
# function will output the resulting value of "number" squared.

for number in range(2,8):
    print(number**2)

# The loop should print 4, 9, 16, 25, 36, 49
Restablecer

Nested for Loops 
The syntax of nested for loops:


for x in sequence:
    # start of the outer loop body
    for y in sequence:
        # start of the inner loop body
        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body

Example of nested for loops:


# This code demonstrates the outer and inner loop iterations of a pair 
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions 
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in ra
Restablecer

for loop with nested if Statement
The syntax of a for Loop with nested if Statement:


for x in sequence:
    # start of body of for loop
    if condition is true:
        # start of body of if-statement
        # end of body of if-statement
    # continue body of for loop
    # end of body of for loop

# As a list comprehension:
[x for x in sequence if condition]

Example of a for Loop with Nested if Statement:


# This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no 
# incremental value is specified in the range() parameters, the default
# increment is +1. 

for x in range(7):
    if x % 2 == 0:
        print(x)

Restablecer

List comprehensions
It is important to know that loops can be avoided sometimes; as you progress, you will develop a sense of when and how to do so. The concepts for loops are similar between other languages, but in Python, list comprehensions provide a concise way to create lists based on existing lists or sequences. 

Here is a concrete example for better understanding. Let's say you have a sequence of numbers and you want to create a new list containing only the even numbers from the sequence.

With a traditional for Loop, you might write:


sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)

With a list comprehension, you could achieve the same result in a more concise way:


sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]

Both of these pieces of code will create a list of even numbers from 0 to 10: [0, 2, 4, 6, 8]. The list comprehension version does this in a single, compact line. These “one-liners” are very useful and dramatically reduce overhead. 

An example of a useful one-liner is:


print("*" * 8)
Restablecer

This prints “*” 8 times. The number can be replaced by an integer variable, and to do this with a loop would be several lines of code and run more slowly.  


Key takeaways


for n in range(6,18+1,3):
  print(n*2)
  
for n in range(19):
    if n % 2 == 0:
        print(n)
        
for x in range(1,11):
  print(x**3)
  
 for i in range(0, 101, 7): 
    print(i)
    
for c in input:
  if c.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(c)
