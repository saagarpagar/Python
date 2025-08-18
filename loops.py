"""
My Python Practice - Loops and Iterations
-----------------------------------------

This file is just my practice for loops in Python.
Trying to understand for, while, break, continue, pass and nested loops.
"""

# Example 1: for loop (print 1 to 5)
print("For Loop Example")
for i in range(1, 6):
    print("Number:", i)

print()  # just space


# Example 2: while loop (count till 5)
print("While Loop Example")
count = 1
while count <= 5:
    print("Counting:", count)
    count += 1

print()


# Example 3: break (stop loop when number is 5)
print("Break Example")
for num in range(1, 10):
    if num == 5:
        print("Stopped at 5")
        break
    print("Number:", num)

print()


# Example 4: continue (skip number 3)
print("Continue Example")
for num in range(1, 6):
    if num == 3:
        print("Skipped 3")
        continue
    print("Number:", num)

print()


# Example 5: pass (just a placeholder, does nothing)
print("Pass Example")
for num in range(1, 4):
    if num == 2:
        pass
    print("Number:", num)

print()


# Example 6: nested loop (loop inside loop)
print("Nested Loop Example")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")
