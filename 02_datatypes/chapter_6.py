# -----------------------------------
#  Strings in Python
# -----------------------------------
# In Python, strings are IMMUTABLE.
# This means once a string is created, it cannot be changed.
# Any modification creates a new object in memory.

# Everything inside quotes (" " or ' ') is considered a string.

# -----------------------------------
#  Example Variables
# -----------------------------------
chai_type = "Ginger chai"
customer_name = "Alan Toro"

print(f"Customer: {customer_name}, Order: {chai_type}")

# -----------------------------------
#  Indexing & Slicing
# -----------------------------------
# Each character in a string has an index starting from 0.
# The ending index in slicing is NOT inclusive.

chai_description = "Aromatic and bold"

#  Empty slice (start and end are the same)
print(f"Empty slice: '{chai_description[0:0]}'")

#  Extracting "Aromatic"
print(f"First word: {chai_description[0:8]}")

#  Taking every 2 characters
print(f"Every two letters: {chai_description[0:8:2]}")

#  Extracting "bold"
print(f"Last word: {chai_description[12:]}")

#  Reversing the string
print(f"Reversed: {chai_description[::-1]}")

# -----------------------------------
# Encoding & Decoding
# -----------------------------------
# When working with special characters (like accents),
# it's a good practice to encode strings using UTF-8.

label_text = "Chai Spécial"

# Encode string into bytes
encoded_label = label_text.encode("utf-8")

print(f"Original label: {label_text}")
print(f"Encoded label: {encoded_label}")

# Decode bytes back to string
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")