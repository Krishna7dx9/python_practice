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
print(next(iterator))     # 2

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