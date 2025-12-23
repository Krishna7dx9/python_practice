# ============================================================
# Problem 1 : Create 5 variables of different types
# ============================================================

var1 = "kris"
var2 = 52
var3 = True
var4 = 52.63
var5 = [1, 63, 4, 2, 5, 4]

print(var3)
print(var4)

# ============================================================
# Problem 2 : Reassign TWO variables to NEW types
# ============================================================

var3 = 45          # bool -> int
var4 = 52          # float -> int

print(var3)
print(var4)

# ============================================================
# Problem 3 : Two good variable names + two garbage names
# ============================================================

good_name1 = "krishna"
good_name2 = "krishna sharma"

x = "kris"
y = 45

# ============================================================
# Problem 4 : Print all variables clearly
# ============================================================

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(good_name1)
print(good_name2)
print(x)
print(y)

# ============================================================
# Problem 5
# ============================================================

city = "Ahmedabad"
pincode = 314022
height = 5.7
is_coder = True
favorite_foods = ["dosa", "idli", "vada pav"]
colors = ("red", "blue")

# ============================================================
# Problem 6
# ============================================================

snake_case_variable = 45
badname = 45
PI = 3.14
numbers_list = [2, 2, 3, 5, 4]

# ============================================================
# Problem 7
# ============================================================

var_a = 4
var_a = str(var_a)

var_b = "hello"
print(var_b)
var_b = 3.14

var_c = [1, 2, 3]
print(var_c)
var_c = True

# ============================================================
# Problem 8
# ============================================================

a1, a2, a3, a4, a5 = 1, 2, 3, 4, 5
print(a1, a2, a3, a4, a5)

# ============================================================
# Problem 9
# ============================================================

name = "kris"
age = 45
is_student = False

age = str(age)
name = name.upper()

print(name, age, is_student)

# ============================================================
# Problem 10
# ============================================================

full_name = "Krishna Sharma"
print(full_name[0])
print(full_name[-1])
print(len(full_name))

# ============================================================
# Problem 11
# ============================================================

fav_movie = "Batman"
birth_year = 2005
weight = 54.06
skills = ["Flutter", "Python", "DSA", "LLD"]
countries = ("Dubai", "Hong Kong", "USA")

# ============================================================
# Problem 12
# ============================================================

num = 45
num = float(num)

flag = True
flag = int(flag)

text = "Kris"
text = list(text)

# ============================================================
# Problem 13
# ============================================================

x1, x2, x3, x4, x5 = 1, 2, 3, 4, 5
print(f"{x1}, {x2}, {x3}, {x4}, {x5}")

# ============================================================
# Problem 14
# ============================================================

total_price = 5420
bad = 2
VERSION = 2.3
random_floats = [2.3, 20.1, 3.2]

# ============================================================
# Problem 15
# ============================================================

sentence = "Hey, I am Krishna Sharma, Learning Python."

print(sentence[:5])
print(sentence[-3:])
print(sentence.count(" "))

# ============================================================
# Problem 16
# ============================================================

favorite_sport = "football"
trophies = 2
gpa = 7.6
learning_python = True
dream_companies = ["Google", "Oracle", "Amazon", "Microsoft"]

# ============================================================
# Problem 17
# ============================================================

trophies = bool(trophies)
gpa = int(gpa)
favorite_sport = favorite_sport.upper()

print(trophies, gpa, favorite_sport)

# ============================================================
# Problem 18
# ============================================================

v1 = 1
v2 = 1.1
v3 = True
v4 = [1, 2]
v5 = (1, 2)

print(v1, v2, v3, v4, v5)

# ============================================================
# Problem 19
# ============================================================

sentence = "Hey bro What's up there!"
print(len(sentence))
print(sentence.count(" "))
print(sentence[:3])
print(sentence[-4:])

# ============================================================
# Problem 20
# ============================================================

numbers = [2, 3, 4, 6, 1]
numbers_tuple = tuple(numbers)

print(numbers)
print(numbers_tuple)

# ============================================================
# Problem 21
# ============================================================

phone_brand = "Mango Phone"
battery_percentage = 96
apps = ["Whatsapp", "LinkedIn", "ToDo"]

phone_brand_chars = list(phone_brand)
battery_percentage = float(battery_percentage)

print(phone_brand, battery_percentage, apps, phone_brand_chars)

# ============================================================
# Problem 22
# ============================================================

full_name = "Krishna Sharma"
print(len(full_name))

vowel_count = 0
for ch in full_name.lower():
    if ch in "aeiou":
        vowel_count += 1

print(vowel_count)
print(full_name[0], full_name[-1])

# ============================================================
# Problem 23
# ============================================================

college_name = "Silver Oak"
passing_year = 2027
cgpa = 7.6

passing_year = str(passing_year)
college_name = college_name.upper()
cgpa = int(cgpa)

print(passing_year, college_name, cgpa)

# ============================================================
# Problem 24
# ============================================================

sentence = "I Love Solving Problems"

print(len(sentence))
print(sentence.count(" "))
print(sentence[:4])
print(sentence[-2:])

# ============================================================
# Problem 25
# ============================================================

a, b, c, d, e = 1, 2.3, True, [1, 2], (2, 3)
print(f"{a}, {b}, {c}, {d}, {e}")

# ============================================================
# Problem 26
# ============================================================

laptop_brand = "Dell"
ram = 8
ssd = 512

laptop_brand = list(laptop_brand)
ram = float(ram)
ssd = str(ssd)

print(laptop_brand, ram, ssd)

# ============================================================
# Problem 27
# ============================================================

address = "314022, Sabla, Dungarpur"
print(len(address))

vowels = 0
for ch in address.lower():
    if ch in "aeiou":
        vowels += 1

print(vowels)
print(address[0])
print(address[-1])

# ============================================================
# Problem 28
# ============================================================

nums = [1, 2, 3, 4]
nums_tuple = tuple(nums)

print(nums)
print(nums_tuple)
