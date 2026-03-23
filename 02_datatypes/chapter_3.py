# =============================================================
# Topic: Data Types — Integers (int)
# =============================================================

# Integers are whole numbers (no decimal point).
# Python supports: +, -, *, / (float division), // (floor division), % (modulo), ** (exponent)

# --- Addition ---
black_tea_grams = 14
ginger_grams = 2
total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

# --- Subtraction ---
remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining tea: {remaining_tea}")

# --- Float division (/) — always returns a float ---
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving: {milk_per_serving}")

# --- Floor division (//) — returns the whole number part only ---
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Tea bags per pot: {bags_per_pot}")

# --- Modulo (%) — returns the remainder ---
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

# --- Exponent (**) ---
base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Flavor strength {base_flavor_strength} scaled by {scale_factor} = {powerful_flavor}")

# --- Underscore separator — makes large numbers more readable ---
total_tea_leaves = 1_000_000_000
print(f"Total tea leaves: {total_tea_leaves}")
