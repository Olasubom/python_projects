


# class BankError(Exception):
#     pass
# class NOtsufficientAmount(BankError):
#     def __init__(self ,account_number, balance, amount):
#         super().__init__(print(f"Sorry Acccount: *{account_number}* only has a balanse of ${balance}\nAttemted Withawal Amount :{amount} not sent"))
# class BankAccount:
#     def __init__(self , name , account_number , balance ):
#         self.name = name
#         self.account_number = account_number
#         self.balance = balance
#         self.intrest_rate = 0.05
#     def account(self):
#         print(f"Account Name: {self.name} \nAccount Number: {self.account_number}\nBalance: ${self.balance}")
    
#     def deposit(self , amount):
#         self.balance = self.balance + amount
#         print(f"Deposit made to {self.account_number} ")
#         print("Deposit Completed.....")
#         self.account()
#     def withdraw(self, amount):
#         try:
#             if amount > self.balance:
#                 raise NOtsufficientAmount(self.account_number,self.balance , amount)
#             self.balance -= amount
#             print("withdrawal completed...")
#         except NOtsufficientAmount as error:
#             print(error)
#             self.account()
#     def calculate_intrest(self):
#         intrest = self.balance * self.intrest_rate
#         print(f"Total intrest on account {self.account_number}: {intrest}")
#         return intrest
    
#     def check_overdue(self):
#         if self.balance < 0:
#             print(f"Account : {self.account_number} is Overdue")
#             return True
#         else:
#             print(f"Account: {self.account_number} is not Overdue")
#             return False


    
# account1 = BankAccount("joe" , 81167524 , 1000)

# account1.deposit(500)
# account1.withdraw(2000)
# account1.check_overdue()
# account1.calculate_intrest()
# account1.deposit(20000)




# class Task:
#     def __init__(self  , description , due_date):
#         self.description = description
#         self.due_date = due_date
#         self.is_completed = False

#     def mark_task(self):
#         self.is_completed = True
#         print("Task has been completed")
    
#     def __str__(self):
#         status = "Completed" if self.is_completed else "Not Completed"
#         return f"Task: {self.description} Due Date: {self.due_date} Status: {status}"


# class TaskManager:
#     def __init__(self):
#         self.task = []

#     def add_task(self , task):
#         self.task.append(task)
#         print(f"Task {task.description} was added")
    
#     def remove_task(self , task_description):
#         for task in self.task:
#             if task.description == task_description:
#                 self.task.remove(task)
#                 return
#         print(f"404\nTask {task_description} not found")
#     def mark_task(self , task_description):
#         for task in self.task:
#             if task.description == task_description:
#                 task.mark_task()
#                 return
#         print(f"404\nTask {task_description} not found")

#     def sort_due_date(self):
#         self.task.sort(key=lambda task: task.due_date)
#         print('task has been sorted by due date')  
#     def show_task(self):
#         if not self.task:
#             print("no task added")
#         for task in self.task:
#             print(task)

        
# start = TaskManager()
# task_1 = Task("print this code", "2024-29-08")
# task_2 = Task("look around","2024-22-08")
# task_3 = Task("print this code and look","2024-27-08")

# start.add_task(task_1)
# start.add_task(task_2)
# start.add_task(task_3)
# print("\nshow tasks")
# start.show_task()
# print("\nSorting task by due date")
# start.sort_due_date()
# start.show_task()
# print("\nMark task 'print this code' as completed")
# start.mark_task("print this code")
# start.show_task()
# start.mark_task("look around")
# start.show_task()
    