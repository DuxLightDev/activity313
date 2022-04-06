#**************************************************
# Activity 3.1.3 - combo menu - iteration 1
# Author: Micah T
# Variables:
#   sandwich - user's input on which sandwich
#   drink - user's input on what drink
#   fries - user's input on what fry size
#   total - total cost of order
#   sandwich_selected - bool, was sandwich ordered
#   beverage_selected - bool, was beverage ordered
#   fries_selected - bool, was fries ordered
#   beverage_input - string, yes or no for beverage
#   fries_input - string,  yes or no for fries
#   packets - amount of ketchup ordered
#   order - list of the order
#***************************************************


# initialize variables
total = 0.0
sandwich_selected = True
beverage_selected = True
fries_selected = True
packets = 0
order = []

# iteration 1 - prompt user for sandwich type
print("Sandwich Menu:\nChicken - $5.25\nBeef - $6.25\nTofu - $5.75\n")
sandwich = input("Which sandwich would you like?\nType none for no sandwich").lower() # asking for which sandwich wanted

# adding price for each type of sandwich
if (sandwich == "chicken"):
  total += 5.25
  order.append("chicken")
elif (sandwich == "beef"):
  total += 6.25
  order.append("beef")
elif (sandwich == "tofu"):
  total += 5.75
  order.append("tofu")
else:
  print("No sandwich selected!")
  sandwich_selected = False
  order.append("nothing")

# iteration 2 - prompt user for drink
beverage_input = input("\nWould you like a drink?").lower() # beverage prompt; beverage_input = string of yes or no

# checking if yes or no for beverage
if(beverage_input == "yes"): 
  beverage_selected = True # beverage selected, used later for discount, applies to drink_selected and drink_input as well
else:
  beverage_selected = False
  drink = "none"
  order.append("nothing")

# checking which size and adding price
if(beverage_selected == True):
  print("Sizes:\nSmall - $1.00\nMedium - $1.75\nLarge - $2.25")
  drink = input("\nWhat size would you like?").lower()
  
  if(drink == "small"):
    total += 1.0
    print("You have selected:", drink)
    order.append("small")
  elif(drink == "medium"):
    total += 1.75
    print("You have selected:", drink)
    order.append("medium")
  elif(drink == "large"):
    total += 2.25
    print("You have selected:", drink)
    order.append("large")
  else:
    print("No drink selected!")
    order.append("nothing")

# iteration 3 - prompt user for french fires
fries_input = input("\nWould you like french fries?").lower()

if(fries_input == "yes"):
  fries_selected = True
else:
  fries_selected = False
  fries = "none"
  order.append("nothing")
  
if(fries_selected == True):
  print("Sizes:\nSmall - $1.00\nMedium - $1.50\nLarge - $2.00")
  fries = input("\nWhat size would you like?").lower()
  
  if(fries == "small"):
    mega = input("Would you like to mega-size your fries?").lower() # fries megasize, if small then ask if want big
    if(mega == "yes"):
      total += 2.0
      fries = "large"
      order.append("large")
    else:
      total += 1.0
      print("You have chosen:", fries)
      fries = "small"
      order.append("small")
  elif(fries == "medium"):
    total += 1.5
    print("You have chosen:", fries)
    order.append("medium")
  elif(fries == "large"):
    total += 2.0
    print("You have chosen:", fries)
    order.append("large")
  elif(fries != "small" or "medium" or "large"):
    print("No fries chosen!")
    order.append("nothing") # fix this code later, bug detailed below
    
# print(order) # debugging code for checking why it prints no fries chosen if you do not megasize small fries
# print(total)
  
# iteration 4 - prompt user for packets and repeat order and total
while True:
  try:
    packets = int(input("\nHow many packets of ketchup would you like?")) # ketchup packets, asks for amount, multiples by .25
    break
  except ValueError:
    print("You did not enter a valid integer!")

total += packets * 0.25

if(sandwich_selected == True and beverage_selected == True and fries_selected == True): # discount code, subtracts 1$ if ordered all
  total -= 1.00
  print("\nYou have been discounted for buying a combo meal!\n")
  
print("\nYou have ordered a", order[0], "sandwich, a", order[1], "drink, and", order[2], "fries!\nYou have also added", packets, "ketchup packets to your order!" ) # repeating order back
print("\nYour total is: $", str(total)) # printing total

# iteration 5 - qol

# iteration 6 - adding order to a list, other qol, ketchup packet errors
