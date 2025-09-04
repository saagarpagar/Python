# Using Built-in Modules in Python
# Example 

import math
from datetime import datetime, timedelta

# Math module examples
def math_examples():
    print("=== Math Module ===")
    print("Pi value:", math.pi)
    print("Euler's number:", math.e)

    print("Square root of 25:", math.sqrt(25))
    print("Factorial of 5:", math.factorial(5))
    print("Sine of 90 degrees:", math.sin(math.radians(90)))
    print("Log base 10 of 1000:", math.log10(1000))
    print("Ceil of 3.2:", math.ceil(3.2))
    print("Floor of 3.8:", math.floor(3.8))
    print()

# Datetime module examples
def datetime_examples():
    print("=== Datetime Module ===")
    now = datetime.now()
    print("Current Date & Time:", now)

    # Show date and time separately
    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%H:%M:%S"))

    # Add or subtract days
    print("Tomorrow:", now + timedelta(days=1))
    print("Yesterday:", now - timedelta(days=1))

    # Custom date
    birthday = datetime(2000, 5, 15)
    print("My Birthday:", birthday.strftime("%d-%m-%Y"))
    print()

# Main program
def main():
    print("Built-in Modules Demo\n")
    math_examples()
    datetime_examples()
    print("Done!")

if __name__ == "__main__":
    main()
