"""
Online Tea Store – Delivery Fee Calculator

This script:
- Takes the order amount as input
- Uses a ternary operator to determine the delivery fee
- Applies free delivery for orders below 30 COP
"""

# -----------------------------------
# User Input
# -----------------------------------
order_amount = float(input("Enter the order amount in COP: "))

# -----------------------------------
# Ternary Operator Logic
# -----------------------------------
# If the order amount is less than 30 COP → free delivery
# Otherwise → delivery costs 5 COP

delivery_fee = 0 if order_amount < 30 else 5

# -----------------------------------
# Output
# -----------------------------------
print(f"Your delivery fee is: {delivery_fee} COP")