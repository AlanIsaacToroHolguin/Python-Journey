"""
Tea Stall Pricing System

This script:
- Takes user input for cup size
- Calculates the price based on size
- Handles invalid input gracefully
"""

# -----------------------------------
# User Input
# -----------------------------------
cup_size = input("Choose your cup size (small/medium/large): ").strip().lower()

# -----------------------------------
# Conditional Logic
# -----------------------------------
if cup_size == "small":
    print("The price for a small cup of chai is 10 COP.")

elif cup_size == "medium":
    print("The price for a medium cup of chai is 15 COP.")

elif cup_size == "large":
    print("The price for a large cup of chai is 20 COP.")

else:
    print("Unknown cup size.")