# Create a class called "Class" that is meant to hold the details
# of a class in a school.

# This class should have variables for the following:
# - subject - string, e.g., math, english, computer science
# - level - string, e.g., honors, high honors, ap
# - topic - string, e.g., pre-calculus, computer science principles
# - credit value - float, e.g., 1, 0.5
# - roster - list of strings, start by giving them at least one name

# The class should have methods for the following:
# - __init__()
# - __str__()
# - Adding a student (adding their name to the list if not already in it)
# - Dropping a student (removing their name from the list if it is there)
# - Property (get, set) methods for subject, level, topic, credit value
#   - credit value should not be allowed to be 0 (or less) or greater than 1

from re import A


class Class:
    def __init__(
        self, sub: str, lev: str, top: str, cred: float, roster: list[str]
    ) -> None:
        self._subject = sub
        self._level = lev
        self._topic = top
        self._credit_value = cred
        self.roster = roster

    def __str__(self) -> str:
        return f"This class is {self.level} {self.subject} {self.topic} worth {self.credit_value} credit(s)."

    def add_student(self, name: str) -> None:
        if not (name in self.roster):
            self.roster.append(name)
            print(f"{name} has been added to the roster!")
        else:
            print(f"{name} is already in the roster!")

    def drop_student(self, name: str) -> None:
        if name in self.roster:
            self.roster.remove(name)
            print(f"{name} has been removed from the roster!")
        else:
            print(f"{name} was not in the roster to remove")

    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, sub: str) -> None:
        self._subject = sub

    @property
    def level(self) -> str:
        return self._level

    @level.setter
    def level(self, lev: str) -> None:
        self._level = lev

    @property
    def topic(self) -> str:
        return self._topic

    @topic.setter
    def topic(self, top: str) -> None:
        self._topic = top

    @property
    def credit_value(self) -> float:
        return self._credit_value

    @credit_value.setter
    def credit_value(self, val: float) -> None:
        if val > 0 and val <= 1:
            self._credit_value = val
        else:
            print(f"Cannot have {val} credits as a value")


# Create two instances of "Class" for two classes you are taking right
# now. For each one, add three students, remove one student, and
# modify the level and credit value.
apcs4b = Class("Computer Science", "AP", "Principles", 1.0, ["Mr. G"])
print(apcs4b)

hprecalc3b = Class("Math", "Honors", "Pre-Calculus", 1.0, ["Mr. G"])
print(hprecalc3b)

apcs4b.add_student("Jayda")
apcs4b.add_student("Josiah")
apcs4b.add_student("Patrick")

apcs4b.drop_student("Mr. G")

apcs4b.level = "High Honors"
print(apcs4b)

apcs4b.credit_value = 2.0
print(apcs4b)

hprecalc3b.add_student("Cody")
hprecalc3b.add_student("David")
hprecalc3b.add_student("Tristan")

hprecalc3b.drop_student("Mr. G")

hprecalc3b.level = "High Honors"
print(hprecalc3b)

hprecalc3b.credit_value = 0.75
print(hprecalc3b)

# Create a class called "HotDrink" that is meant to hold information
# about a hot beverage (like something you could have ordered at
# Dunkin or Starbucks)

# This class should have variables for the following:
# - type - string, e.g., coffee, tea, etc.
# - subtype - string, e.g., dark roast, decaf, gray, etc.
# - size - string, e.g., small, medium, or large
# - cream - boolean
# - sugar - boolean
# - quantity_left - float, from 0 for empty to 1 for full

# The class should have methods for the following:
# - __init__()
# - __str__()
# - Property methods for type, subtype, size, cream, sugar, quantity_left
#   - For modifying cream and sugar, prevent the user from removing
#     (turning True to False), as you can't take cream out of coffee/tea
#     once you put it in.
# - drink method which decreases the quantity by some amount, and prints
#   something if the cup is now empty. Should remove less of the amount
#   the bigger the size (i.e., large removes 0.02, small removes 0.1)
# - refill method which resets the quantity_left to 1 regardless of size
class HotDrink:
    def __init__(
        self, type: str, subtype: str, size: str, cream: bool, sugar: bool, quant: float
    ) -> None:
        self._type = type
        self._subtype = subtype
        self._size = size
        self._cream = cream
        self._sugar = sugar
        self._quantity_left = quant

    def __str__(self) -> str:
        return f"This is a {self._size} {self._subtype} {self._type}"

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, typ: str) -> None:
        self._type = typ

    @property
    def subtype(self) -> str:
        return self._subtype

    @subtype.setter
    def subtype(self, sub: str) -> None:
        self._subtype = sub

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, siz: str) -> None:
        self._size = siz

    @property
    def cream(self) -> bool:
        return self._cream

    @cream.setter
    def cream(self, crm: bool) -> None:
        if crm:
            self._cream = crm
        elif self._cream:
            print("Cannot take cream out!")

    @property
    def sugar(self) -> bool:
        return self._sugar

    @sugar.setter
    def sugar(self, sug: bool) -> None:
        if sug:
            self._sugar = sug
        elif self._sugar:
            print("Cannot take sugar out!")

    @property
    def quantity_left(self) -> float:
        return self._quantity_left

    @quantity_left.setter
    def quantity_left(self, left: float) -> None:
        self._quantity_left = left

    def drink(self) -> None:
        if self._size == "Small":
            self._quantity_left -= 0.1
        elif self._size == "Medium":
            self._quantity_left -= 0.05
        elif self._size == "Large":
            self._quantity_left -= 0.02

    def refill(self) -> None:
        self._quantity_left = 1


# Create three instances of "HotDrink" for three different hot drinks.
# For each one, add cream, remove sugar (try to), drink twice and print
# the quantity_left, then refill the cup and report the quantity.
drink1 = HotDrink("Coffee", "Decaf", "Medium", True, True, 1.0)
print(drink1)

drink2 = HotDrink("Coffee", "Dark Roast", "Large", True, False, 1.0)
print(drink2)

drink3 = HotDrink("Tea", "Earl Gray", "Small", False, True, 1.0)
print(drink3)

drink1.cream = True
drink1.sugar = False
drink1.drink()
drink1.drink()
print(f"There is {drink1.quantity_left:0.2%} left")
drink1.refill()
print(f"There is {drink1.quantity_left:0.2%} left")

drink2.cream = True
drink2.sugar = False
drink2.drink()
drink2.drink()
print(f"There is {drink2.quantity_left:0.2%} left")
drink2.refill()
print(f"There is {drink2.quantity_left:0.2%} left")

drink3.cream = True
drink3.sugar = False
drink3.drink()
drink3.drink()
print(f"There is {drink3.quantity_left:0.2%} left")
drink3.refill()
print(f"There is {drink3.quantity_left:0.2%} left")
