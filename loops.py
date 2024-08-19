# value =1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)



# names =["bola" ,"ade" ,"femi"]
# actions =["eats" ,"brush" ,"fights"]

# for name in names:
#     for action in actions:
#      print(name + " " + action + ".")

# print("")

# for action in actions:
#     for name in names:
#      print(name + " " + action + ".")

inventory = {
     "Apples": (1.20, 50),
     "Bananas": (0.50, 100),
     "Oranges": (0.75, 80)
     }
print("inventory")
print("**********")

for item, details in inventory.items():
   price , quantity = details
   print(f"{item}: price--${price} , quantity--{quantity}")



