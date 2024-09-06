# import sys
# import string 

# greetings = ".................welcome....................."
# valid = greetings.center(50)
# print(valid)


# # Student Grades:
# # A teacher has a class of students and their corresponding grades. Store the student names and grades in a list. Calculate the average grade of the class. Find the highest and lowest grades. 
# # # Create a function that prints out the average scores from the lists. 
# # Grade them as A,B,C,D and F
# # A = 80 -100
# # B =  60 -80
# # C = 50 -60
# # D = 40 - 50
# # E = < 40

# def student_grade(grade):
#     g_o_f = sum(grade) / len(grade)
#     if g_o_f >= 80:
#         result = "A"
#     elif g_o_f >= 60:
#         result = "B"
#     elif g_o_f >= 50:
#         result ="C"
#     elif g_o_f >= 40:
#         result = "D" 
#     else:
#         result = "F"
#     return g_o_f, result
# result_n = input("input your result: ")
# result_com = [int (x) for x in result_n.split()] 
# g_o_f , result = student_grade(result_com)
# print(f"your average score is {g_o_f:.2f}")
# print(f"{result}") 



# # Inventory Management:
# # A store wants to track product inventory. Create a dictionary where product names are keys and quantities are values. Calculate the total value of the inventory based on product prices stored in a separate list.

# inventory = "bread" , "corn" , "beans" , "rice" , "mango" ,"apple"
# quantities = 20 , 45 , 34 , 50 , 20 , 40

# inventory_two = {"bread": 20 , "corn" : 45 , "beans": 35 , "rice" : 50 , "mango" : 20 , "apple" : 40}

# print(inventory_two)
# print(type(inventory_two))

# for  details in inventory_two.items():
#     details = [20 , 45 , 34 , 50 , 20 , 40]
#     quantity = sum(details)
#     print(f"quantity :${quantity}")
# inventory = {
#     "Apples": (30, 100),
#     "Bananas": (45 ,50),
#     "Oranges": (20, 80),
#     "Mangoes": (10 ,150)
# }

# # prices = {
# #     "Apples": 100,
# #     "Bananas": 50,
# #     "Oranges": 80,
# #     "Mangoes": 150
# # }

# # Calculate total value of the inventory
# total_value = 0
# for product, quantity in inventory.items():
#     # Get the price of the product from the prices dictionary
#     price , product = quantity
#     print(f"{product} : {price}")

# # Output the total value
# # print(f"Total value of the inventory: N{total_value}")


# def calculate_inventory_value(inventory, prices):
#   """Calculates the total value of the inventory.

#   Args:
#     inventory: A dictionary where keys are product names and values are quantities.
#     prices: A list of tuples, where each tuple contains a product name and its price.

#   Returns:
#     The total value of the inventory.
#   """

#   price_dict = dict(prices)  # Convert price list to a dictionary for efficient lookup
#   total_value = 0

#   for product, quantity in inventory.items():
#     if product in price_dict:
#       total_value += quantity * price_dict[product]
#     else:
#       print(f"Price for {product} not found.")

#   return total_value

# # Example usage:
# inventory = {"apple": 30, "banana": 45, "orange": 20 , "mango": 10}
# prices = {"apple": 100, "banana": 50 , "orange": 80 , "mango": 150}

# total_value = calculate_inventory_value(inventory, prices)
# print("Total inventory value:", total_value)


# # a. Shopping List: You're planning a picnic. Create a shopping list of items you need. As you add items, you realize you need to buy double the amount of drinks. After shopping, remove items from your list as you pack them.

# def shopping():
#   shopping_list = ["bread", "apple","popcorn","drink","mango","cherry"]
#   shopping_list.append("drink")
#   print("Your list")

#   while shopping_list:
#       print(f"current shopping list: {shopping_list}\n")

#       packed_items = input("enter the item you packed: ")

#       if packed_items in shopping_list:
#           shopping_list.remove(packed_items)
#           print(f"your {packed_items} has been packed\n")
#       else:
#           print(f"{packed_items} is not in list......\n")
# shopping()
# print("enjoy your picnic")   

# print("")

# # b. Student Scores: A teacher has a list of student names and their corresponding test scores. Calculate the class average, the highest, and the lowest score.
# def student_score():
#     student_name = ["bola","adekunle","adebayo","tunde","joe","kemi"]
#     test_score = [45,36,27,89,44,79,]
#     class_ave = round (sum(test_score) / len(test_score))
#     print(f"the class average is {class_ave}")

#     highes_score = max(test_score)
#     lowest_score = min(test_score)

#     hight_student = test_score.index(highes_score)
#     lowest_student = test_score.index(lowest_score)

#     for x in range(len(student_name)):
#          print(f"Name:{student_name[x]} score:{test_score[x]}")   

#     print(f"the highest score is {highes_score} by {student_name[hight_student]}")
#     print(f"the lowest score is {lowest_score} by {student_name[lowest_student]}")     
# student_score()

# print("")
# # Password Validation: Create a function to check if a password meets certain criteria (e.g., minimum length, at least one uppercase letter, one lowercase letter, and one number)
# def password_validation():
#      while True:
#       input_pass = input("PASSWORD: ")
#       if len(input_pass) != 3:
#             print("must be 3 ")
#             continue

#       if (not any ((x.isupper()) for x in input_pass) or 
#           not any ((x.islower()) for x in input_pass) or
#           not any ((x.isdigit()) for x in input_pass)):
#           print("at least one uppercase letter, one lowercase letter, and one number")
#           continue
#       print("password valid")
#       break

# password_validation()      
# #  Product Catalog: A store wants to track product information: name, price, and quantity. Store this information in tuples. Calculate the total value of the inventory.

# def product_category():
#   name = ("apple" , "mango","melon","cherry","orange")
#   price = (32 , 45, 50 , 23, 44)
#   quantity = (10 ,15,9,23,15)
#   for i in range(len(name)):
#       product = (f"{name[i]}",f"price: ${price[i]}", f"quantity: {quantity[i]}")
#       print(product)
#   total_value = 0

#   for i in range(len(name)):
#      total_value += price[i] * quantity[i]
#   print(f"your total value: {total_value}")
#   return total_value
# product_category()
# print("")
# # Customer Data: A company stores customer information in tuples: name, age, and city. Find the average age of customers.
# def costomer_data():
#     name = "kemi","bayo","temi","qudus","bola","ezekel"
#     age = 40,30,67,41,28,31
#     city = "lagos","ekiti","ibadan","osun","lagos","lagos"

#     for i in range(len(name)):
#         contact = (f"NAME: {name[i]}",f" AGE: {age[i]}",f" CITY: {city[i]}")
#         print(contact)

#     average = round(sum(age) / len(age))
#     print(f"total average age of customers is {average} years")
#     return average
# costomer_data()
# print("")
# # Email Analysis: Analyze a list of emails. Count the number of emails from each domain (using string manipulation and dictionaries).
# def emails():
#     list_of_mails = ["olasubomiadebayo90@gmail.com",
#         "olabayo10@gmail.net",
#         "adeyemiadekunle114@gmail.ko",
#         "olabisiadebayo@gmail.net",
#         "productcompany@gmail.org"
#       ]
        
#     count = {}
#     for email in list_of_mails:
#         domain = email.split("@")[-1]
#         count[domain] = count.get(domain, 0) + 1
    
      
#     return count
# result = emails()
# print(result)
# print("")
# #  Sales Report: A store has a list of products and their prices (tuples). Calculate the total sales based on a list of purchased items (list of product names)
# def sales_report(product ,purchased_items):
#     product_1 = dict(product) 
#     total = 0


#     for item in purchased_items:
#         if item in product_1:
#             total += product_1[item]
#         else:
#             print(f"{item} not found")
         
#     return total 
# product = [("apple",30) ,("banana",20),("mango",15),("orange",32)]
# purchased_items = ["apple","mango","apple","cherry","orange"]
# result = sales_report(product , purchased_items)  
# print(f"total sals :${result}")


# def grocery_store():
#     store = [
#         {"item" : "apple", "quantities" : 5},
#         {"item" : "mango", "quantities" : 2},
#         {"item" : "carrot", "quantities" : 6},
#         {"item" : "cherry", "quantities" : 11},
#         {"item" : "bread", "quantities" : 21},
#         {"item" : "oramge", "quantities" : 10}
#     ]

#     item_above_10 = filter(lambda num : num["quantities"] > 10 ,store)
#     item_names = list(map(lambda num : num["item"],item_above_10))
#     print(f"the list of items with quantities greater than 10 {item_names}")

# grocery_store()

# def student_grades():
#     grades = [
#         ("kunle ojo", 68),
#         ("kemi ade" , 70),
#         ("toyin ojo" , 54),
#         ("tunde ojo" , 79),
#         ("adebayo ola" ,63),
#         ("bola ayo", 89)
#     ]

#     grade_greater = filter(lambda gra : gra[1] >= 70 , grades)
#     name = list(map(lambda gra : gra[0],grade_greater))
#     print(f"students that passed: {name}")
# student_grades()


# def employee_salaries(employees):
   
#     salaries = list (map(lambda avg : avg[1] ,employees))
#     avg_salaries = sum(salaries) / len(salaries)
#     avg_amount = filter(lambda avg : avg[1] > avg_salaries , employees)
#     employees_name = list(map(lambda avg : avg[0], avg_amount))

#     print(f"employees earning more than average: {employees_name}")

       
        
# employees = [("kunle",120000),("john",240000),("bola", 120000), 
#         ("tolu", 220000),("batolu", 120000)]
# result = employee_salaries(employees)

# class BOOK:
#     def __init__(self , title, author , publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.status = "Avaliable"
#         self.due_date = None

#     def book_taken_date(self , due_date):
#         if self.status == "Avaliable":
#             self.status = "checked out"
#             self.due_date = due_date
#             print(f"Book {self.title} checked out for {self.due_date}")
#         else:
#             print(f"Book {self.title} has been checked out")

#     def return_book(self , days_kept):
#         if self.status == "checked out":
#             overdue_days = days_kept - self.due_date if days_kept > self.due_date else 0
#             if overdue_days > 0:
#                 fine = self.calculate_fine(overdue_days)
#                 print(f"Book {self.title} has been overdue by {overdue_days}. fine: {fine:.2f}")
#                 self.status = "Avaliable"
#                 self.due_date = None
#             else:
#                 print(f"book {self.title} has been returned on time")
#         else:
#             print(f"book {self.title} is already avaliable")

#     def calculate_fine(self , overdue_days):
#         fine_to_pay = 10.2
#         return fine_to_pay * overdue_days
#     def update_statuse(self , new_statuse):
#         self.status = new_statuse
#         print(f"the book {self.title} as been updated to {self.status}")

# start = BOOK("rapid fire","dave john", 20-4-1948)
# start.book_taken_date(7)
# start.return_book(18)
# start.update_statuse("Avaliable")
#instansiate




class TASK:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_task(self):
        self.is_completed = True
        print("Task has been completad ")

    def __str__(self):
        statuse = "Completed" if self.is_completed else "Not Completed"
        return f" Task: {self.description} Due date :{self.due_date}  statuse: {statuse}"
class Task_manager:
    def __init__(self):
        self.task = []

    def add_task(self , task):
        self.task.append(task)
        print(f" Task '{task.description}' added")
    def remove_task(self , task_description):
        for task in self.task:
            if  task.description ==  task_description:
                self.task.remove(task)
                return
        print(f"task {task_description} not found")
    def mark_task(self , task_description):
        for task in self.task:
            if  task.description ==  task_description:
                task.mark_task()
                return
        print(f"task {task_description} not found")
    def sort_due_date(self):
        self.task.sort(key=lambda task: task.due_date)
        print('task has been sorted by due date')  
    def show_task(self):
        if not self.task:
            print("no task added")
        for task in self.task:
            print(task)

if __name__=="__main__":
    start = Task_manager()

task_1 = TASK("print this code", "2024-29-08")
task_2 = TASK("look around ","2024-22-08")
task_3 = TASK("print this code and look","2024-27-08")

start.add_task(task_1)
start.add_task(task_2)
start.add_task(task_3)
print("\nshow tasks")
start.show_task()
print("\nSorting task by due date")
start.sort_due_date()
start.show_task()
print("\nMark task 'print this code' as completed")
start.mark_task("print this code")
start.show_task()


# Task Class:

# description: A string describing the task.

# due_date: A string representing the due date of the task (e.g., "2023-09-10").

# is_completed: A boolean indicating whether the task has been completed (default is False).

# mark_as_completed(): Marks the task as completed.

# __str__(): Returns a string representation of the task for easy printing.

# TaskManager Class:

# tasks: A list to store multiple Task objects.

# add_task(task): Adds a Task object to the tasks list.

# remove_task(task_description): Removes a task from the list by its description.

# mark_task_completed(task_description): Finds a task by its description and marks it as completed.
        