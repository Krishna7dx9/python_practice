# ------------------------------------------------------------
# OOP BASICS – Classes, Objects, Constructors, Methods
# ------------------------------------------------------------

# 1. Defining a Class
# A class is a blueprint for creating objects.

class student:

    # --------------------------------------------------------
    # 2. Constructor (__init__)
    # Runs automatically when an object is created.
    # 'self' refers to the current object instance.
    # --------------------------------------------------------

    def __init__(self, name, age, branch):
        self.name = name                      # attribute
        self.age = age                        # attribute
        self.branch = branch                  # attribute

    # --------------------------------------------------------
    # 3. Instance Method
    # Methods always take 'self' as first argument.
    # --------------------------------------------------------

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Branch: ", self.branch)

    # Example: method performing some operation
    def is_adult(self):
            return self.age >= 18
        
# ------------------------------------------------------------
# 4. Creating Objects (Instances)
# ------------------------------------------------------------

s1 = student("Kris", 20, "CSE")
s2 = student('John', 17, "CSE")

# ------------------------------------------------------------
# 5. Calling Methods
# ------------------------------------------------------------

# student 1 info
s1.display_info()
print("Is adult: ", s1.is_adult())

# student 2 info
s2.display_info()
print("Is adult: ", s2.is_adult())

# ------------------------------------------------------------
# 6. Updating Object Attributes
# ------------------------------------------------------------





