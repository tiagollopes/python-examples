# New commands: import, from, as
# Modules allow us to use pre-written code

# Example 1: Importing the entire math module
import math
print(f"The square root of 25 is: {math.sqrt(25)}")

# Example 2: Importing with an alias (as)
import datetime as dt
print(f"Current date and time: {dt.datetime.now()}")

# Example 3: Importing a specific function from a module
from random import randint
print(f"Random number between 1 and 100: {randint(1, 100)}")

# Example 4: Using a constant from a module
print(f"The value of PI is: {math.pi}")
