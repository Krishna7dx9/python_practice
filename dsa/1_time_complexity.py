# Answer all. No explanations unless asked.

# Q1
for i in range(n):
    for j in range(i):
        for k in range(5):
            pass
# Time Complexity?

# O(n^2)

# Q2
for i in range(n):
    for j in range(n // 2):
        pass
# Time Complexity?

# O(n^2)

# Q3
for i in range(n):
    for j in range(i):
        for k in range(j):
            pass
# Time Complexity?

# O(n^3)

# Q4
for i in range(n):
    j = i
    while j > 0:
        j = j // 2
# Time Complexity?

# O(nlogn)

# Q5
for i in range(n):
    for j in range(n):
        break
# Time Complexity?

# O(n)

# ==============================
# NESTED LOOP — RETEST
# ==============================

# Q6
for i in range(n):
    for j in range(3):
        pass
# Time Complexity?

# O(n)

# Q7
for i in range(n):
    for j in range(i):
        for k in range(2):
            pass
# Time Complexity?

# O(n^2)

# Q8
for i in range(n):
    j = 1
    while j < n:
        j = j * 2
# Time Complexity?

# O(nlogn)

# Q9
for i in range(n):
    for j in range(n):
        break
# Time Complexity?

# O(n)

# Q10
for i in range(n):
    for j in range(i):
        for k in range(j):
            for x in range(10):
                pass
# Time Complexity?

# O(n^3)

# ==============================
# TIME COMPLEXITY — FINAL TEST
# ==============================

# Q1
# What does Time Complexity measure?

# How runtime grows as input size n increases.

# Q2
# Simplify:
# O(7n + 3n + 100)

# O(n)

# Q3
# Simplify:
# O(n^2 + n log n + n)

# O(n^2)

# Q4
for i in range(n):
    print(i)
# Time Complexity?

#  O(n)

# Q5
for i in range(n):
    for j in range(i):
        print(i, j)
# Time Complexity?

# O(n^2)

# Q6
i = n
while i > 1:
    i = i // 2
# Time Complexity?

# O(log n)

# Q7
for i in range(n):
    j = i
    while j > 0:
        j = j // 2
# Time Complexity?

# O(nlogn)

# Q8
# What is the worst-case time complexity of linear search?

# O(n)

# Q9
# True or False:
# Big-O notation ignores constants and lower-order terms.

# True

# Q10
# Choose the dominant term:
# O(n + n log n + n^2)

# O(n^2)