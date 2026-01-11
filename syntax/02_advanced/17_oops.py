# ========================================================
# PYTHON OOP (Object-Oriented Programming) FULL LESSON
# ========================================================

# ------------------------------
# 1. Defining a Class
# ------------------------------
# A class is like a blueprint for objects.

class Person:
    # class is like a blueprint for objects 
    species = "Human"

    # constructor / initializer
    def __init__(self, name, age):
        # instance varible (unique to each object)
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")

    # Method to check if adult
    def is_adult(self):
        return self.age >= 18
        
# ------------------------------
# 2. Creating Objects
# ------------------------------

# Create two objects from person class
person1 = Person("Kris", 20)
person2 = Person("Alex", 15)

# Accessing attributes
print(person1.name)         # Kris
print(person2.age)          # 15

# Calling methods
person1.greet()             # Hello, my name is Kris, I am 20 years old.
print("Is person2 adult?", person2.is_adult())        # False

# Accessing class variable
print("Species: ", Person.species)

# ------------------------------
# 3. Updating Attributes
# ------------------------------

person2.age = 18
print("Updated age of person2: ", person2.age)

# ------------------------------
# 4. Inheritance
# ------------------------------
# A child class can reuse code from a parent class

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)                # Call parent constructor
        self.grade = grade

    # Overriding greet method
    def greet(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, in grade {self.grade}.")

# Create a Student object
student1 = Student("Sam", 16, 10)
student1.greet()                  # Overridden method
print("Species: ", student1.species)

# ------------------------------
# 5. Encapsulation (Access Modifiers)
# ------------------------------

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner                   # public
        self._balance = balance              # protected (convention: single _)
        self.__pin = 1234                    # private (name mangling)

    # public method to show balance
    def show_balance(self):
        print(f"{self.owner}'s balance is {self._balance}")

    # private method (cannot be called outside easily)
    def __show_pin(self):
        print(f"PIN is {self.__pin}")

    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin

account = BankAccount("Kris", 50000)
account.show_balance()         # 50000
# account.__show_pin()         # Error: private method
account.verify_pin(123)

# ------------------------------
# 6. Polymorphism Example
# ------------------------------

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow")

# Both objects have speak() but behave diferently
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()

# ------------------------------
# 7. Special / Dunder Methods
# ------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # string represantation
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    # Length representation
    def __len__(self):
        return len(self.title)
    
book1 = Book("Python 101", "Kris")
print(book1)
print("Length of title: ", len(book1))           # __len__ called

# ========================================================
# PYTHON OOP — TEST FILE
# ========================================================
# RULES:
# 1. Write code only where instructed.
# 2. Do not modify questions.
# 3. Do not add extra prints unless asked.
# 4. All answers must be executable.
# ========================================================

# --------------------------------------------------------
# Q1. Class & Object Basics 1
# --------------------------------------------------------
# Create a class named Car
# Attributes: brand (str), year (int)
# Method: info() → prints "Brand: <brand>, Year: <year>"

# WRITE CODE BELOW

# class car
class Car:
    # constructor / initializer
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    # Instance method
    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

# creating objects
car1 = Car("Toyota", 1984)

# calling methods
car1.info()

# --------------------------------------------------------
# Q2. Constructor & Instance Variables
# --------------------------------------------------------
# Create a class User
# Constructor takes: username, email
# Store them as instance variables
# Create ONE object and print both attributes

# WRITE CODE BELOW

# class user
class User:
    # constructor / initializer
    def __init__(self, username, email):
        # instance variable
        self.username = username
        self.email = email

# object user1
user1 = User("Krish7dx9", "sharmakriss985@gmail.com")
print(f"Username: {user1.username}, Email: {user1.email}")

# --------------------------------------------------------
# Q3. Class Variable vs Instance Variable
# --------------------------------------------------------
# Create a class Employee
# Class variable: company = "Google"
# Instance variables: name, salary
# Create TWO employees and print:
# name, salary, company (for both)

# WRITE CODE BELOW

# class Employee
class Employee:
    # class variable
    company = "Google"

    # constructor / initializer
    def __init__(self, name, salary):
        # instance varible
        self.name = name
        self.salary = salary
        
# object employee1
employee1 = Employee("Kris", 15000)
print(f"Company: {Employee.company}, Name: {employee1.name}, Salary: {employee1.salary}")

# object employee2
employee2 = Employee("Manav", 20000)
print(f"Company: {Employee.company}, Name: {employee2.name}, Salary: {employee2.salary}")

# --------------------------------------------------------
# Q4. Method Returning Value
# --------------------------------------------------------
# Create a class Rectangle
# Attributes: length, breadth
# Method: area() → returns area
# Print the returned value

# WRITE CODE BELOW

class Rectangle:
    # constructor / initializer
    def __init__(self, length, breadth):
        # instance variable
        self.length = length
        self.breadth = breadth

    # method area
    def area(self):
        return self.length * self.breadth

# object rectangle1 
rectangle1 = Rectangle(5, 10)

# calling method 
print(rectangle1.area())

# --------------------------------------------------------
# Q5. Inheritance
# --------------------------------------------------------
# Create a parent class Animal
# Method: speak() → prints "Animal speaks"
#
# Create child class DogPoly
# Override speak() → prints "Dog barks"
#
# Create DogPoly object and call speak()

# WRITE CODE BELOW

# parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# child class
class DogPoly(Animal):
    def speak(self):
        print("Dog barks")                     # override speak()

dog1 = DogPoly()
dog1.speak()                                  # method calling  

# --------------------------------------------------------
# Q6. Using super()
# --------------------------------------------------------
# Create class PersonBase
# Constructor: name, age
#
# Create class StudentDerived inheriting PersonBase
# Additional attribute: grade
# Use super() to initialize name and age
# Create object and print all attributes

# WRITE CODE BELOW

class PersonBase:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class StudentDerived(PersonBase):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

student1 = StudentDerived("Kris", 19, 4)
print(student1.name, student1.age, student1.grade)

# --------------------------------------------------------
# Q7. Encapsulation
# --------------------------------------------------------
# Create class BankAccountEncap
# Public variable: owner
# Protected variable: _balance
# Private variable: __pin
#
# Constructor initializes all
# Create method get_balance() → returns balance
#
# Create object and print balance using method ONLY

class BankAccountEncap:
    def __init__(self, owner, balance, pin):          
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def  get_balance(self):
        return self._balance

# object    
bankaccount1 = BankAccountEncap("Kris", 15000, 2609)

# method calling
print(bankaccount1.get_balance())

# --------------------------------------------------------
# Q8. Polymorphism
# --------------------------------------------------------
# Create two classes:
# CatPoly → method sound() prints "Meow"
# CowPoly → method sound() prints "Moo"
#
# Store objects in a list
# Loop and call sound() on each

# WRITE CODE BELOW

class CatPoly:
    def sound(self):
        print("Meow")

class CowPoly:
    def sound(self):
        print("Moo")

# storing class in a list
animals = [CatPoly(), CowPoly()]

for animal in animals:
    animal.sound()

# --------------------------------------------------------
# Q9. Dunder Method __str__
# --------------------------------------------------------
# Create class Laptop
# Attributes: brand, price
# Implement __str__ to return:
# "Laptop <brand> costs <price>"
#
# Print the object directly

# WRITE CODE BELOW

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"Laptop {self.brand} costs {self.price}"
    
laptop1 = Laptop("hp", 15000)
print(laptop1)

# --------------------------------------------------------
# Q10. Logic Test 
# --------------------------------------------------------
# Create class Counter
# Attribute: count (starts at 0)
# Method increment() → increases count by 1
# Method reset() → sets count to 0
#
# Increment 3 times, print count
# Reset, print count

# WRITE CODE BELOW

class Counter:
    def __init__(self):
        self.count = 0                        # starts at 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

counter1 = Counter()
counter1.increment()
counter1.increment()
counter1.increment()
print(counter1.count)                         # prints 3

counter1.reset()
print(counter1.count)                         # prints 0

# ============================================================
# PYTHON OOPS — TEST 2
# ============================================================

# Q1
# What is a class in Python? (one sentence)
# A class is a blueprint that defines the structure and behavior of objects.

# Q2
# What is an object? (one sentence)
# An object is an instance of a class that exists in memory.

# Q3
# What does the __init__ method do?
# It initializes the object's attributes when a new object is created.

# Q4
# What is the purpose of self?
# self refers to the current object and is used to access its attributes and methods.

# Q5
# What will this code print?
class A:
    def __init__(self, x):
        self.x = x

a1 = A(10)
a2 = A(20)

print(a1.x, a2.x)
# Output:
# 10 20

# Q6
# Write a class Car with:
# - attributes: brand, year
# - method: info() that returns "Brand: <brand>, Year: <year>"
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

# Q7
# Create two Car objects and call info() on both
c1 = Car("Toyota", 2020)
c2 = Car("BMW", 2023)

print(c1.info())
print(c2.info())