"""
Smart Thermostat Alert System

This script:
- Evaluates the device status
- Checks the temperature if the device is active
- Displays appropriate alerts based on conditions
"""

# -----------------------------------
# Input Data
# -----------------------------------
device_status = "active"   # Possible values: "active" or "offline"
temperature = 40           # Current temperature

# -----------------------------------
# Conditional Logic
# -----------------------------------
if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal.")
else:
    print("Device is offline.")

# -----------------------------------
# Note on 'pass'
# -----------------------------------
# The 'pass' statement is a placeholder that does nothing.
# It is useful when a statement is syntactically required
# but no action is needed yet.

# Example:
if device_status == "maintenance":
    pass  # Logic can be added here later