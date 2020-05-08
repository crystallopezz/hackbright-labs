############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    Muskmelon = MelonType("musk", "1998", "green", True, True, "Muskmelon")
    Muskmelon.add_pairing(["mint"])
    all_melon_types.append(Muskmelon)

    Casaba = MelonType("cas", "2003", "orange", False, False, "Casaba")
    Casaba.add_pairing(["strawberries", "mint"])
    all_melon_types.append(Casaba)

    Crenshaw = MelonType("cren", "1996", "green", False, False, "Crenshaw")
    Crenshaw.add_pairing(["proscuitto"])
    all_melon_types.append(Crenshaw)

    Yellow_Watermelon = MelonType("yw", "2013", "yello", False, True, "Yellow Watermelon")
    Yellow_Watermelon.add_pairing(["ice cream"])
    all_melon_types.append(Yellow_Watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:

        name = melon.name
        print(f"{name} pairs with")
        for pairing in melon.pairings:
            print(f"-{pairing}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

    melon_type_by_code = {}
    for melon in melon_types:
        if melon.code not in melon_type_by_code:
            melon_type_by_code[melon.code] = melon

    return melon_type_by_code

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest

    def __init__(self, melon_type, shape_rating, color_rating, field, harverster):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harverster = harverster

    def is_sellable(self, shape_rating, color_rating, field):
        return shape_rating > 5 and color_rating > 5 and field != 3

    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melon_by_id = make_melon_type_lookup(melon_types)

    Melon1 = Melon(melon_by_id["yw"], 8, 7, 2, "Sheila")
    Melon2 = Melon(melon_by_id["yw"], 3, 4, 2, "Sheila")
    Melon3 = Melon(melon_by_id["yw"], 9, 8, 3, "Sheila")
    Melon4 = Melon(melon_by_id["cas"], 10, 6, 35, "Sheila")
    Melon5 = Melon(melon_by_id["cren"], 8, 9, 35, "Michael")
    Melon6 = Melon(melon_by_id["cren"], 8, 2, 35, "Michael")
    Melon7 = Melon(melon_by_id["cren"], 2, 3, 4, "Michael")
    Melon8 = Melon(melon_by_id["musk"], 6, 7, 4, "Michael")
    Melon9 = Melon(melon_by_id["yw"], 7, 10, 3, "Sheila")

    melons.extend([Melon1, Melon2, Melon3, Melon4, Melon5, Melon6, Melon7, Melon8, Melon9])

    return melons

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons: 
        harvester = melon.harverster
        field = melon.field
        sellable = "CAN BE SOLD" if melon.is_sellable(melon.shape_rating, melon.color_rating, melon.field) else "UNSELLABLE"

        print(f"Harvested by {harvester} from field {field} {sellable}")
























