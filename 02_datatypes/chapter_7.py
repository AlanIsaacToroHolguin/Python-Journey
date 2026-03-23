#  What is a Tuple?
# -----------------------------------
# A tuple is a collection of items that is:
# - Ordered
# - Immutable (cannot be changed after creation)

masala_spices = ("cardamom", "cinnamon", "cloves")

# -----------------------------------
#  Immutability
# -----------------------------------
# Tuples cannot be modified once created.
# However, you can create new tuples or concatenate them.

# -----------------------------------
#  Tuple Unpacking
# -----------------------------------
# You can assign tuple values to variables in a single line.

spice1, spice2, spice3 = masala_spices

print(f"Spice 1: {spice1}, Spice 2: {spice2}, Spice 3: {spice3}")

# -----------------------------------
#  Multiple Variable Assignment
# -----------------------------------
# Python allows assigning multiple values at once.

ginger_ratio, cardamom_ratio = 2, 1

print(f"Ginger Ratio: {ginger_ratio}, Cardamom Ratio: {cardamom_ratio}")

#  Swapping values (very common use case)
ginger_ratio, cardamom_ratio = 1, 2

print(f"Ginger Ratio: {ginger_ratio}, Cardamom Ratio: {cardamom_ratio}")

# -----------------------------------
#  Membership Testing
# -----------------------------------
# You can check if an element exists in a tuple using 'in'.

print(f"Is 'ginger' in masala_spices? {'ginger' in masala_spices}")  # False
print(f"Is 'cardamom' in masala_spices? {'cardamom' in masala_spices}")  # True