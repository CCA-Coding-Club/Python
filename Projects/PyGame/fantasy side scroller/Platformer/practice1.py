
"""
This program stores personal information in variables
and then displays it in two different ways.

It includes:
1. A print statement using commas
2. A cleaner version using f-strings
3. A function with a docstring so help() can explain it
"""

# Step 1: Define the function
def show_info():
    """
    Displays personal information in two different ways.

    Variables:
        name (str): Person's name
        age (int): Person's age
        c (str): Person's favorite color
    """
    # Variables
    name = 'Melvin'
    age = 25
    c = 'Blue'  # Favorite color

    # Version 1: Using commas
    print('My name is', name, 'I am', age, 'years old, and my favorite color is', c)

    # Version 2: Using f-strings
    print(f"My name is {name}, I am {age} years old, and my favorite color is {c}.")

# Step 2: Show the docstring using help()
help(show_info)

# Step 3: Add a separator
print("\n--- Now running the function ---\n")

# Step 4: Call the function
show_info()

# Step 5: Pause the program so you can see everything
input("\nPress Enter to exit...")