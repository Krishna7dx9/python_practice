# ============================
# PYTHON SYNTAX — TUPLES
# ============================

# 1. Creating Tuples

t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (1,)                 # single-element tuple MUST have a comma
t4 = ()                   # empty tuple
t5 = tuple([1, 2, 3, 4])  # converting list to tuple

# 2. Accessing Elements

x = t1[0]                  # indexing
y = t1[-1]                 # Negative indexing

# 3. Slicing

s1 = t1[1:3]
s2 = t1[:]

# 4. Tuple is IMMUTABLE (cannot change values)
# t1[0] = 10                # ❌ ERROR

# 5. Tuple Methods

count_val = t1.count(2)
index_val = t1.index(3)

# 6. Tuple Unpacking

a, b, c = t1

# 7. Nested Tuples

t_nested = (1, (1, 2), (9, 10))

# 8. Tuple + Tuple

t6 = t1 + (2, 6)

# 9. Tuple Repetition

t7 = t1 * 3

# 10. Why Tuples?
# - Faster than lists
# - Used for fixed collections
# - Safer (immutable)
# - Common in interview return-values (like returning multiple values)

# ============================
# END OF TUPLE TEACHING
# ============================

# 1. Create a tuple with values (10, 20, 30) and return the first element.

t1 = (10, 20, 30)

def f1(t1):
    return t1[0]               # 1

f1(t1)

# 2. Given a tuple t = (5, 10, 15, 20), return a slice containing (10, 15).

t = (5, 10, 15, 20)

def f2(t):
    return t[1, 3]

f2(t)

# 3. Write a function that takes a tuple and returns how many times 2 appears.

t2 = (1, 2, 3, 4, 2, 2)

def f3(t2):
    return t2.count(2)

f3(t2)

# 4. Return the index of value 50 in the tuple (10, 20, 30, 40, 50).

t3 = (5, 10, 15, 20)

def f4(t3):
    return t3.index(50)

f4(t3)

# 5. Given a tuple (1, 2, 3) unpack it into variables a, b, c and return a + c.

t4 = (1, 2, 3)

def f5(t4):
    a, b, c = t4
    return a + c

f5(t4)

# 6. Write a function that takes a nested tuple 
#    like: (1, (2, 3), (4, 5))
#    and return the element 3.

# 7. Combine two tuples (1, 2) and (3, 4) without using list conversion.

# 8. Repeat the tuple ('x',) 5 times.

# 9. Write a function that checks if the first and last element of a tuple are equal.

# 10. Given a tuple (10, 20, 30, 40), return a NEW tuple where each element is multiplied by 2.

