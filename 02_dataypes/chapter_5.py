# =============================================================
# Topic: Data Types — Floats and Precision
# =============================================================

# Floats are real numbers with a decimal point.
# Python uses IEEE 754 double precision (64-bit) for floats.
# Use Decimal or Fraction when exact precision is required.

import sys
from fractions import Fraction
from decimal import Decimal

# --- Basic float ---
ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp:   {ideal_temp}")
print(f"Current temp: {current_temp}")
print(f"Difference:   {ideal_temp - current_temp}")

# --- Float system info (max/min values, precision, etc.) ---
print(sys.float_info)

# --- Note: complex numbers also exist in Python ---
# They are written as: z = 3 + 4j
# Mainly used in scientific/engineering contexts, not covered here.
