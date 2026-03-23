# -----------------------------------
#  What is a Set?
# -----------------------------------
# A set is a collection that is:
# - Unordered
# - Mutable
# - Contains UNIQUE elements (no duplicates allowed)

essential_spices = {"cardamom", "cinnamon", "clove"}
optional_spices = {"ginger", "nutmeg", "clove"}

# -----------------------------------
#  Set Operations
# -----------------------------------

# Union: combines all unique elements from both sets
all_spices = essential_spices | optional_spices
print(f"All spices (union): {all_spices}")

# Intersection: elements present in BOTH sets
common_spices = essential_spices & optional_spices
print(f"Common spices (intersection): {common_spices}")

# Difference: elements only in the first set
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

# -----------------------------------
#  Membership Testing
# -----------------------------------
# Check if an element exists in a set

print(f"Is 'clove' in essential spices? {'clove' in essential_spices}")

# -----------------------------------
#  Frozenset (Immutable Set)
# -----------------------------------
# A frozenset is:
# - Immutable (cannot be modified after creation)
# - Unordered
# - Contains unique elements
# - Hashable (can be used as dictionary keys or inside other sets)

frozen_spices = frozenset(["cardamom", "cinnamon", "clove"])

print(f"Frozen spices: {frozen_spices}")

#  The following would raise an error:
# frozen_spices.add("ginger")  # Not allowed

# Example use case: using frozenset as a dictionary key
spice_profiles = {
    frozenset(["cardamom", "cinnamon"]): "Sweet blend",
    frozenset(["ginger", "clove"]): "Spicy blend"
}

print(f"Spice profiles: {spice_profiles}")