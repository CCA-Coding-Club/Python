
'''
*******************************
The Python Practice Worksheet 2
*******************************

This worksheet covers core Python concepts including lists, loops, NoneType, errors, stacks, and functions. 
The exercises are designed to be hands-on, encouraging you to write and run code to better understand how each concept works.

1. Lists

A list is an ordered, mutable collection of items. Lists are versatile and can hold different data types.
Accessing elements: You can access items in a list by their numerical index, starting from 0.
Modifying lists: Methods like .append(), .pop(), and .remove() allow you to add, remove, and change items in a list.
Question: What happens if you try to access an index that doesn’t exist in a list?
You will encounter an IndexError. This error occurs when you try to access an index that is outside the bounds of the list.

2. Loops

Loops are used to repeatedly execute a block of code. The two main types are for loops and while loops.
A for loop is used for iterating over a sequence (like a list) or other iterable objects.
A while loop continues to execute as long as a certain condition remains true.
Question: How do you use a loop to process each item in a list?
You can use a for loop to iterate through each item. For example: for item in my_list: print(item).

3. NoneType

None is a special value in Python that represents the absence of a value or a null object.
It is the only value of the NoneType data type.
Functions that don't explicitly return a value will automatically return None.
You should use the is operator to check if a variable is None (e.g., if result is None:), as it's more idiomatic and reliable than ==.
Question: What is NoneType, and how is the value None used in Python?
NoneType is the data type for the value None. None is used to indicate that a variable has no value or that a function does not return anything meaningful. 
It's often used as a placeholder or to signify a failed operation.

4. Errors

An error (or exception) is an event that disrupts the normal flow of a program.
Common errors include IndexError (bad index), ValueError (invalid value), and ZeroDivisionError (division by zero).
Error handling: You can gracefully handle errors using try and except blocks. 
The code in the try block is executed, and if an error occurs, the code in the except block is run instead of crashing the program.
Question: What happens when you encounter an error in your code? How can Python handle errors?
When an unhandled error is encountered, the program crashes and displays an error message called a traceback. 
Python handles errors using try-except blocks. The try block contains the code that might cause an error, and the except block specifies the code to run if a particular error occurs.

5. Stacks

A stack is an abstract data structure that follows the LIFO (Last-In, First-Out) principle.
The last element added to a stack is the first one to be removed.
In Python, you can easily implement a stack using a list.
Push: Adding an element to the top of the stack is done with .append().
Pop: Removing the top element is done with .pop().
Question: How can you add or remove elements in a stack using a list?
You add elements using the .append() method (push) and remove elements using the .pop() method (pop).

6. Function Basics

A function is a reusable block of code that performs a specific task.
You define a function using the def keyword, followed by the function name and parentheses.
Functions can take parameters as input and can return a value.
Calling a function executes its code.
Question: What are the steps to define and use a function in Python?
Define: Use def function_name(parameters): to create the function.
Code block: Write the code the function will execute, indented inside the definition.
Call: Use function_name(arguments) to run the function.

'''
'''
***************************
Challenge Section Solutions
***************************

1. Create a list of numbers and use a loop to print their sum.
Example: nums = [3, 7, 2] total = 0 for n in nums: total += n print(total)
Sum of numbers:
'''
'''
# Sum of numbers entered by the user

nums = []  # Start with an empty list
total = 0

print("Enter the numbers you want to sum. Type 'done' to finish.")

# Loop to ask for numbers
while True:
    user_input = input("Enter a number: ")
    
    # Check if the user wants to stop
    if user_input.lower() == 'done':
        break
    
    # Try to convert the input to a number and add it to the list
    try:
        num = int(user_input)
        nums.append(num)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Loop to sum the numbers in the list
for n in nums:
    total += n
    
# Print the results
print("The numbers you entered are:", nums)
print("The total sum is:", total)

'''
'''
nums = [3, 9, 2]
total = 0
for n in nums:
    total += n
print(total) # Output: 12
'''

'''
2.Even numbers from 1 to 20:
Python
'''
'''

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

'''
'''
3.Loop until 'quit':
Python
'''
'''
while True:
    txt = input("Type something: ")
    if txt == "quit":
        break
'''
'''
4.double_or_none function:
Python
'''
'''
def double_or_none(n):
    if n < 0:
        return None
    return n * 2

print(double_or_none(5))  # Output: 10
print(double_or_none(-3)) # Output: None

'''
'''

5.Handling FileNotFoundError:
Python

'''
'''
try:
    open("nofile.txt")
except FileNotFoundError:
    print("File not found!")

'''
'''
6.Handling ZeroDivisionError:
Python
'''
'''
try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Can't divide by zero!")

'''
'''
7.Stack operations:
Python
'''
'''
#*args are the elements you want to add to the stack.
def stack_operations(*args):
    stack = []
    # Add all elements passed as arguments
    for item in args:
        stack.append(item)
    
    # Remove the last element (simulate pop operation)
    removed_item = stack.pop()
    
    # Show the removed item and the final stack
    print("Removed item:", removed_item)
    print("Final stack:", stack)

# Example usage:
stack_operations(1, 2, 4, 5)

'''
'''
8.Reverse a word with a stack:
Python
'''
'''
def reverse_word(word):
    # Convert the input word into a list of characters (this will act as our stack)
    stack = list(word)
    
    # Create an empty string to store the reversed word
    rev = ""
    
    # Loop while there are still characters in the stack
    while stack:
        # Remove the last character from the stack and add it to rev
        # This is the LIFO behavior of a stack (Last In, First Out)
        rev += stack.pop()
    
    # Print the reversed word
    print(rev)  # Example: if word="python", output will be "nohtyp"
    
    # Return the reversed word in case it needs to be used later
    return rev

# Example usage:
reverse_word("python")  # Output: nohtyp
reverse_word("hello")   # Output: olleh

'''
'''
9.greet_user function:
Python
'''
'''
def greet_user(name):
    print("Hello,", name + "!")
greet_user("Sam")
greet_user("Alex")
greet_user("Taylor")
'''
'''
10.Simple calculator:
Python
'''

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Can't divide by zero!")


print(add(3, 2))  # Output: 5
print(div(3, 1))  # This will cause a ZeroDivisionError unless handled in a try-except block.


