#**************************************************
# Activity 3.1.3 - combo menu - iteration 1
# Author: Micah T
# Variables:
#   sandwich - user's input
#   total - total cost of order
#   sandwich_selected - bool, was sandwich ordered
#***************************************************


# initialize variables
total = 0.0
sandwich_selected = True
beverage_selected = True
fries_selected = True

# iteration 1 - prompt user for sandwich type
print("Sandwich Menu:\nChicken - $5.25\nBeef - $6.25\nTofu - $5.75\n")
sandwich = input("Which sandwich would you like?\nType none for no sandwich")

if (sandwich == "Chicken"):
  total += 5.25
elif (sandwich == "Beef"):
  total += 6.25
elif (sandwich == "Tofu"):
  total += 5.75
else:
  print("No sandwich selected!")
  sandwich_selected = False

# iteration 2 - prompt user for drink
beverage_selected = input("\nWould you like a drink?")

if(beverage_selected == "Yes"):
  beverage_selected = True
elif(beverage_selected == "No"):
  beverage_selected = False
  
if(beverage_selected == True):
  print("Sizes:\nSmall - $1.00\nMedium - $1.75\nLarge - $2.25")
  drink = input("\nWhat size would you like?")
  
  if(drink == "Small"):
    total += 1.0
    print("You have selected:", drink)
  elif(drink == "Medium"):
    total += 1.75
    print("You have selected:", drink)
  elif(drink == "Large"):
    total += 2.25
    print("You have selected:", drink)
  else:
    print("No drink selected!")
    
else:    
  print("No drink selected!")

# iteration 3 - prompt user for french fires
fries_selected = input("\nWould you like french fries?")

if(fries_selected == "Yes"):
  fries_selected = True
elif(fries_selected == "No"):
  fries_selected == False
  
if(fries_selected == True):
  print("Sizes:\nSmall - $1.00\nMedium - $1.50\nLarge - $2.00")
  fries = input("\nWhat size would you like?")
  
  if(fries == "Small"):
    mega = input("Would you like to mega-size your fries?")
    if(mega == "Yes"):
      fries = "Large"
    else:
      total += 1.0
      print("You have chosen:", fries)
      
  if(fries == "Medium"):
    total += 1.5
    print("You have chosen:", fries)
  elif(fries == "Large"):
    total += 2.0
    print("You have chosen:", fries)
  else:
    print("No fries chosen!")
else:
  print("No fries chosen!")
  
print("Your total is:", total)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
