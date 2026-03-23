"""
Snack Suggestion System

This script:
- Takes user input for a preferred snack
- Confirms the order if the snack is available
- Handles unavailable options gracefully
"""

# -----------------------------------
# User Input
# -----------------------------------
snack = input("Enter your preferred snack (cookies/samosa): ").strip().lower()

print(f"User said: {snack}")

# -----------------------------------
# Conditional Logic
# -----------------------------------
if snack == "cookies":
    print("Great choice! Your cookies will be ready soon.")

elif snack == "samosa":
    print("Great choice! Your samosa will be ready soon.")

else:
    print("Sorry, we don't have that snack available.")