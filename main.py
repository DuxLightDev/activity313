#**************************************************
# Activity 3.1.3 - Combo Menu - Iteration 1
# Author: Collin G.
# Variables:
#   sandwich - user's input
#   total - total cost of order
#   sandwich_selected - bool, was sandwich ordered
#***************************************************


# initialize variables
total = 0.0
sandwich_selected = True
beverage_selected = True

# iteration 1 - prompt user for sandwich type
print("Sandwich Menu:\n1. Chicken - $5.25\n2. Beef - $6.25\n3. Tofu - $5.75\n")
sandwich = input("Which one would you like?\nType none for no sandwich")
if (sandwich == "Chicken"):
  total += 5.25
elif (sandwich == "Beef"):
  total += 6.25
elif (sandwich == "Tofu"):
  total += 5.75
else:
  sandwich_selected = False
