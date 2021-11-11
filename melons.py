"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
        
    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        # if type = Christmas
        if self.species == "Christmas":
            base_price *= 1.5

        # international < 10
        if self.order_type == "international" and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + 3
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    # add additional parameter to subclass init
    def __init__(self, species, qty, country_code):
        # inherit all parameters from superclass that exist
        super().__init__(species, qty)
        # assign new attribute that does not exist in super class
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        if passed == "Yes":
            self.passed_inspection = True


one = GovernmentMelonOrder("Watermelon", 3)
two = InternationalMelonOrder("watermelon", 19, "AUS")