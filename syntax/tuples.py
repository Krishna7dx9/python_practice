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

def f2(t00):
    return t00[1:3]

f2(t)

# 3. Write a function that takes a tuple and returns how many times 2 appears.

t2 = (1, 2, 3, 4, 2, 2)

def f3(t2):
    return t2.count(2)

f3(t2)

# 4. Return the index of value 50 in the tuple (10, 20, 30, 40, 50).

t3 = (10, 20, 30, 40, 50)

def f4(t3):
    x = t3.index(50)
    return x
 
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

def nested_tuple(a):
    return a[1][1]

a = (1, (2, 3), (4, 5))

nested_tuple(a)

# 7. Combine two tuples (1, 2) and (3, 4) without using list conversion.

a = (1, 2)
b = (3, 4)

c = a + b

# 8. Repeat the tuple ('x',) 5 times.

t8 = ('x',)
t9 = t8 * 5

# 9. Write a function that checks if the first and last element of a tuple are equal.

def check(a):
    return a[0] == a[-1]

check(a)

# 10. Given a tuple (10, 20, 30, 40), return a NEW tuple where each element is multiplied by 2.

t10 = (10, 20, 30, 40)

def each_by2(t):
    a = ()
    for x in t:
        a = a + (x * 2,)
    return a

each_by2(t10)

# 11. Given a tuple t = (1, 2, 3, 4, 5)
#     return a NEW tuple containing only the even numbers.


# 12. Write a function that swaps the first and last element 
#     of a tuple and returns the new tuple.
#     Example: (10, 20, 30, 40) → (40, 20, 30, 10)


# 13. Given two tuples (1, 2, 3) and (4, 5), 
#     return a single tuple using unpacking (no + operator).


# 14. Write a function that returns the maximum element of a tuple
#     WITHOUT using max().


# 15. Given a tuple of strings ("a","bb","ccc"), 
#     return a tuple of their lengths.  → (1,2,3)


# 16. Write a function that reverses a tuple WITHOUT using slicing.


# 17. Given t = (10, 20, 30, 40, 50),
#     return a tuple of only the middle elements → (20, 30, 40)


# 18. Count how many tuples exist inside:
#     x = (1, (2, 3), (4, 5, 6), 7, (8,))
#     Output → 3


# 19. Given t = ((1,2), (3,4), (5,6))
#     return a tuple of all second elements → (2, 4, 6)


# 20. Write a function that returns True if a tuple is sorted
#     in NON-decreasing order, else False.
#     Example: (1,2,2,3) → True; (3,1,2) → False
