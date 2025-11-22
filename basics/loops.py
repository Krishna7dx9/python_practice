# ============================================================
#                         LOOPS IN PYTHON
# ============================================================

# ------------------------------------------------------------
# 1. FOR LOOP (used when you know HOW MANY times to repeat)
# ------------------------------------------------------------

# Basics for loops 

for i in range(5):
    print(i)

# range(a, b) → starts at a, ends at b-1

for x in range(5, 7):
    print(x)

# range with step    

for j in range(2, 10, 2):
    print(j)

# Loop through a list

nums = [10, 20, 30]
for n in nums:
    print(n)

# Loop through a string

word = "Kris"
for char in word:
    print(char)

# ------------------------------------------------------------
# 2. WHILE LOOP (used when you DON'T know how many times)
# ------------------------------------------------------------

# Basic while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# While loop example: stop when value becomes 10

value = 1
while value !=10:
    print(value)
    value += 1

# ------------------------------------------------------------
# 3. LOOP CONTROL: break, continue, pass
# ------------------------------------------------------------

# break → stop the loop completely
for k in range(18):
    if k == 4:
        break
    print(k)

# continue → skip the current iteration
for m in range(6):
    if m == 2:
        continue
    print(m)

# pass → placeholder (does nothing)
for t in range(3):
    pass                                       # useful when writing empty blocks

# ------------------------------------------------------------
# 4. Nested loops
# ------------------------------------------------------------

for a in range(2):
    for b in range(3):
        print(a, b)

























