# =============================================================
# Topic: Data Types — Booleans (bool)
# =============================================================

# Booleans represent True or False.
# In Python, bool is a subclass of int: True == 1, False == 0

# --- Upcasting: bool used in arithmetic ---
is_boiling = True       # True is treated as 1 in numeric context
stir_count = 5
total_actions = stir_count + is_boiling  # 5 + 1 = 6
print(f"Total actions: {total_actions}")

# --- Casting values to bool ---
# Rules: 0, None, "", [], {} -> False  |  anything else -> True
milk_present = 1        # try 0 for False, or a non-empty string for True
print(f"Is there milk? {bool(milk_present)}")

# --- Logical operators: and, or, not ---
# or  -> True if at least one operand is True
# and -> True only if both operands are True
# not -> inverts the boolean value

hot_water = True
tea_added = True

can_serve = hot_water and tea_added   # both must be True to serve
print(f"Can serve chai? {can_serve}")
