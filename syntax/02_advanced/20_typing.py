# ============================================================
# PYTHON TYPING (TYPE HINTS) — SINGLE FILE TEACHING
# ============================================================

# Python typing adds TYPE INFORMATION
# It does NOT enforce types at runtime
# It is used for readability, tooling, and large codebases


# ------------------------------------------------------------
# 1. BASIC VARIABLE TYPE HINTS
# ------------------------------------------------------------

name: str = "Kris"
age: int = 21
height: float = 5.9
is_student: bool = True

# Python will NOT stop wrong assignments at runtime
age = "twenty one"   # allowed, but logically wrong


# ------------------------------------------------------------
# 2. FUNCTION TYPE HINTS
# ------------------------------------------------------------

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return "Hello " + name

def log(message: str) -> None:
    print(message)
    # -> None means function returns nothing


# ------------------------------------------------------------
# 3. COLLECTION TYPES (Python 3.9+)
# ------------------------------------------------------------

numbers: list[int] = [1, 2, 3]
names: list[str] = ["a", "b", "c"]

scores: dict[str, int] = {"math": 90, "science": 95}
ids: set[int] = {1, 2, 3}

def total(nums: list[int]) -> int:
    return sum(nums)


# ------------------------------------------------------------
# 4. TUPLE TYPES
# ------------------------------------------------------------

# Fixed size tuple
point: tuple[int, int] = (10, 20)

# Variable size tuple (same type)
values: tuple[int, ...] = (1, 2, 3, 4)


# ------------------------------------------------------------
# 5. UNION TYPES (MULTIPLE POSSIBLE TYPES)
# ------------------------------------------------------------

# Python 3.10+
def stringify(x: int | str) -> str:
    return str(x)


# ------------------------------------------------------------
# 6. OPTIONAL VALUES (TYPE OR NONE)
# ------------------------------------------------------------

def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Kris"
    return None


# ------------------------------------------------------------
# 7. TYPE ALIAS
# ------------------------------------------------------------

UserId = int

def get_user(uid: UserId) -> str:
    return "User"


# ------------------------------------------------------------
# 8. IMPORTANT FACTS
# ------------------------------------------------------------

# - Type hints are ignored at runtime
# - Used by tools like mypy, pyright
# - Mandatory in serious production Python
# - Google Python code is heavily typed


# ============================================================
# TEST — PYTHON TYPING (COMPLETED)
# ============================================================

# Q1: Add correct type hints
name: str = "Kris"
age: int = 21
scores: list[int] = [90, 80, 70]

# Q2: Add type hints to this function
def multiply(a: float, b: float) -> float:
    return a * b

# Q3: Function returns string or None
from typing import Optional

def get_email(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "a@b.com"
    return None

# Q4: Write a function with typing:
# Input: list of integers | Output: integer (sum)
def calculate_sum(numbers: list[int]) -> int:
    return sum(numbers)

# Q5: Correct the type hint
data: tuple[str, ...] = ("a", "b", "c")

# Q6: Type hint for dictionary (keys: str, values: list[int])
results: dict[str, list[int]] = {"math": [90, 80]}

# Q7: What does -> None mean in function typing?
# It specifies that the function explicitly returns no value (None).