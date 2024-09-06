class ListException(Exception):
    pass

class ItemNotFound(ListException):
    def __init__(self, item):
        super().__init__(f"{item} not found in inventory")

class NoItemSort(ListException):
    def __init__(self):
        super().__init__(f"No item to sort inventory empty")
class Noitemfound(ListException):
    def __init__(self):
        super().__init__("No item found in inventory")

class AddError(ListException):
    def __init__(self, item):
        super().__init__(f"{item} as been added already")

class ShoppingList:
    def __init__(self , items = None):
        if items is None:
            self.items = []
        else:
            self.items = items
    def showlist(self):
        try:
            if not self.items:
                raise Noitemfound()
            else:
                print(f"Current items: {self.items}")
        except Noitemfound as error:
            print(error)
    def additems(self, item):
        try:
            if item in self.items:
                raise AddError(item)
            self.items.append(item)
            print(f"{item} has been added to the list")
            self.showlist()
        except AddError as error:
            print(error)
    def remove_item(self, item):
        try:
            if item not in self.items:
                raise ItemNotFound(item)
            self.items.remove(item)
            print(f"{item} has been removed from the list")
            self.showlist
        except ItemNotFound as error:
            print(error)
class SortInventory(ShoppingList):
    def __init__(self, items):
        super().__init__(items)
    def sort_item(self):
        try:
            if not self.items:
                raise Noitemfound
            self.items.sort()
            print(f"item sorted: {self.items}")
            self.showlist
        except NoItemSort as error:
            print(error)

start = ShoppingList()

shopping_list = ShoppingList()

shopping_list.showlist()          # Will raise NoItemSort exception
shopping_list.additems("Apples")  # Adds "Apples" to the list
shopping_list.additems("Oranges") # Adds "Oranges" to the list
shopping_list.additems("Apples")  # Will raise AddError exception
shopping_list.remove_item("Milk")  # Will raise ItemNotFound exception
shopping_list.showlist()          # Shows the sorted list
shopping_list.remove_item("Apples")# Removes "Apples" from the list
shopping_list.showlist()
sort_inventory = SortInventory(shopping_list.items)
sort_inventory.sort_item()
sort_inventory.additems("Mango")
sort_inventory.additems("Banana")
sort_inventory.additems("Cherry")
sort_inventory.sort_item()
