'''
Description:
    This script is my personal practice file for revising and
    showcasing the most important core Python concepts in one place.
    Each section includes simple but meaningful examples, so I (or anyone)
    can quickly recall Python basics.
'''

# ------------------------------------------
# 1️⃣ VARIABLES & DATA TYPES
# ------------------------------------------
print("\n--- VARIABLES & DATA TYPES ---")

# Example 1: Different data types
name = "Sagar"
age = 22
height = 5.9
is_student = True
print(f"My name is {name}, I am {age} years old, height: {height}ft, Student: {is_student}")

# Example 2: Type checking
print(type(name), type(age), type(height), type(is_student))

# ------------------------------------------
# 2️⃣ IF-ELSE CONDITIONS
# ------------------------------------------
print("\n--- IF-ELSE CONDITIONS ---")

# Example 1: Simple if-else
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: Multiple conditions
marks = 75
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 50:
    print("Grade: B")
else:
    print("Grade: C or Fail")

# ------------------------------------------
# 3️⃣ LOOPS
# ------------------------------------------
print("\n--- LOOPS ---")

# Example 1: For loop
for i in range(1, 6):
    print(f"For loop count: {i}")

# Example 2: While loop
count = 1
while count <= 3:
    print(f"While loop count: {count}")
    count += 1

# ------------------------------------------
# 4️⃣ FUNCTIONS
# ------------------------------------------
print("\n--- FUNCTIONS ---")

# Example 1: Function without parameters
def greet():
    print("Hello! Welcome to Python basics.")

greet()

# Example 2: Function with parameters and return value
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(10, 20)
print(f"Sum of 10 and 20 is {sum_result}")

# ------------------------------------------
# 5️⃣ LISTS
# ------------------------------------------
print("\n--- LISTS ---")

# Example 1: Basic operations
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits list:", fruits)
fruits.append("Mango")
print("After adding Mango:", fruits)

# Example 2: Looping through list
for fruit in fruits:
    print(f"I like {fruit}")

# ------------------------------------------
# 6️⃣ SETS
# ------------------------------------------
print("\n--- SETS ---")

# Example 1: Creating and adding
numbers = {1, 2, 3}
numbers.add(2)  # Duplicate ignored
numbers.add(4)
print("Numbers set:", numbers)

# Example 2: Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)

# ------------------------------------------
# 7️⃣ TUPLES
# ------------------------------------------
print("\n--- TUPLES ---")

# Example 1: Basic tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Example 2: Tuple unpacking
x, y = coordinates
print(f"x = {x}, y = {y}")

# ------------------------------------------
# 8️⃣ DICTIONARIES
# ------------------------------------------
print("\n--- DICTIONARIES ---")

# Example 1: Basic dictionary
person = {"name": "Sagar", "age": 22, "city": "Nashik"}
print("Person details:", person)

# Example 2: Accessing and updating
print("Name:", person["name"])
person["age"] = 23
print("Updated details:", person)

# ------------------------------------------
# 9️⃣ IMPORTING MODULES
# ------------------------------------------
print("\n--- IMPORTING MODULES ---")

# Example 1: Using math module
import math
print("Square root of 16:", math.sqrt(16))

# Example 2: Using datetime module
import datetime
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# ------------------------------------------
# 🔟 EXTRA: LIST COMPREHENSION & F-STRINGS
# ------------------------------------------
print("\n--- EXTRA TOPICS ---")

# Example 1: List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Example 2: f-strings for formatting
name = "Python"
version = 3.11
print(f"I am learning {name} version {version}")

# ------------------------------------------
# ✅ END OF SCRIPT
# ------------------------------------------
print("\nAll core Python topics covered! ✅")
