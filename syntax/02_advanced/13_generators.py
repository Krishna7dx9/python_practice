# -----------------------------
# Python Generators
# -----------------------------

# ===============================
# 1. Introduction to Generators
# ===============================
# Generators are a way to create iterators in Python.
# They allow you to iterate over data without storing the entire sequence in memory.
# Generators use the 'yield' keyword instead of 'return'.

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))           # 1
print(next(gen))           # 2
print(next(gen))           # 3
# print(next(gen))         # Raises StopIteration

# ===============================
# 2. Using Generators in Loops
# ===============================
# Generators are often used in loops directly.

for value in simple_generator():
    print(value)

# ===============================
# 3. Generator Expressions
# ===============================
# Similar to list comprehensions but use parentheses instead of brackets.
# They are memory efficient because they generate values on the fly.

gen_expr = (x*x for x in range(5))
for val in gen_expr:
    print(val)

# ===============================
# 4. Advantages of Generators
# ===============================
# 1. Memory efficiency: don't store all items in memory.
# 2. Lazy evaluation: compute values on demand.
# 3. Useful for reading large files or streams.

# Example: reading large file line by line
# with open('large_file.txt') as f:
#     for line in f:
#         process(line)  # only one line in memory at a time

# ===============================
# 5. Generator with Infinite Sequence
# ===============================
# Useful for streams or continuous data.

def infinite_number(start = 0):
    n = start
    while True:
        yield n
        n += 1

# Example usage (stop manually after 5 numbers)

inf_gen = infinite_number()
for _ in range(5):
    print(next(inf_gen))

# ===============================
# 6. Sending Values to Generators
# ===============================
# You can send values into a generator using .send()

def accumulator():
    total = 0
    while True:
        x = yield total
        if x is None:
            break
        total += x

acc = accumulator()
print(next(acc))              # Initialize generator, prints 0
print(acc.send(10))           # Add 10, print 10
print(acc.send(5))            # Add 5, print 15
acc.close()                   # close generator

# ===============================
# 7. Summary
# ===============================

# - Generators are iterators created with 'yield' or generator expressions.
# - They provide memory efficiency and lazy evaluation.
# - Can be infinite and accept values using .send()
# - Commonly used in data streaming, large files, or sequences.

# ===============================
# PYTHON GENERATORS — TEST
# ===============================

# Q1.
# Explain in 3–4 lines what a generator is and how it differs from a normal function.
# (Answer in comments)

# A generator is a special type of function that returns an iterator using the `yield` keyword.
# Unlike a normal function, it does not terminate after returning a value; it pauses execution.
# The generator preserves its state between yields and resumes from where it left off.
# Normal functions return all results at once, while generators produce values lazily on demand.

# Q2.
# Write a generator function named `count_up_to(n)`
# It should yield numbers from 1 to n (inclusive).
# Example:
# for x in count_up_to(3) → 1 2 3

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

cnt = count_up_to(3)
print(next(cnt))
print(next(cnt))
print(next(cnt))

# Q3.
# What will be the output of the following code?
# Write the exact output in comments.

def test_gen():
    yield 10
    yield 20

g = test_gen()
print(next(g))                    # 10
print(next(g))                    # 20

# Q4.
# Convert this list comprehension into a generator expression:
# squares = [x * x for x in range(1, 6)]

squares = (x * x for x in range(1, 6))

# Q5.
# Write a generator `even_numbers(limit)`
# It should yield all even numbers from 0 up to limit (inclusive).

def even_numbers(limit):
    for _ in range(0, limit + 1):
        if _ % 2 == 0:
            yield _

evn = even_numbers(5)
print(next(evn))

# Q6.
# True or False (answer in comments):
# a) Generators store all values in memory.
# b) Generator expressions use square brackets.
# c) A generator stops automatically after exhaustion.

# a) False - generators are lazy and do not store all values.
# b) False - generator expressions use parentheses.
# c) True - after exhaustion, the generator raises StopIteration and stops.

# Q7.
# Write a generator that produces an infinite sequence of multiples of 3,
# starting from 3.
# Then show how you would print only the first 5 values.

def infinite_sequence():
    start = 3
    while True:
        yield start
        start += 3

infi = infinite_sequence()
print(next(infi))
print(next(infi))
print(next(infi))
print(next(infi))
print(next(infi))

# Q8.
# What happens if `next()` is called on an exhausted generator?
# Explain briefly in comments.

# It will raise a StopIteration exception, indicating the generator is exhausted.

# Q9.
# Write a generator `running_sum()`
# It should:
# - Start with total = 0
# - Accept numbers using `.send()`
# - Yield the updated total each time
# - Stop if None is sent

def running_sum():
    total = 0
    num = yield total               # initialize and yield 0
    while num is not None:
        total += num                # adds input to total
        num = yield total           # waits for next input (overwrites num)

run = running_sum()
print(next(run))
print(run.send(3))
print(run.send(4))

# Q10.
# Explain ONE real-world use case where generators are better than lists.
# (Answer in comments)

# Generators are better than lists when we need to produce values on the fly
# without storing them all in memory, e.g., generating temporary passwords,
# processing large log files, or streaming data.












