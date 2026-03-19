# =============================================================
# Topic: Data Types — Objects in Python
# =============================================================

# Everything in Python is an object.
# Each object is composed of:
#   - identity : unique ID in memory (id())
#   - type     : what kind of object it is (int, str, etc.)
#   - value    : the data it holds

# --- Mutable vs Immutable ---
# Mutable   : can be changed after creation (e.g. list, set, dict)
# Immutable : cannot be changed after creation (e.g. int, str, tuple)
# When an immutable value changes, Python creates a NEW object in memory.

sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")
print(f"id of 2: {id(2)}")

sugar_amount = 12
print(f"Updated sugar: {sugar_amount}")
print(f"id of 12: {id(12)}")

# Notice the ids are different — a new int object was created, not mutated.