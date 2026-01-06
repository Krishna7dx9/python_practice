# =========================
# PYTHON ITERATORS — BASICS
# =========================

# 1️⃣ WHAT IS AN ITERATOR?
# An iterator is an object that allows you to traverse through elements
# one at a time, using a fixed protocol.

# The iterator protocol requires two methods:
# 1. __iter__()  → returns the iterator object itself
# 2. __next__()  → returns the next value, or raises StopIteration

# 2️⃣ ITERABLE vs ITERATOR

# Iterable:
# An object you can loop over (list, tuple, string, etc.)
numbers = [1, 2, 3]

# Iterator:
# An object that keeps track of the current position
iterator = iter(numbers)              # iter() converts iterable -> iterator

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# print(next(iterator))  # ❌ StopIteration (no elements left)

# 3️⃣ HOW FOR LOOP WORKS INTERNALLY

# for x in numbers:
#     print(x)

# Internally, Python does this:
# 1. iterator = iter(numbers)
# 2. repeatedly calls next(iterator)
# 3. stops when StopIteration is raised

# 4️⃣ ITERATORS ARE STATEFUL

iterator2 = iter(numbers)

print(next(iterator2))    # 1
print(next(iterator2))    # 2

# The iterator remembers where it stopped.
# You cannot reset it unless you create a new iterator.

# 5️⃣ STRING IS ALSO ITERABLE

text = "ABC"
text_iterator = iter(text)

print(next(text_iterator))   # A
print(next(text_iterator))   # B
print(next(text_iterator))   # C

# 6️⃣ CREATING A CUSTOM ITERATOR (IMPORTANT)

class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self              # iterator must return itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 3)

print(next(counter))     # 1
print(next(counter))     # 2
print(next(counter))     # 3
# print(next(counter))  # ❌ StopIteration

# 7️⃣ USING CUSTOM ITERATOR IN FOR LOOP

counter2 = CountUp(5, 7)

for num in counter2:
    print(num)

# 8️⃣ KEY RULES (MEMORIZE)
# ✔ iter(obj) → gives iterator
# ✔ next(iterator) → gives next value
# ✔ StopIteration ends iteration
# ✔ for-loop uses iter() + next() internally
# ✔ Iterator remembers state

# ==============================
# ITERATORS — Test (QUESTIONS)
# ==============================

# Q1
# For each object below, print whether it has:
# 1) __iter__
# 2) __next__
#
# Objects:
# - list                            -- has __iter__
# - list iterator                   -- has __next__
# - set                             -- has __iter__
# - set iterator                    -- has __next__
# - dict                            -- has __iter__ 
# - dict iterator                   -- has __next__

# Q2
# Create ONE iterator from a list.
# Use a first for-loop to print all elements.
# Use a second for-loop on the SAME iterator to prove exhaustion.

print()
a = [1, 2, 3]
b = iter(a)
for x in b:
    print(x)
for y in b:
    print(y)

# Q3
# Without using a for-loop:
# Iterate completely through [100, 200, 300]
# Use iter(), next(), and try/except StopIteration.

p = [100, 200, 300]
q = iter(p)

print()
while True:
    try:
        print(next(q))
    except StopIteration:
        print("Iteration finished")
        break

# Q4
# Create an iterator.
# Prove using code that:
# iter(iterator) is iterator

print()
a = [1, 2, 3]              # iterable 
b = iter(a)                # iterator
print(next(b))             
c = iter(b)                # iter of iterator
print(next(c))             # iter of iterator worms as same as iterator  (shows same behaviour)
d = b is c                 # iter(iterator) is iterator (Shows same identtity)
print(d) 

# Q5
# Create a dictionary with at least two key-value pairs.
# Iterate over it using a for-loop.
# Print exactly what is produced by default.

print()
student = {
    "Name": "Kris",
    "Age": 19,
    "is_codes" : True
}

for x in student:
    print(x)