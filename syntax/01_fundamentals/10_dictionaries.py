# ============================
# PYTHON DICTIONARIES – FULL SYNTAX
# ============================

# 1. Creating dictionaries

d1 = {
    "name": "Kris",
      "age": 19,
      "city": "Pune"
      }
d2 = dict(a=2, b=2, c=3)       # Using dict constructor
empty_dict = {}


print("d1: ", d1)
print("d2: ", d2)
print("empty_dict: ", empty_dict)

# 2. Accessing values

print("Name: ", d1["name"])                     # using key
print("Age: ", d1.get("age"))                   # safer way, returns none if  key missing
print("Country: ", d1.get("country", "India"))  # default if missing

# 3. Adding & updating

d1["email"] = "kris@example.com"          # add new key
d1["age"] = 20                            # updating existing key
print("Updated d1: ", d1)

# 4. Removing items

d1.pop("city")                     # remove by key
d1.pop("nonexistent", None)        # safer remove, no error
d1.popitem()                       # removes last inserted item (Python 3.7+)
del d1["name"]                     # delete key
# d1.clear                         # uncomment to empty the dictionary
print("After removals: ", d1)

# 5. Dictionary operations

keys = d2.keys()
values = d2.values()
items = d2.items()

print("Keys: ", keys)
print('Values: ', values)
print("Items: ", items)

# 6. Iterating through dictionary

for key in d2:
    print(key, "->", d2[key])

for key, value in d2.items():
    print(f"{key} -> {value}")

# 7. Copying dictionaries

d_copy = d2.copy()
print("Copy of d2: ", d_copy)

# 8. Nested dictionaries

students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}

print("Nested dicts: ", students)
print("Alice's grades: ", students["Alice"]["grade"])

# ============================
# PYTHON DICTIONARIES – TEST
# ============================

# 1. Create a dictionary:
#       {"name": "Kris", "age": 21, "city": "Pune"}
#    Print it.

A = {"name": "Kris", "age": 21, "city": "Pune"}
print("A: ", A)

# 2. Access and print:
#    # name
#    # age
#    # country (default to "India" if not present)

print("name: ", A["name"])
print("age: ", A.get("age"))
print("Country: ", A.get("country", "India"))

# 3. Add key "email" with value "kris@example.com" 
#    Update age to 22
#    Print the dictionary

A["email"] = "kris@example.com"
A["age"] = 22
print("A: ", A)

# 4. Remove:
#    # city using pop
#    # non-existent key safely
#    Print the dictionary

A.pop("city")
A.pop("nonexisting", None)
print("A: ", A)

# 5. Create:
#       d = {"a":1, "b":2, "c":3}
#    # Print all keys
#    # Print all values
#    # Print all items (key-value pairs)

d = {"a":1, "b":2, "c":3}

keys = d.keys()
values = d.values()
items = d.items()

print("Keys: ", keys)
print("Values: ", values)
print("Items: ", items)

# 6. Create nested dictionary:
#       {"Alice": {"age": 20, "grade": "A"}, "Bob": {"age": 22, "grade": "B"}}
#    # Print Alice's grade

X = {"Alice": {"age": 20, "grade": "A"},
     "Bob": {"age": 22, "grade": "B"}}

print("Alice's grade: ", X["Alice"]["grade"])

# 7) Create the dictionary:
#    marks = {"math": 90, "science": 80}
#    Add a new key "english" with value 85. Print the updated dictionary.

marks = {"math": 90, "science": 80}
marks["english"] = 85
print("Marks: ", marks)

# 8) Create:
#    info = {"name": "Kris", "year": 2025, "skills": ["python", "dart"]}
#    Add a new skill "DSA" to the skills list inside the dictionary and print it.

info = {"name": "Kris", "year": 2025, "skills": ["python", "dart"]}
info["skills"].append("DSA")
print("info: ", info)

# 9) Create:
#    prices = {"apple": 100, "banana": 40, "mango": 60}
#    Increase the price of "apple" by 20 and print the updated dictionary.

prices = {"apple": 100, "banana": 40, "mango": 60}
prices["apple"] = 100 + 20
print("Prices: ", prices)

# 10) Create:
#     student = {"name": "Kris", "branch": "CSE", "cgpa": 8.5}
#     Print all keys and all values separately.

student = {"name": "Kris", "branch": "CSE", "cgpa": 8.5}

keys = student.keys()
values = student.values()

print("Keys: ", keys)
print("Values: ", values)

# 11) Create:
#     user = {"name": "Kris", "age": 21}
#     Add key "city" with value "Pune"
#     Update age to 22
#     Print the dictionary

user = {"name": "Kris", "age": 21}
user["city"] = "Pune"
user["age"] = 22
print(user)


# 12) Create:
#     marks = {"math": 80, "science": 90}
#     Remove "math" safely
#     Print the dictionary

marks = {"math": 80, "science": 90}
marks.pop("math", None)
print(marks)

# 13) Create:
#     student = {
#         "Alice": {"age": 20, "grade": "A"},
#         "Bob": {"age": 22, "grade": "B"}
#     }
#     Print Bob's age

student = {
        "Alice": {"age": 20, "grade": "A"},
        "Bob": {"age": 22, "grade": "B"}
    }

print(student["Bob"]["age"])