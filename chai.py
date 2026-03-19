# =============================================================
# Example: Classes in Python
# Topic  : Class definition, attributes, and methods
# =============================================================


class Chai:
    """
    Represents a cup of chai (spiced tea).

    Attributes:
        sweetness  (int): Sweetness level (e.g., scale 1–5)
        milk_level (int): Amount of milk (e.g., scale 1–5)
    """

    def __init__(self, sweetness, milk_level):
        """Initializes the chai with sweetness and milk level."""
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        """Simulates taking a sip of the chai."""
        print("Sipping chai...")

    def add_sugar(self, amount):
        """
        Adds sugar to the chai.

        Args:
            amount (int): Amount of sugar to add.
        """
        self.sweetness += amount
        print(f"Added {amount} units of sugar. New sweetness: {self.sweetness}")


# --- Using the class ---
my_chai = Chai(sweetness=3, milk_level=2)

my_chai.sip()           # Take a sip
my_chai.add_sugar(3)    # Add 3 units of sugar