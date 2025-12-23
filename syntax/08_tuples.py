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

t11 = (1, 2, 3, 4, 5)

def even_tuple(t):
    t12 = ()
    for x in t:
        if x % 2 == 0:
            t12 = t12 + (x,)
    return t12

even_tuple(t11)

# 12. Write a function that swaps the first and last element 
#     of a tuple and returns the new tuple.
#     Example: (10, 20, 30, 40) → (40, 20, 30, 10)

t13 = (10, 20, 30, 40)

def swap_tuple(t):
    last = t[-1]
    first = t[0]
    l = len(t) - 1
    middle = t[1:l]
    t14 = last, *middle, first
    return t14

swap_tuple(t13)

# 13. Given two tuples (1, 2, 3) and (4, 5), 
#     return a single tuple using unpacking (no + operator).

t14 = (1, 2, 3)
t15 = (4, 5)

def single_tuple(a, b):
    t16 = *a, *b
    return t16

single_tuple(t14, t15)

# 14. Write a function that returns the maximum element of a tuple
#     WITHOUT using max().

def maxi(t):
    maximum = t[0]
    for x in t:
        if x > maximum:
            maximum = x
    return maximum

maxi(t14)

# 15. Given a tuple of strings ("a","bb","ccc"), 
#     return a tuple of their lengths.  → (1,2,3)

def tuple_length(t):
    length_tuple = ()
    for x in t:
        z = str(x)
        y = len(z)
        length_tuple = length_tuple + (y,)
    return length_tuple

tuple_length(t14)

# 16. Write a function that reverses a tuple WITHOUT using slicing.

def reverse_(t):
    t16 = ()
    for x in t:
        t16 = (x,) + t16
    return t16

reverse_(t14)

# 17. Given t = (10, 20, 30, 40, 50),
#     return a tuple of only the middle elements → (20, 30, 40)

t17 = (10, 20, 30, 40, 50)

def middle_(t):
    l = len(t) - 1
    return t[1:l]

middle_(t17)

# 18. Count how many tuples exist inside:
#     x = (1, (2, 3), (4, 5, 6), 7, (8,))
#     Output → 3

x = (1, (2, 3), (4, 5, 6), 7, (8,))

count = 0
for element in x:
    if isinstance(element, tuple):
        count += 1

print(count)

# 19. Given t = ((1,2), (3,4), (5,6))
#     return a tuple of all second elements → (2, 4, 6)

t = ((1,2), (3,4), (5,6))

def second(t):
    t18 = ()
    for x in t:
        a = x[1]
        t18 = t18 + (a,)
    return t18

second(t)

# 20. Write a function that returns True if a tuple is sorted
#     in NON-decreasing order, else False.
#     Example: (1,2,2,3) → True; (3,1,2) → False

a = (5,4,3,2,1)
def sorted_check(a):
    prev = a[0]

    for x in a:
        if x < prev:
            return False
        prev = x
    
    return True

sorted_check(a)