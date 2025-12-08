# ---------------------------
# PYTHON SETS - FULL SYNTAX
# ---------------------------

# 1. Creating sets

a = {1, 2, 3}
b = set([3, 4, 5])                   # Using set constructor
empty_set = set()                    # {} is not empty set, it's dict

# 2. Set properties
# - unordered
# - unique elements only
# - mutable (can add/remove)
# - but elements must be immutable

c = {1, 1, 2, 2, 3, 3}
print("Unique only: ", c)

# 3. Adding & removing

nums = {10, 20}

nums.add(30)          # add element
nums.update([40, 50]) # add multiple elements
nums.remove(20)       # removes; throws error if missing
nums.discard(999)     # removes; NO error if missing
nums.pop()            # removes a random element

print("After add/update.remove: ", nums)

# 4. Set operations

A = {1, 2, 3}
B = {3, 4, 5}

print("Union: ", A | B)                     # {1, 2, 3, 4, 5}
print("Intersection: ", A & B)              # {3}
print("Difference: ", A - B)                # {1, 2}
print("Symmetric Difference: ", A ^ B)      # {1, 2, 4, 5}

# 5. Checking membership

print(2 in A)             # True
print(9 in A)             # False

# 6. Set methods
C = {1, 2, 3}
D = {3, 4}

print(C.isdisjoint(D))               # False
print({1,2}.issubset(D))             # False
print({1, 2, 3}.issuperset({1}))     # True

# 7. Clearing

temp = {100, 200}
temp.clear()
print("After clear: ", temp)

# 8. Frozenset (immutable set)

f = frozenset([1, 2, 3])
print("Frozenset: ", f)

# ============================
# PYTHON SETS – TEST
# ============================

# 1. Create a set containing: 10, 20, 20, 30, 40
#    Print the set.

a = {10, 20, 20, 30, 40}
print("Set a: ", a)

# 2. Given:
#       A = {1, 2, 3}
#       B = {3, 4, 5}
#    Print:
#    # union
#    # intersection
#    # difference (A - B)
#    # symmetric difference

print("Union: ", A | B)
print("Intersection: ", A & B)
print("Difference: ", A - B)
print("Symmetric Difference: ", A ^ B)

# 3. Create:
#       S = {10, 20}
#    Task:
#    # Add 100 to S
#    # Add multiple values [200, 300] in one step
#    # Print S

S = {10, 20}
S.add(100)
S.update([200, 300])
print("S: ", S)

# 4. Given:
#       X = {1, 2, 3, 4}
#    Task:
#    # Check if {1, 2} is a subset of X
#    # Print the result

X = {1, 2, 3, 4}
Y = {1, 2}.issubset(X)       # True
print("{1, 2} is a subset of X: ", Y)

# 5. Create a frozenset with values 5, 6, 7
#    Print the frozenset

F = frozenset([5, 6, 7])
print("Frozenset: ", F)