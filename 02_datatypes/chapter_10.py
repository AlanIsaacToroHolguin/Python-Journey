# -----------------------------------
# What is a Dictionary?
# -----------------------------------
# A dictionary (dict) is a mutable data structure that stores data
# in key-value pairs.
#
# Key characteristics:
# - Keys must be unique and immutable (e.g., strings, numbers, tuples)
# - Values can be of any data type
# - Dictionaries are unordered (ordered since Python 3.7+)
# - Ideal for fast lookups using: dictionary[key]

chai_order = dict(type="Masala chai", size="Large", lvl_sugar="2")

print(f"Chai order: {chai_order}")

# -----------------------------------
# Creating and Modifying Dictionaries
# -----------------------------------
chai_recipe = {}

chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")

# Removing a key-value pair
del chai_recipe["base"]
print(f"Updated recipe: {chai_recipe}")

# -----------------------------------
# Membership Testing
# -----------------------------------
# Checks if a key exists in the dictionary

print(f"Is 'liquid' in chai_order? {'liquid' in chai_order}")

# -----------------------------------
# Dictionary Methods
# -----------------------------------
chai_order2 = {"type": "Ginger chai", "size": "medium", "sugar": "1"}

print(f"Order keys: {chai_order2.keys()}")
print(f"Order values: {chai_order2.values()}")
print(f"Order items: {chai_order2.items()}")

# Note:
# items() returns tuples inside a view object (key, value)

# -----------------------------------
# Removing Elements
# -----------------------------------
# popitem() removes and returns the last inserted key-value pair

last_item = chai_order2.popitem()
print(f"Removed last item: {last_item}")

# -----------------------------------
# Updating Dictionaries
# -----------------------------------
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}

chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

# -----------------------------------
# Accessing Values
# -----------------------------------
chai_size = chai_order["size"]
print(f"Chai size: {chai_size}")

# Safe access using get()
# If the key does not exist, a default value can be provided

customer_note = chai_order.get("customer_note", "No note provided")
print(f"Customer note: {customer_note}")