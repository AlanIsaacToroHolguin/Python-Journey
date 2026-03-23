# =============================================================
# Topic: Data Types — Mutable objects (Sets)
# =============================================================

# A set is a mutable, unordered collection of unique elements.
# Because it is mutable, adding items does NOT create a new object —
# the same object in memory is modified (same id before and after).

spice_mix = set()

print(f"id before adding items: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("Cardamom")

print(f"Contents: {spice_mix}")
print(f"id after adding items:  {id(spice_mix)}")

# Notice the id stays the same — the set was mutated in place.
