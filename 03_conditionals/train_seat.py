"""
Railway Ticket System – Seat Type Features

This script:
- Takes user input for a seat type
- Uses match-case (Python 3.10+) to determine features
- Handles invalid input gracefully
"""

# -----------------------------------
# User Input
# -----------------------------------
seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").strip().lower()

# -----------------------------------
# Match-Case Logic
# -----------------------------------
match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")

    case "ac":
        print("AC - Air conditioned, beds available")

    case "general":
        print("General - Basic seating, no AC")

    case "luxury":
        print("Luxury - Premium seating, AC and additional amenities")

    case _:
        print("Unknown seat type. Please choose from sleeper, AC, general, or luxury.")