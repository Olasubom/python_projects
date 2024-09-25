


# def picnic(shopping_list):

#     print("YOUR LIST")

#     while shopping_list:
#         print(f"current shopping list: {shopping_list}")
#         package_item = input("enter the item packed: ")

#         if package_item in shopping_list:
#             shopping_list.remove(package_item)
#         else:
#             print("item not found in list")
# shopping_list = ["apple" , "mango" , "bread" , "drinks" , "cherry" , "bliss"] 
# shopping_list.append("drinks")
# start = picnic(shopping_list)
# print(start)
# print("enjoy your picnic.......")


# def inventory(products , price):
#     products__name = list(products.keys())
#     products_quantities = list(products.values())

#     for i in range(len(products)):
#         print(f"product: {products__name[i]} , quantities: {products_quantities[i]} , price: ${price[i]}")
    
#     total_value = 0

#     for i in range(len(products)):
#         total_value += price[i] * products_quantities[i]
#     print(f"total value = ${total_value}")
#     return total_value

# products = {"apple": 20,"mango" : 28,"orange": 10,"cherry": 19,"watermelon": 24}
# price = [30,48,20,24, 49]
# start = inventory(products , price)
# print(start)
# print("calculation completed.......\n")


# def prime(numbers):
#     prime_num = []

#     for num in numbers:
#         if num < 1:
#             continue
    
#         is_prime = True

#         for i in range(2 , num):
#            if num % i == 0:
#                 is_prime = False
#                 break
    
#         if is_prime:
#             prime_num.append(num)
#     return prime_num

# numbers = [1,3,11,5,6,15,12,17,20,22,25,55]
# start = prime(numbers)
# print(f"prime numbers in the list {start}")




# def closure(i):

#     def add(x):
#         return x + i
#     return add
# add_5 = closure(5)
# print(add_5(10))


# def square(numbers):
#     return map(lambda x: x ** 2 ,  numbers )
# numbers = [1,2,3,4,5,6,7,8]
# start = list(square(numbers))
# print(start)



# def calculator():

#     cal_one  = int(input("input any number: "))
#     cal_two = int(input("input any number: "))

#     print("choose an operator")
#     print("choose any operators")
#     print("1. addition (+)")
#     print("2. subtraction (-)")
#     print("3. multiplication (*)")
#     print("4. division (/)")
#     print("5. modulus (%)")
#     operators = input("input an operator:\n")

#     if operators == "1":
#             result =  cal_one + cal_two
#             print(f"{cal_one} + {cal_two} = {result}")
#     elif operators == "2":
#             result =  cal_one - cal_two
#             print(f"{cal_one} - {cal_two} = {result}")
#     elif operators == "3":
#             result =  cal_one * cal_two
#             print(f"{cal_one} * {cal_two} = {result}")
#     elif operators == "4":
#             result =  cal_one / cal_two
#             print(f"{cal_one} / {cal_two} = {result:.2f}")
#     elif operators == "5":
#             result =  cal_one % cal_two
#             print(f"{cal_one} % {cal_two} = {result}")
#     else:
#         print("enter a valid operator")

# calculator()


# class ProcessError(Exception):
#     pass
# class NoIngridentFound(ProcessError):
#     def __init__(self, item):
#         super().__init__(f"{item} not found in inventory")
# class IngredentAdded(ProcessError):
#     def __init__(self, item ):
#         super().__init__(f"{item} has been added to the list")
# class IngredientNotFoundInRecipe(ProcessError):
#     def __init__(self, ingredient):
#         super().__init__(f"No recipes found containing {ingredient}")

# class Recipe:
#     def __init__(self , name ,ingredients= None, instruction=None):
#         self.name = name 
#         self.ingredients = ingredients if ingredients else []
#         self.instruction = instruction if instruction else ""
#     def ingrident_ava(self):
#         try:
#             if not self.ingredients:
#                 raise NoIngridentFound()
#             print(f"Current ingridents: {self.ingredients}")
#         except NoIngridentFound as error:
#             print(error)
    
#     def add_ingre(self,item ):
#         try:
#             if item in self.ingredients:
#                 raise IngredentAdded(item)
#             self.ingredients.append(item)
#             print(f"{item} has been added")
#             self.ingrident_ava()
#         except IngredentAdded as error:
#             print(error)
#     def remove_ingre(self, item):
#         try:
#             if item not in self.ingredients:
#                 raise NoIngridentFound(item)
#             self.ingredients.remove(item)
#             print(f"{item} has been removed from the list")
#             self.ingrident_ava()
#         except NoIngridentFound as error:
#             print(error)
#     def print_instruction(self):
#         print(f"\nRecipe for {self.name}")
#         print(self.instruction)
#     def search_for_recipe(recipes , ingredient):
#         found_recipe = []
#         for recipe  in recipes:
#             if ingredient in recipe.ingredients:
#                 found_recipe.append(recipe.name)
#         if found_recipe:
#             print(f"Recipes containing {ingredient}: {', '.join(found_recipe)}")
#         else:
#             raise IngredientNotFoundInRecipe(ingredient)



# recipe1 = Recipe("Pancakes", ["flour", "milk", "egg", "butter"], "1. Mix ingredients.\n2. Cook on stove.")
# recipe2 = Recipe("Omelette", ["egg", "cheese", "butter"], "1. Beat eggs.\n2. Cook in pan with cheese and butter.")

# recipe1.add_ingre("sugar")
# recipe1.add_ingre("butter")
# recipe1.remove_ingre("butter")
# recipe1.print_instruction()
# all_recipes = [recipe1, recipe2]
# try:
#     Recipe.search_for_recipe(all_recipes, "cheese")
#     Recipe.search_for_recipe(all_recipes, "milk")
#     Recipe.search_for_recipe(all_recipes , "bread")
# except IngredientNotFoundInRecipe as error:
#     print(error)



# print("")




# class PRODUCT:
#     total_price = 0
#     def __init__(self , name , price , quantity = None):
#         self.name = name
#         self.price  = price
#         self.quantity = quantity
#     def __str__(self):
#         return f"{self.name} - {self.price} (Quantity: {self.quantity})"
   
# class CART:
#     def __init__(self):
#         self.product = []
#     def add_item(self,item):
#         for i in self.product:
#             if i.name == item.name:
#                 i.quantity += item.quantity
#                 print(f"Added {item.quantity} more of {item.name} to the cart.")
#                 return
#         self.product.append(item)
#         print(f"{item} has been added to the cart")
#     def remove_item(self , item):
#         for i in self.product:
#             if i.name == item:
#                 self.product.remove(i)
#                 print(f"{item} has been removed from cart")
#                 return
#         print("item not found in cart")
      
#     def calculate_total(self):
#         total_price = sum(item.price * item.quantity for item in self.product)
#         print(f"Total price {total_price}")
#         return total_price
#     def show_info(self):
#         if not self.product:
#             print("Your cart is empty.")
#         else:
#             print("Items in your cart:")
#             for item in self.product:
#                 print(item)



# product1 = PRODUCT("Laptop", 1000.00, 1)
# product2 = PRODUCT("Headphones", 200.00, 2)
# product3 = PRODUCT("Mouse", 50.00, 1)
# product4 = PRODUCT("Laptop", 1000.00, 1)
# cart = CART()
# cart.add_item(product1)
# cart.add_item(product2)
# cart.add_item(product3)
# cart.show_info()
# cart.remove_item("Mouse")
# cart.add_item(product4)
# cart.show_info()
# cart.calculate_total()



