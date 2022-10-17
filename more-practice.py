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


# Create two instances of "Class" for two classes you are taking right
# now. For each one, add three students, remove one student, and
# modify the level and credit value.


# Create a class called "HotDrink" that is meant to hold information
# about a hot beverage (like something you could have ordered at
# Dunkin (jeet and saad reference) or Starbucks)

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


# Create three instances of "HotDrink" for three different hot drinks.
# For each one, add cream, remove sugar (try to), drink twice and print
# the quantity_left, then refill the cup and report the quantity.