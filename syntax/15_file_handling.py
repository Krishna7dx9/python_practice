# ================================
#   PYTHON FILE HANDLING BASICS
# ================================

# -------- 1. Opening Files --------
# open(filename, mode)
# Modes:
#   r  -> read (file must exist)
#   w  -> write (create or overwrite)
#   a  -> append (add at end)
#   r+ -> read + write (file must exist)
#   w+ -> write + read (overwrites)
#   a+ -> append + read

# -------- 2. Writing to a File --------
# 'w' creates or overwrites a file
f = open("example.txt", "w")
f.write("Hello, this is file handling. \n")
f.write("Writting another line. \n")
f.close()                                  # Always close when done

# -------- 3. Appending to a File --------
# 'a' adds data at the end of file
f = open("example.txt", "a")
f.write("This is append text. \n")
f.close()

# -------- 4. Reading Entire File --------
f = open("example.txt", "r")
full_content = f.read()
print("Full read: ")
print(full_content)
f.close()

# -------- 5. Reading Line-by-Line --------
f = open("example.txt", "r")
print("Reading line by line: ")
line = f.readline()                      # read 1st line
while line:
    print(line.strip())
    line = f.readline()
f.close()

# -------- 6. Reading All Lines as List --------
f = open("example.txt", "r")
lines = f.readlines()
print("READLINES (list of lines): ", lines)
f.close()

# -------- 7. Using 'with' (BEST PRACTICE) --------
# Automatically closes file
with open("example.txt", "r") as f:
    first_line = f.readline()
    print("First line read with 'with': ", first_line.strip())

# -------- 8. Read + Write Together (r+) --------
# r+ lets you write without deleting the old content
with open("example.txt", "r") as f:
    f.seek(0)                                      # move pointer to start
    f.write("start of file")                       # overwrites only first part
    f.seek(0)
    print("After r+ write: ")
    print(f.read())

# -------- 9. Handling File Errors --------
try:
    f = open("file_that_does_not_exist.txt", "r")
except FileNotFoundError:
    print("Error! File not found")

# ------------------------------------------------------------
# TEST: FILE HANDLING
# ------------------------------------------------------------

# Q1. Create a file named "data.txt" in write mode.
#     Write the following three lines into it:
#     Line1: "Python File Handling Test"
#     Line2: "Line A"
#     Line3: "Line B"

f = open("data.txt", "w")
f.write("Python File Handling Test \n")
f.write("Line A \n")
f.write("Line B \n")
f.close()

# Q2. Open "data.txt" in append mode.
#     Append: "Line C"

f = open("data.txt", "a")
f.write("Line C \n")
f.close()

# Q3. Read the entire file and print its contents exactly.

f = open("data.txt", "r")
full_file = f.read()
print("Full File: ", full_file)
f.close()

# Q4. Read the file line-by-line using readline() inside a loop.
#     Print each line without extra newlines.

f = open("data.txt", "r")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()
f.close()

# Q5. Read the file using readlines()
#     Print the resulting list.

f = open("data.txt", "r")
lines = f.readlines()
print("Readlines printing: ", lines)
f.close()

# Q6. Use a 'with open' block to:
#       - Open "data.txt" in read mode
#       - Print only the first line

with open("data.txt", "r") as f:
    line = f.readline()
    print("Only first line: ", line)

# Q7. Open "data.txt" in r+ mode.
#     - Move pointer to start using seek()
#     - Write: "UPDATED START\n"
#     - Then read the entire content and print it.

f = open("data.txt", "r+")
f.seek(0)
f.write("UPDATED START\n")
f.seek(0)
full_content = f.read()
print("Full content: ", full_content)
f.close()

# Q8. Try opening "missing.txt" in read mode.
#     Catch FileNotFoundError and print: "File missing"

try:
    f = open("missing.txt", "r")
except FileNotFoundError:
    print("File missing")