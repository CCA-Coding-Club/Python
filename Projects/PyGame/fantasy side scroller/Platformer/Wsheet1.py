'''
Section 1: Data Types

Overview
Python offers several fundamental data types:
int - Integer numbers (e.g., 5, -3, 42) 1


float - Decimal numbers (e.g., 3.14, -0.001) 2
str - Strings (e.g., "hello", 'Python') 3
bool - Boolean values (True or False) 4

Questions 1
1.Why is it important to know the data type of a variable?
It's crucial because the data type determines the operations you can perform on a value. 
For example, you can't perform math operations on a string.
2.What happens if you try to perform mathematical operations on incompatible data types?
Python will raise a TypeError because the operation is not supported between those data types.



# Practice 1


#Write the type of each value:

12: int
12.0: float
'12': str
True: bool
False: bool


#Identify the data type of the following variables:

x = 5: int
y = 'hello': str
z = 2.5: float
is_valid = False: bool

'''
'''
#Change the value of x from an int to a float and print its new type. Python

x = 5
x = int(x)
print(type(x))

'''
'''
Questions 1

1.Why is it important to know the data type of a variable?
It's crucial because the data type determines the operations you can perform on a value. 
For example, you can't perform math operations on a string.

2.What happens if you try to perform mathematical operations on incompatible data types?
Python will raise a TypeError because the operation is not supported between those data types.

'''
'''
*********************
Section 2: Variables
*********************

=>Overview
    Variables are names that store data values. Python is dynamically typed, meaning you don't need 
    to declare a variable's type explicitly; Python infers it for you. Variable names must start with
    a letter or an underscore and cannot be Python keywords.
'''
#=>Practice 2

#1.Create variables for your age, your favorite color, and whether you like pizza (use a boolean value).
'''
my_age = 30
favorite_color = "Blue"
likes_pizza = True
print(my_age)
'''
    

#2.Assign a string value to a variable named city, then update it to a new value and print both.
'''
city = "New York"
print("Original city:", city)
city = "Los Angeles"
print("Updated city:", city)
'''
'''
Questions 2

1.What happens if you assign the same variable name to a new value?
The old value is overwritten and replaced by the new one.
How does Python handle variable reassignment?
Python handles reassignment by simply replacing the old value with the new one.

2.Is it possible to use numbers in variable names? If so, how?
Yes, but the number cannot be the first character of the variable name. For example, variable1 is valid, 
but 1variable is not.
'''
'''
************************
Section 3: Boolean Logic
************************

=>Overview
    Boolean logic involves True and False values, which are essential for decision-making8. 
    The keywords are case-sensitive9. 
    The common logical operators are:

    and: Returns True if both statements are True10.

    or: Returns True if at least one statement is True11.

    not: Negates the value12.
'''

#=>Practice 3
'''
#1.Evaluate the following expressions:
True and False: False
not False: True
True or False: True
(3 > 2) and (5 < 10): True
(3 == 4) or (1 != 2): True
'''

#2.Write a statement that checks if a number is both positive and even.
'''
number = -10
is_positive_and_even = (number > 0) and (number % 2 == 0)
print(is_positive_and_even)
'''

'''
#3.What does not True return?
not True returns False.

Questions 3

1.How does boolean logic help in programming?
It's the foundation of conditional statements, allowing programs to make decisions by evaluating conditions 
as either True or False.

2.Write an example where you would use or in a real-world situation.
You could use it to check if a person is a student or a senior to qualify for a discount.
'''
'''
***********************
Section 4: Conditionals
***********************

=>Overview
    Conditionals allow your program to make decisions using
    if, elif, and else statements.

    if: The main condition.
    elif: An "else if" for additional conditions.
    else: The "catch-all" block for when no other conditions are met.
'''

#=>Practice 4

#1.Write a program that checks if a person is old enough to vote (age >= 18) and prints an appropriate message.
'''
age = 20
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

'''

#2.Write a program that checks if a number is negative, zero, or positive and prints the result.
'''
number = -5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

'''

'''
#3.Given a variable score, print "Excellent" if the score is over 90, "Good" if it's between 70 and 90, and 
"Needs Improvement" otherwise.
Python
'''
'''
score = int(input("Please enter your score: "))

if score > 90:
    print("Excellent")
elif score >= 70 and score <= 90:
    print("Good")
else:
    print("Needs Improvement")

'''
'''
Questions 4

1.What happens if multiple elif conditions are true?
Only the code block for the first if or elif condition that evaluates to True will be executed. 
The rest are ignored.

2.How does Python decide which else block to execute?
The else block is executed only if all preceding if and elif conditions evaluate to False.
'''
'''
************************
Section 5: String Basics
************************

=>Overview
 Strings are sequences of characters enclosed in single or double quotes14. Common operations include:
 
 Concatenation (+) 
 Repetition (*) 
 Accessing characters ([]) 
 Length (len()) 

'''

#=>Practice 5

#1.Create a string variable greeting with the value "Hello, world!". Print its length and first character.
'''
greeting = "Hello, world!"
print("Length:", len(greeting))
print("First character:", greeting[0])
'''

#2.Concatenate two strings: your first name and last name, separated by a space.
'''
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
'''

#2.Write a program that asks the user for their favorite color and prints "Your favorite color is: [color]".
'''
favorite_color = input("What is your favorite color? ")
print("Your favorite color is: " + favorite_color)
'''
'''
#2.Use slicing to print the first three characters of "Python".

word = "Python"
first_three = word[0:3]
print(first_three)
'''

'''
Questions 5

1.What happens if you try to access an index that doesn't exist in a string?
Python will raise an IndexError.

2.How can you convert an integer to a string?
You can use the built-in str() function, for example, str(123).

*****************
Challenge Section
*****************

Write a program that takes a user's age as input, stores it in a variable, and prints whether the user is 
a child (under 13), teenager (13-17), adult (18-64), or senior (65+).

'''
'''
#age = int(input("Please enter your age: "))
age_str = input("Please enter your age: ")
age = int(age_str)

if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 17:
    print("You are a teenager.")
elif age >= 18 and age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")

'''

'''
Write a program that checks if a string contains the letter 'a' and prints "Found 'a'" or "No 'a' found".
'''
'''
my_string = "banana"
if 'a' in my_string:
    print("Found 'a'")
else:
    print("No 'a' found")

'''
'''
Combine boolean logic and conditionals: Given variables a and b, write a program that prints "Both are positive" 
only if both are positive numbers.
'''
'''
a = 5
b = 10
if a > 0 and b > 0:
    print("Both are positive")

'''
'''
Reflection

1.Which section did you find the most challenging?
Conditionals section.

2.What new concepts did you learn about strings?
use len() to get the length of a string.
'''

