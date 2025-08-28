# Data Structures in Python
# i just covered the main 4 : list, tuple, set, dictionary

# ---------------- LIST ----------------
# list = ordered, changeable, allows duplicates
my_list = [10, 20, 30, 40]
print("List:", my_list)

# add something
my_list.append(50)   # adding at end
print("After append:", my_list)

# remove something
my_list.remove(20)   # removing value
print("After remove:", my_list)

# ---------------- TUPLE ----------------
# tuple = ordered, unchangeable, allows duplicates
my_tuple = (1, 2, 3, 4)
print("\nTuple:", my_tuple)
# can't update tuple so its like fixed data

# ---------------- SET ----------------
# set = unordered, no duplicates
my_set = {1, 2, 2, 3, 4}
print("\nSet:", my_set)  # duplicate 2 gone automatically

# adding to set
my_set.add(5)
print("After add:", my_set)

# ---------------- DICTIONARY ----------------
# dictionary = key : value pairs, like a mini database
my_dict = {"name": "Sagar", "age": 21, "city": "Nashik"}
print("\nDictionary:", my_dict)

# accessing using key
print("Name is:", my_dict["name"])

# updating value
my_dict["age"] = 22
print("After update:", my_dict)
