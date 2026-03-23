
# -----------------------------------
#  What is a List?
# -----------------------------------
# In Python, what other languages call "arrays" are typically implemented as lists.
# Lists are:
# - Ordered
# - Mutable (can be modified after creation)
# - Allow duplicate elements

ingredients = ["water", "milk", "black tea"]

# -----------------------------------
#  Adding Elements
# -----------------------------------
ingredients.append("sugar")  # Adds an element at the end

print(f"Ingredients: {ingredients}")

# -----------------------------------
# ➖ Removing Elements
# -----------------------------------
ingredients.remove("water")  # Removes a specific element

print(f"Updated ingredients: {ingredients}")

# -----------------------------------
#  Combining Lists
# -----------------------------------
spice_ingredients = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_ingredients)  # Merge lists

print(f"Chai ingredients: {chai_ingredients}")

# -----------------------------------
#  Inserting Elements
# -----------------------------------
# Indexing starts at 0

chai_ingredients.insert(2, "black tea")

print(f"Updated chai ingredients: {chai_ingredients}")

# -----------------------------------
# Removing Last Element
# -----------------------------------
last_added = chai_ingredients.pop()  # Removes and returns last item

print(f"Removed ingredient: {last_added}")
print(f"Remaining chai ingredients: {chai_ingredients}")

# -----------------------------------
# Reversing a List
# -----------------------------------
chai_ingredients.reverse()  # In-place modification

print(f"Reversed (in-place): {chai_ingredients}")

# Alternative: slicing (does NOT modify original list)
print(f"Reversed (copy): {chai_ingredients[::-1]}")

# -----------------------------------
# Sorting
# -----------------------------------
chai_ingredients.sort()  # Alphabetical order

print(f"Sorted chai ingredients: {chai_ingredients}")

# -----------------------------------
# Built-in Functions
# -----------------------------------
sugar_levels = [1, 2, 3, 4, 5]

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

# -----------------------------------
# Operator Overloading with Lists
# -----------------------------------
# In Python, operators like + and * work with lists

base_liquid = ["water", "milk"]
extra_liquid = ["soda"]

# Concatenation (creates a new list)
full_liquid_mix = base_liquid + extra_liquid
print(f"Full liquid mix: {full_liquid_mix}")

# Repetition
strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

# -----------------------------------
#  Bytearray Basics
# -----------------------------------
# A bytearray is a mutable sequence of bytes

raw_spice_data = bytearray(b"CINNAMON")

# Replace part of the bytearray
raw_spice_data = raw_spice_data.replace(b"CINNAMON", b"CINNAMON CARDAMOM")

print(f"Raw spice data: {raw_spice_data}")