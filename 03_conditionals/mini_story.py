"""
Smart Kettle Notification System

This script:
- Checks whether the kettle has finished boiling
- Notifies the user when it is ready
- Displays a waiting message otherwise
"""

# -----------------------------------
# Input State
# -----------------------------------
kettle_boiled = False  # Change to True when boiling is complete

# -----------------------------------
# Conditional Logic
# -----------------------------------
if kettle_boiled:
    print("Kettle done! Time to make chai!")
else:
    print("Kettle is still boiling. Please wait.")